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
| [CLSPRG-7](https://sofenglab.atlassian.net/browse/CLSPRG-7) / CS-07 | Bookmark lectures and save private notes | Could | Performance | Medium / High | Enrolled learner saves a bookmark and private note, then retrieves them later. | CS-01, CS-02 |
| [CLSPRG-8](https://sofenglab.atlassian.net/browse/CLSPRG-8) / CS-08 | Celebrate course milestones | Could | Attractive | Low / Medium | Learner receives an accessible acknowledgement after a defined milestone. | CS-04, motion preferences |
| [CLSPRG-9](https://sofenglab.atlassian.net/browse/CLSPRG-9) / CS-09 | Ask a course assistant for study guidance | Won't this release | Attractive | Medium / Low | Assistant responses use approved material and pass accuracy/privacy review. | CS-01, content approval, safety evaluation |

## Release rationale

Enrollment and reliable lecture access are the minimum learning path. Assessment and progress visibility follow because they depend on course activity and improve feedback. Discussion and certificates can wait until the course baseline and moderation/completion rules are defined.

MoSCoW defines scope while Kano expresses a satisfaction hypothesis. Basic enrollment and content access are expected prerequisites; quiz quality and progress clarity may improve satisfaction with better performance; discussion and certificates may delight some learners but are not prerequisites for course access. Validate these assumptions with learners before treating them as research findings.

All nine Jira issues are included in the requirements register. The report's progress snapshot is a planning baseline, not proof of deployed learning functionality. Confirm issue keys and status in the live board before using the sprint as current delivery evidence.

## Kano validation questions

Ask both questions using the same response options: **I like it**, **It must be that way**, **I am neutral**, **I can live with it**, **I dislike it**. Use a learner sample and record the answers before assigning a validated category.

| Capability | Functional question | Dysfunctional question |
|---|---|---|
| Course enrollment | How would you feel if you could enroll online in an open course and see confirmation? | How would you feel if online enrollment and confirmation were unavailable? |
| Lecture streaming | How would you feel if you could stream course lectures and resume after a pause? | How would you feel if lecture streaming and resume were unavailable? |
| Quizzes and assignments | How would you feel if quizzes returned scores or instructor feedback? | How would you feel if quizzes gave no score or feedback? |
| Progress dashboard | How would you feel if a dashboard showed completed lectures and outstanding work? | How would you feel if you had to track course progress yourself? |
| Discussion forum | How would you feel if you could post and reply to classmates in the course? | How would you feel if course discussions were unavailable? |
| Certificates | How would you feel if you could download a certificate after meeting course criteria? | How would you feel if the course provided no completion certificate? |
| Bookmarks and notes | How would you feel if you could save private notes and bookmarks beside a lecture? | How would you feel if saved notes and bookmarks were unavailable? |
| Milestone acknowledgement | How would you feel if the platform acknowledged course milestones accessibly? | How would you feel if the platform gave no milestone acknowledgement? |
| Study assistant | How would you feel if a course assistant answered from approved material with clear limits? | How would you feel if this course assistant were unavailable? |

These are proposed survey prompts only. No learner survey has been run.
