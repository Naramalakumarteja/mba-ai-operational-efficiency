"""Critical tests for source consistency, portability, and usable HTML output."""

import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

from build_report import build, load_sources, render, validate_source


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.tables = 0
        self.scripts = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "a":
            self.links.append(attributes.get("href", ""))
        self.tables += tag == "table"
        self.scripts += tag == "script"


class ReportTests(unittest.TestCase):
    def test_current_sources_are_valid(self):
        validate_source(load_sources())

    def test_questionnaire_is_included_once(self):
        source = load_sources()
        self.assertEqual(source.count("A07b. Did operational AI use stop"), 1)

    def test_missing_source_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, "Required source is missing"):
            load_sources(Path("not-a-real-report.md"))

    def test_missing_chapter_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Chapter 4"):
            validate_source(load_sources().replace("# Chapter 4:", "# Missing chapter:"))

    def test_machine_paths_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Machine-specific"):
            validate_source(load_sources() + "\nC:/Users/example/report.md")

    def test_html_navigation_and_tables(self):
        page = PageParser()
        page.feed(render(load_sources()))
        self.assertEqual(len(page.ids), len(set(page.ids)))
        internal = [link[1:] for link in page.links if link.startswith("#")]
        self.assertGreaterEqual(len(internal), 7)
        self.assertTrue(all(anchor in page.ids for anchor in internal))
        self.assertGreaterEqual(page.tables, 5)
        self.assertTrue(any(link.startswith("https://doi.org/") for link in page.links))

    def test_raw_html_is_not_executed(self):
        page = PageParser()
        page.feed(render(load_sources() + "\n<script>alert('unsafe')</script>\n"))
        self.assertEqual(page.scripts, 0)

    def test_build_writes_portable_file(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build(Path(directory) / "nested" / "report.html")
            text = output.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("<!doctype html>"))
            self.assertNotIn("C:/Users/", text)
            self.assertIn('name="viewport"', text)
            self.assertIn("window.print()", text)
            self.assertNotRegex(text, r'<(?:link|script)[^>]+(?:src|href)="https?://')

    def test_unreadable_output_fails_instead_of_reporting_success(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(OSError):
                build(Path(directory))

    def test_empty_sources_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / 'report.md'
            questionnaire = Path(directory) / 'questionnaire.md'
            report.write_text('', encoding='utf-8')
            questionnaire.write_text('Questionnaire', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'must not be empty'):
                load_sources(report, questionnaire)


if __name__ == "__main__":
    unittest.main()
