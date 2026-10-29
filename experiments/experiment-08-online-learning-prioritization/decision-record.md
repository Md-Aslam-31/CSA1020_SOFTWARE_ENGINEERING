# ClassSpring — MoSCoW and Kano Decision Record

**Context:** A first release must let learners join a course and access its teaching content. Impact and feasibility are qualitative planning judgments. Kano categories are unvalidated hypotheses that require learner feedback.

| Jira / ID | Capability | MoSCoW | Kano hypothesis | Learner impact / feasibility | Acceptance evidence | Depends on |
|---|---|---|---|---|---|---|
| [CLSPRG-1](https://sofenglab.atlassian.net/browse/CLSPRG-1) / CS-01 | Course enrollment and registration | Must | Basic | High / Medium | Learner enrolls in an open course and sees confirmation. | Account and course catalog |
| [CLSPRG-2](https://sofenglab.atlassian.net/browse/CLSPRG-2) / CS-02 | Video lecture streaming | Must | Basic | High / Medium | Enrolled learner starts a lecture and recovers from a paused connection. | CS-01, media hosting |
| [CLSPRG-3](https://sofenglab.atlassian.net/browse/CLSPRG-3) / CS-03 | Interactive quizzes and assignments | Should | Performance | High / Medium | Learner submits answers and sees a score or instructor feedback. | CS-01, CS-02 |
| [CLSPRG-4](https://sofenglab.atlassian.net/browse/CLSPRG-4) / CS-04 | Progress tracking dashboard | Should | Performance | Medium / Medium | Dashboard shows completed lectures and outstanding activities. | CS-02, CS-03 |
| [CLSPRG-5](https://sofenglab.atlassian.net/browse/CLSPRG-5) / CS-05 | Peer discussion forums | Could | Attractive | Medium / Medium | Learner posts and replies in a course discussion. | CS-01, moderation |
| [CLSPRG-6](https://sofenglab.atlassian.net/browse/CLSPRG-6) / CS-06 | Certificate generation | Could | Attractive | Medium / Medium | Eligible learner downloads a certificate after passing completion rules. | CS-03, CS-04 |

## Release rationale

Enrollment and reliable lecture access are the minimum learning path. Assessment and progress visibility follow because they depend on course activity and improve feedback. Discussion and certificates can wait until the course baseline and moderation/completion rules are defined.

MoSCoW defines scope while Kano expresses a satisfaction hypothesis. Basic enrollment and content access are expected prerequisites; quiz quality and progress clarity may improve satisfaction with better performance; discussion and certificates may delight some learners but are not prerequisites for course access. Validate these assumptions with learners before treating them as research findings.

All six live Jira issues remain To Do. The account contains planning requirements, not a deployed learning service.
