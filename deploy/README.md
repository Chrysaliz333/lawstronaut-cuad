# Deployment Configuration

This directory contains deployment configurations for running Lawstronaut on Google Cloud Platform.

## Files

- **Dockerfile** - Container image definition
- **cloudbuild.yaml** - Google Cloud Build configuration
- **setup-gcp.sh** - GCP setup script

## Status

⚠️ **These deployment files are incomplete/untested.**

The primary focus is on local testing with Vertex AI. Cloud deployment is a future enhancement.

## Setup (If Deploying to GCP)

1. Set up Google Cloud project
2. Enable required APIs (Vertex AI, Cloud Build, etc.)
3. Configure authentication
4. Run setup-gcp.sh
5. Trigger build with cloudbuild.yaml

For now, use Vertex AI Studio directly for testing: https://console.cloud.google.com/vertex-ai/studio
