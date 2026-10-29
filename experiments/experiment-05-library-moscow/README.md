# Experiment 05 — Library requirements with MoSCoW

## Aim

Prioritize the ten library-system features listed in the lab PDF, with explicit impact, feasibility, rationale, effort, cost, and release assumptions.

## Tools Required

- Microsoft Excel or compatible spreadsheet software.
- MoSCoW decision rules and the ten features from the lab PDF.
- Filter, formula, validation, and chart/summary support in the workbook.

## Quick access links

| What to open | Link |
| --- | --- |
| Editable workbook | [Library_MoSCoW.xlsx](Library_MoSCoW.xlsx) |
| Screenshots | [Priority matrix](workbook-priority-matrix.png) · [Summary and assumptions](workbook-summary-assumptions.png) |
| Portfolio index | [All experiments](../../README.md) |

## Algorithm

1. Extract and preserve the ten library features from the PDF.
2. Assess user impact and delivery feasibility for each feature.
3. Assign a MoSCoW category with a short rationale and define the first-release boundary.
4. Estimate effort and labor cost using the assumptions recorded in the workbook.
5. Review counts, totals, formulas and filters; retain the workbook as the editable source of truth.

## Prioritization result

| MoSCoW | Count | Release decision |
|---|---:|---|
| Must | 3 | Search books by title/author, reserve books online, and provide a librarian dashboard. |
| Should | 3 | Monthly admin reports, overdue email notifications, and multilingual support. |
| Could | 3 | QR-code borrowing/return, book reviews/ratings, and a mobile app. |
| Won’t this release | 1 | A chatbot is deferred until its support content, privacy boundaries, and answer quality can be validated. |

High-impact Must items enable discovery, access, and circulation oversight. Reporting and overdue email require reliable transaction history, scheduling, and delivery handling. QR and mobile depend on device/browser compatibility; reviews need moderation; multilingual support requires translated, reviewed interface text. Chatbot work is deferred until approved content and quality controls exist.

## Planning assumptions

The workbook assumes an eight-week first release, one product owner, one librarian, two engineers, part-time QA, existing catalogue/circulation exports, and ₹1,500 per person-day. The estimate is 56 person-days and ₹84,000 labor, excluding hosting, hardware, and translation services. It is a planning scenario, not an approved quote.

## Evidence

[Editable MoSCoW workbook](Library_MoSCoW.xlsx), with ten PDF-matched requirements, formulas, a summary, assumption block, filter, frozen headings, dropdown validation, and priority formatting.

![Requirement matrix](workbook-priority-matrix.png)

![MoSCoW summary and assumptions](workbook-summary-assumptions.png)

The images are workbook previews; the workbook is the editable source.

## Result

The workbook classifies all ten features as 3 Must, 3 Should, 3 Could, and 1 Won't this release. It records a planning estimate of 56 person-days and ₹84,000 labor under the stated assumptions; hosting, hardware, and translation are excluded. This is a prioritization exercise, not an approved budget.
