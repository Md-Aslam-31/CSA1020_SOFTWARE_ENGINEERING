# Publish the experiment catalog

The original catalog and static prototypes are prepared for GitHub Pages. The repository currently has no Pages site configured, so the Pages URL is not live yet.

## One-time account setup

1. Open the [repository Settings](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/settings/pages) while signed in as `Md-Aslam-31`.
2. Under **Build and deployment**, set **Source** to **GitHub Actions** and save.
3. Open [Actions](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/workflows/deploy-static-portfolio.yml), select **Deploy experiment portfolio to GitHub Pages**, choose `main`, and run the workflow.
4. After the deploy job succeeds, open `https://md-aslam-31.github.io/CSA1020_SOFTWARE_ENGINEERING/`.

The workflow publishes `index.html` and the original `experiments/` directory. This includes static front-end previews, reports, screenshots, and source artifacts. The workflow does not run Flask, PostgreSQL, Docker, Jenkins, or Kubernetes backends; pages labeled as local/API previews still need their documented local runtime. Atlassian and Figma links open their own account-hosted services.

The workflow is manual so it will not fail on every push before Pages is enabled. Once the site is active, run it again after portfolio changes to refresh the hosted site.
