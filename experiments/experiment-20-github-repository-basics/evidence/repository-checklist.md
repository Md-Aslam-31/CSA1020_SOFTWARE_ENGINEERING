# Repository setup verification checklist

Use this checklist after creating a repository under the intended account. Do not paste private credentials or access tokens into this record.

- [x] Target repository owner is `Md-Aslam-31`.
- [x] Target repository URL is `https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING`.
- [x] Portfolio README and experiment folders are published.
- [x] Local `origin` points to the target repository.
- [x] Changes from this task were pushed to `main`.
- [ ] Separate Lab Journal repository was created; this optional example repository was not created in this run.

To recheck the remote without exposing credentials:

```powershell
git remote get-url origin
git ls-remote origin refs/heads/main
git log -1 --oneline
git status --short
```
