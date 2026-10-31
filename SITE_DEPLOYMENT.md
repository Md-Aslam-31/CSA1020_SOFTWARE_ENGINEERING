# Publish the experiment catalog

The original catalog and static prototypes are published on GitHub Pages at [md-aslam-31.github.io/CSA1020_SOFTWARE_ENGINEERING](https://md-aslam-31.github.io/CSA1020_SOFTWARE_ENGINEERING/). The repository's Pages source is configured to use GitHub Actions.

## One-time account setup

1. Open the [live portfolio](https://md-aslam-31.github.io/CSA1020_SOFTWARE_ENGINEERING/).
2. After each push to `main`, check the [Pages deployment workflow](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/workflows/deploy-static-portfolio.yml) for a successful run. A manual rerun is available from the Actions page.

The workflow publishes `index.html` and the original `experiments/` directory. This includes static front-end previews, reports, screenshots, and source artifacts. The workflow does not run Flask, PostgreSQL, Docker, Jenkins, or Kubernetes backends; pages labeled as local/API previews still need their documented local runtime. Atlassian and Figma links open their own account-hosted services.

The first successful deployment is recorded at [GitHub Actions run 41171754112](https://github.com/Md-Aslam-31/CSA1020_SOFTWARE_ENGINEERING/actions/runs/41171754112). The workflow now republishes on pushes to `main` and also supports manual runs.
