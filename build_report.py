"""Build the existing MBA research documents into an offline, printable report."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "outputs" / "MBA_Project_Chapters_1_to_3.md"
QUESTIONNAIRE = ROOT / "outputs" / "MBA_Draft_Questionnaire.md"

CSS = """
:root{color-scheme:light;--ink:#1b2938;--muted:#526578;--accent:#125e69;--line:#d7e1e5}
*{box-sizing:border-box}body{margin:0;background:#f0f4f5;color:var(--ink);font:17px/1.7 Georgia,serif}
.shell{display:grid;grid-template-columns:270px minmax(0,920px);gap:36px;max-width:1260px;margin:auto;padding:32px}
nav{font:14px/1.5 system-ui,sans-serif;position:sticky;top:24px;align-self:start;max-height:90vh;overflow:auto}
nav a{display:block;padding:8px 0;color:var(--accent);text-decoration:none;border-bottom:1px solid var(--line)}
nav a:hover,nav a:focus{text-decoration:underline}main{background:white;padding:48px;border-radius:8px;min-width:0}
h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.3;scroll-margin-top:24px}h1{font-size:1.8rem;margin-top:48px}
h1:first-child{margin-top:0}h2{font-size:1.3rem;margin-top:36px}h3{font-size:1.1rem;margin-top:28px}
a{color:var(--accent);overflow-wrap:anywhere}p,li{overflow-wrap:anywhere}.table-wrap{overflow-x:auto;margin:24px 0}
table{border-collapse:collapse;width:100%;font:14px/1.5 system-ui,sans-serif}th,td{padding:12px;text-align:left;border:1px solid var(--line);vertical-align:top}
th{background:#eaf1f3}code{font-size:.9em;background:#f0f4f5;padding:2px 4px}.badge{padding:16px;border-left:4px solid var(--accent);background:#eaf1f3;font:14px/1.6 system-ui,sans-serif;margin-bottom:32px}
button{background:var(--accent);color:white;border:0;border-radius:4px;padding:12px 18px;cursor:pointer;font:inherit;margin:16px 0}
button:focus-visible,a:focus-visible{outline:3px solid #d98218;outline-offset:3px}footer{font:13px/1.5 system-ui,sans-serif;color:var(--muted);border-top:1px solid var(--line);padding-top:20px;margin-top:40px}
@media(max-width:800px){.shell{display:block;padding:16px}nav{position:static;max-height:none;margin-bottom:24px}main{padding:24px}h1{font-size:1.5rem}}
@media print{@page{size:A4;margin:18mm}body{background:white;font-size:11pt}.shell{display:block;padding:0}nav,button{display:none}main{padding:0;border-radius:0}h1{break-before:page}h1:first-child{break-before:auto}h1,h2,h3{break-after:avoid}.table-wrap{overflow:visible}table{font-size:9pt}tr{break-inside:avoid}a{color:inherit}.badge{font-size:9pt}footer{font-size:9pt}}
"""


def load_sources(report: Path = REPORT, questionnaire: Path = QUESTIONNAIRE) -> str:
    """Use the standalone questionnaire as the single appendix source."""
    for path in (report, questionnaire):
        if not path.is_file():
            raise ValueError(f"Required source is missing: {path.name}")
    source = report.read_text(encoding="utf-8-sig")
    source = source.split("# Appendix A: Draft Survey Instrument", 1)[0].rstrip()
    survey = questionnaire.read_text(encoding="utf-8-sig").strip()
    if not source or not survey:
        raise ValueError("Report and questionnaire sources must not be empty.")
    return source + "\n\n# Appendix A: Draft Survey Instrument\n\n" + survey + "\n"


def validate_source(source: str) -> None:
    for number in range(1, 6):
        if len(re.findall(rf"^# Chapter {number}:", source, flags=re.M)) != 1:
            raise ValueError(f"Expected exactly one Chapter {number}.")
    if source.count("# Appendix A: Draft Survey Instrument") != 1:
        raise ValueError("Expected one survey appendix.")
    for field in ("A02", "A07b", "P01", "E01", "K01", "D01"):
        if not re.search(rf"^{field}\.", source, flags=re.M):
            raise ValueError(f"Required questionnaire item missing: {field}")
    if "no empirical conclusion" not in source.lower():
        raise ValueError("The report must disclose its lack of empirical conclusions.")
    if re.search(r"(?:C:[/\\]Users[/\\]|file://)", source, flags=re.I):
        raise ValueError("Machine-specific paths must not appear in the report.")


def render(source: str) -> str:
    try:
        import markdown
    except ImportError as exc:
        raise ValueError("Install the dependency with: python -m pip install -r requirements.txt") from exc
    import html

    # Source files contain research prose, not executable HTML. Escape raw tags.
    safe_source = source.replace("<", "&lt;").replace(">", "&gt;")
    md = markdown.Markdown(extensions=["tables", "toc", "sane_lists"],
                           extension_configs={"toc": {"toc_depth": "1-1"}})
    body = md.convert(safe_source)
    # Turn bare bibliographic URLs into clickable links without nesting links.
    parts = re.split(r"(<[^>]+>)", body)
    inside_link = False
    for i, part in enumerate(parts):
        if part.startswith("<a "):
            inside_link = True
        elif part == "</a>":
            inside_link = False
        elif not part.startswith("<") and not inside_link:
            parts[i] = re.sub(r"https://[^\s<]+", lambda m: '<a href="' + html.escape(m[0], quote=True) + '">' + m[0] + '</a>', part)
    body = "".join(parts).replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    title = html.escape("AI Adoption and Operational Efficiency — MBA Research Project")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><style>{CSS}</style></head><body>
<div class="shell"><nav aria-label="Report sections"><strong>MBA research project</strong>
<button type="button" onclick="window.print()">Print / Save as PDF</button>{md.toc}</nav>
<main><div class="badge"><strong>Research design report · Chennai IT-enabled services</strong><br>
Chapters 1–3 and the draft instrument are developed. No survey data have been collected; Chapters 4–5 document the evidence status rather than invented results.</div>
{body}<footer>Generated from the repository's report and questionnaire. Offline document: no analytics, uploads, or participant-data storage.</footer></main></div></body></html>"""


def build(output: Path) -> Path:
    source = load_sources()
    validate_source(source)
    page = render(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding="utf-8")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "outputs" / "MBA_Project_Report.html")
    args = parser.parse_args()
    try:
        path = build(args.output)
    except (ValueError, OSError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    print(f"Report built: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
