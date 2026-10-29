# Experiment 05 — Library Requirements with MoSCoW

## Aim

Classify ten original library-system requirements using MoSCoW, explain the user impact and delivery feasibility, and make the release trade-offs visible.

## Method

The workbook scores each requirement for user impact and feasibility, then records a MoSCoW decision and its rationale. The scenario covers borrower discovery and circulation, librarian desk work, reporting, and optional personalization. The classification is a reasoned planning proposal, not the result of a stakeholder survey.

## Prioritization result

| MoSCoW | Count | Release decision |
|---|---:|---|
| Must | 4 | Catalogue search, availability and shelf location, borrowing/renewal with due dates, and librarian check-in/check-out establish the minimum usable service. |
| Should | 3 | Email reminders, holds, and CSV circulation export add value, with manual processes available as interim workarounds. |
| Could | 2 | Reading history/personal lists and barcode scanning are useful enhancements, but can be deferred if capacity or device availability is limited. |
| Won’t this release | 1 | Personalized recommendations are deferred until consent, data governance, and recommendation quality can be addressed. |

## Impact, feasibility, time, and resource considerations

High-impact Must items directly enable finding a book and completing circulation. Their feasibility varies: search, availability, and basic desk transactions use standard catalogue and role data; borrowing/renewal has medium feasibility because loan rules and account states must be agreed. Holds and reminders are valuable, but require queue, notification, and failure-handling rules. The low-feasibility recommendation feature depends on trustworthy history data and privacy choices, so it is not a release dependency.

The first release should reserve librarian and backend capacity for circulation rules, account/loan state, and catalogue correctness, with frontend effort for search and availability. Should items can follow after a working circulation baseline; barcode scanning also needs compatible devices and integration time. No budget amount, team size, vendor quote, or measured duration was supplied, so this analysis does not invent cost figures. For budget control, defer recommendation work and treat scanner hardware, email delivery, and reporting as explicit resource decisions during estimation.

## Output and evidence

[Download the original Library MoSCoW workbook](Library_MoSCoW.xlsx). It contains the ten requirement records, rationale, and formula-based summary (4 Must, 3 Should, 2 Could, 1 Won’t this release).

![Workbook preview of requirement classifications and summary](workbook-preview.png)

The image is a local workbook preview. The workbook remains the editable source artifact; category totals are planning counts, not project progress.

## Result

Ten requirements have been classified with explicit impact, feasibility, and rationale. The release baseline protects core circulation and discovery, provides a clear follow-up path for useful enhancements, and defers a low-feasibility, privacy-sensitive feature until its prerequisites are understood.
