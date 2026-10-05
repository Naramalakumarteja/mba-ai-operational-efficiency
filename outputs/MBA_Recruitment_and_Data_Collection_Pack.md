# Recruitment and data-collection pack

**1 October 2026 | Planning draft | No invitations sent or responses collected**

Use with questionnaire v0.3 and the expert-review/pilot kit. This document prepares recruitment; it does not establish institutional permission, participant consent, or survey validation. Replace bracketed fields with actual information before use.

## 1. Access assessment

Start by identifying professional contacts, alumni contacts, and organisational gatekeepers who may help establish access to eligible operational units. Count reachable units separately from people: several managers in one team do not create several independent unit observations.

Eligible units perform customer support, transaction processing, or back-office service delivery as IT-enabled business services within Chennai city. The unit must have operated throughout the preceding six months. Respondents must be adult managers, supervisors, or team leads with direct responsibility and at least six months in that unit. AI use is not required.

Do not expand the geographic boundary simply to meet a numerical target. If the accessible population requires a broader boundary, revise the scope and document the change before recruitment. Clarify what address/location rule defines Chennai city during access screening; do not use a respondent's home address as the unit location.

### Access log template

Create one row per potential organisation, without storing personal contact details in the analytical dataset.

| Organisation code | Contact route | Eligible units estimated | Eligible leaders estimated | Permission requirements | Access status | Invitation denominator known? | Notes |
|---|---|---|---|---|---|---|---|
| To be entered | | | | | | | |

Access status options: not assessed; contact identified; permission pending; accessible; declined; out of scope. Blank estimates mean unknown, not zero. Do not enter fictitious organisations or assume permission from a contact's interest.

### Unit-level recruitment log

| Organisation code | Unit code | Activity | Location confirmed | Eligibility confirmed | Invitation date | Pilot/main phase | Submission status | Duplicate flag | Final disposition |
|---|---|---|---|---|---|---|---|---|---|
| To be entered | | | | | | | | | |

Keep contact information and code linkages in a separate restricted file. Where an open referral route makes the invitation denominator unknowable, state that a conventional response rate cannot be calculated.

## 2. Draft organisation-access request

**Subject: Access enquiry for MBA research on AI use and service operations**

Dear [name/role],

I am [researcher name], an MBA student at [institution]. I am preparing a study titled “Artificial Intelligence Adoption and Operational Efficiency: An Empirical Study of Productivity, Cost Optimization and Managerial Decision-Making.”

The proposed study covers managers, supervisors, and team leads responsible for customer support, transaction processing, or back-office IT-enabled service operations in Chennai. Units using AI and units not using AI are both relevant. Each participant would describe one operational unit; company-wide financial records and client information are not requested.

At this stage, I would like to understand whether eligible units could potentially participate and what organisational requirements would apply. Main survey collection will follow questionnaire review, piloting, and applicable institutional requirements.

Could you indicate the approximate number of eligible units, an appropriate contact route, and any permission requirements? Participation by individual respondents would be voluntary, and findings would be reported in aggregate.

Thank you,
[researcher name]
[institution]
[actual contact details]

This is an unsent draft. Organisational access does not replace individual consent.

## 3. Draft participant invitation — use after release

**Subject: Invitation to MBA research survey on AI use and service operations**

Dear [name/role],

I invite you to participate in an MBA research survey about AI use and operational performance perceptions in Chennai IT-enabled service units. You may participate whether or not your unit uses AI.

The survey is intended for adults who directly supervise customer support, transaction processing, or back-office service operations and have worked in the selected unit for at least six months. Please report on only one unit, and do not submit another response if that same unit has already participated.

Participation is voluntary. You may skip questions or leave before submitting. Please do not provide client details or confidential records. The participant information at the survey link explains data handling and the applicable withdrawal arrangements.

Survey: [released survey link]
Estimated duration: [duration established during pilot]
Researcher/contact: [actual details]

Thank you,
[researcher name and institution]

Do not circulate this invitation until consent details, permissions, instrument checks, and collection rules are complete. No claim of anonymity, approval, or completion time should be added unless established.

## 4. Pilot invitation adaptation

Use the participant invitation with this replacement opening: “I invite you to help test a draft MBA research questionnaire for clarity and usability. These pilot responses will be kept separate from the main study. Feedback on confusing or unanswerable questions is especially useful.” Do not promise a validated instrument or treat pilot participants as main-study observations.

## 5. Sample decision worksheet

Complete the following before setting a final recruitment target:

| Decision | Entry required | Current status |
|---|---|---|
| Accessible organisations and units | Actual access-log totals | Unknown |
| Available collection window | Dates based on submission deadline | Unknown |
| Primary association | Frequency versus each supported outcome domain | Proposed |
| Smallest useful association | Practical rationale, not a borrowed deployment effect | Pending |
| Planned statistical power/precision | Justification and assumptions | Pending |
| Expected missingness | Pilot-informed operational estimate | Pending |
| Organisation dependence | Actual number and concentration of organisations | Pending |
| Final invitation ceiling and stopping rule | Feasibility and analysis-specific justification | Pending |

Do not convert the earlier illustrative 120 independent observations into a fixed requirement. Ordinal ties, organisation dependence, and domain-specific missingness can change analysis requirements. Do not rely on a simple population-size formula to justify a purposive sample.

## 6. Data-handling workflow

1. Complete institutional requirements and actual consent details.
2. Assign organisation and unit codes; keep the linkage separate.
3. Pilot the real survey routes and export format; preserve pilot data separately.
4. Freeze the questionnaire and analysis rules with version/date.
5. Record recruitment events without inspecting association p-values as a stopping rule.
6. Preserve the original main-study export unchanged.
7. Create a cleaned analytical copy and an exclusion/change log.
8. Analyse only eligible records using analysis-specific valid-response counts.
9. Remove identifying open-text details and suppress revealing small cells in reports.
10. Apply the actual retention/deletion schedule established by institutional requirements.

## 7. Minimum analytical record structure

One row represents one operational unit, not one task or one manager rating. Field names align with questionnaire IDs. Include: record_id; phase; questionnaire_version; organisation_code; unit_code; eligibility_status; exclusion_reason; submitted_at; S01–S07 including S03b; B01–B03 and B06; A01–A08 including A07b; P01–P03; E01–E03; K01–K03; D01–D03; X01–X03; and data-quality flags.

B04 and B05 correspond to organisation_code and unit_code; avoid creating inconsistent duplicate identifiers. Store a missing-reason field where necessary to distinguish skipped by design, not known, not applicable, declined, and technical omission. Numeric analytical fields remain empty/missing for these reasons, never artificial values such as 99 included in averages.

Derived fields may include productivity_mean, process_mean, cost_mean, and decision_mean only when domain scoring is supported. No overall efficiency total or summed adoption scale is authorised. Keep raw answers alongside any derived fields.

## 8. Readiness gate

The current status is **prepared for access assessment and document review, not ready for main survey launch**. The next activities require actual institution details, review participation, and eligible respondent access. No messages have been sent on the user's behalf.
