# Run Tests from GitHub with Cloud Build

## Overview

Set up Cloud Build to automatically run tests whenever you push to GitHub. No local setup needed!

---

## One-Time Setup (5 Minutes)

### 1. Connect GitHub to Cloud Build

1. Go to: https://console.cloud.google.com/cloud-build/triggers
2. Click **"Connect Repository"**
3. Select **GitHub**
4. Authenticate with GitHub
5. Select your repository: `Chrysaliz333/lawstronaut-cuad`
6. Click **"Connect"**

### 2. Create Build Trigger

1. Click **"Create Trigger"**
2. Configure:
   - **Name**: `run-gemini-tests`
   - **Event**: Push to a branch
   - **Branch**: `^claude/.*` (or `^main$` for main branch)
   - **Configuration**: Cloud Build configuration file (yaml)
   - **Location**: `cloudbuild.yaml`
3. Click **"Create"**

### 3. Grant Permissions

```bash
# Get your project number
PROJECT_NUMBER=$(gcloud projects describe $(gcloud config get-value project) --format="value(projectNumber)")

# Grant Cloud Build access to Vertex AI
gcloud projects add-iam-policy-binding $(gcloud config get-value project) \
  --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  --role="roles/aiplatform.user"
```

### 4. Enable APIs

```bash
gcloud services enable cloudbuild.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services enable generativelanguage.googleapis.com
```

---

## How It Works

### Automatic Trigger

Every time you push to your GitHub branch:

1. ✅ Cloud Build detects the push
2. ✅ Clones your repo
3. ✅ Installs dependencies
4. ✅ Runs the tests
5. ✅ Saves results to Cloud Storage
6. ✅ Sends you a notification

### Manual Trigger

You can also trigger manually:

```bash
# Trigger from command line
gcloud builds submit --config=cloudbuild.yaml

# Or click "Run" in the Cloud Build console
```

---

## View Results

### In Cloud Console

1. Go to: https://console.cloud.google.com/cloud-build/builds
2. Click on your latest build
3. View logs and download artifacts

### Download Results

```bash
# List recent builds
gcloud builds list --limit=5

# Get build ID from above, then download artifacts
BUILD_ID="your-build-id-here"
gsutil cp gs://$(gcloud config get-value project)_cloudbuild/lawstronaut-results/gemini_vertex_results.json ./
```

### Get Notified

Set up notifications in Cloud Build:

1. Go to: https://console.cloud.google.com/cloud-build/settings/notifications
2. Add your email or Slack webhook
3. Get notified when builds complete

---

## Customize cloudbuild.yaml

### Run Specific Questions

Edit `cloudbuild.yaml`:

```yaml
# Change this line:
args: ['tests/test_gemini_vertex.py', '--questions=all', '--rate-limit=15']

# To test specific questions:
args: ['tests/test_gemini_vertex.py', '--questions=5A', '--rate-limit=15']
```

### Run on Schedule

Create a scheduled trigger:

1. Go to: https://console.cloud.google.com/cloudscheduler
2. Click **"Create Job"**
3. Configure:
   - **Name**: `daily-gemini-tests`
   - **Frequency**: `0 9 * * *` (9 AM daily)
   - **Target**: Pub/Sub
   - **Topic**: Create new topic `lawstronaut-trigger`
4. Update Cloud Build trigger to listen to this Pub/Sub topic

### Add Comparison with Perplexity

Add a step to `cloudbuild.yaml`:

```yaml
- name: 'python:3.11'
  entrypoint: 'python'
  args: ['scripts/compare_results.py', '--gemini', 'gemini_vertex_results.json', '--perplexity', 'perplexity_results.json']
```

---

## Cost

- **Cloud Build**: First 120 build-minutes/day are FREE
- **Each test run**: ~5 minutes = FREE (within free tier)
- **Storage**: Minimal (~1MB results) = FREE
- **Vertex AI calls**: ~$0.22 per 6 tests

---

## Advantages

✅ **Zero local setup** - runs entirely in the cloud
✅ **Automatic** - triggers on every push
✅ **Reproducible** - same environment every time
✅ **Team access** - anyone with access to GCP can view results
✅ **Audit trail** - all runs logged in Cloud Build
✅ **Version controlled** - cloudbuild.yaml in your repo

---

## Troubleshooting

### Build fails with "Permission denied"

```bash
# Grant more permissions
PROJECT_NUMBER=$(gcloud projects describe $(gcloud config get-value project) --format="value(projectNumber)")

gcloud projects add-iam-policy-binding $(gcloud config get-value project) \
  --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  --role="roles/aiplatform.admin"
```

### Can't find cloudbuild.yaml

Make sure `cloudbuild.yaml` is in your repo root and committed to GitHub.

### Tests timeout

Increase timeout in `cloudbuild.yaml`:

```yaml
timeout: '3600s'  # 1 hour
```

---

## Next Steps

1. ✅ Push `cloudbuild.yaml` to your repo
2. ✅ Set up GitHub connection in Cloud Build
3. ✅ Create trigger
4. ✅ Push a commit to trigger your first build
5. ✅ View results in Cloud Console
6. ✅ Download and compare with Perplexity results

---

## Example Workflow

```bash
# Make a change to test questions
git add tests/test_gemini_vertex.py

# Commit and push
git commit -m "Update test questions"
git push

# Cloud Build automatically:
# 1. Detects push
# 2. Runs tests
# 3. Saves results
# 4. Notifies you

# Download results
gsutil cp gs://$(gcloud config get-value project)_cloudbuild/lawstronaut-results/gemini_vertex_results.json ./

# Compare with Perplexity
# Document findings in PERPLEXITY_COMPARISON.md
```

**It's that simple!** 🚀
