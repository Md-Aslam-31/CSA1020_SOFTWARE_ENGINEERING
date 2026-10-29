# Experiment 11 — Static website in Docker with Nginx

## Aim

Create an original campus-support landing page, package it as a static Nginx image, run it as a container, and inspect it in a browser.

## Files

- `website/index.html` and `website/styles.css`: responsive CampusConnect page.
- `nginx.conf`: serves the static site, provides `/healthz`, and returns 404 for missing paths.
- `Dockerfile` and `.dockerignore`: package only the site and Nginx configuration, expose port 80, and define a container health check.

## Procedure

From this directory run:

```powershell
docker build -t campusconnect-static:1.0 .
docker run --rm -d --name campusconnect -p 8080:80 campusconnect-static:1.0
```

Open [http://localhost:8080](http://localhost:8080), inspect the responsive layout, then stop it with `docker stop campusconnect`.

## Evidence and result

The source page and a real local-browser preview are included below. Docker is not installed in the authoring environment, so the image build, Nginx health check, and Docker-served browser evidence remain pending; the preview is not presented as container proof.

![CampusConnect local browser preview](screenshots/campusconnect-browser-preview.png)
