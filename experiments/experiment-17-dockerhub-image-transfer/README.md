# Experiment 17 — Push/pull Docker Hub image

## Aim

Build CampusConnect, log in, push a tagged image, pull and run that image.

## Tools Required

| Tool | Purpose |
| --- | --- |
| Docker Desktop and Docker CLI | Build, push, pull, run and inspect the same image tag |
| Docker Hub account | Store the image under the student's own namespace |
| PowerShell | Run the checked script and inspect exit codes |
| Browser | Check the website on the loopback URL after running the pulled image |

The script accepts the user's Docker Hub username as an argument. It never stores a password or access token; `docker login` prompts for the account's credential interactively.

## Quick access links

| What to open | Link |
| --- | --- |
| Original website source | [CampusConnect](website/index.html) · [Stylesheet](website/styles.css) |
| Build, push, pull and run script | [publish-pull.ps1](publish-pull.ps1) |
| Portfolio report | [This experiment](README.md) · [Portfolio index](../../README.md) |

## Algorithm

1. Build the Experiment 17 CampusConnect website from the local Dockerfile.
2. Authenticate interactively to Docker Hub under the user's own username.
3. Push the tagged image, then pull the same tag back to prove registry transfer.
4. Run the pulled image on port 8081 and inspect the page in a browser.
5. Stop the named container when the check is complete.

From this directory, use `./publish-pull.ps1 -DockerHubUser <your-dockerhub-username>`. The command intentionally leaves the credential prompt to Docker and does not put secrets in PowerShell history or source files.

## Output Screenshots

Reproducible files and commands are included. External execution is only reported when verified.

## Result

The original script and image source are included. Docker and Docker Hub credentials are unavailable in this authoring environment; the build, push/pull, registry URL and browser-on-container proof remain pending. No public image is claimed. After a successful run, record the exact username, immutable tag, registry page and command output in this report rather than assuming the push succeeded.
