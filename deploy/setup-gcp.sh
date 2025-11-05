#!/bin/bash
# Setup script for Google Cloud Build and Vertex AI access

set -e

PROJECT_ID="alien-device-432011-q6"
REGION="us-central1"
SERVICE_ACCOUNT="lawstronaut-cuad@${PROJECT_ID}.iam.gserviceaccount.com"

echo "Setting up Google Cloud project: ${PROJECT_ID}"

# Set the project
gcloud config set project ${PROJECT_ID}

# Enable required APIs
echo "Enabling required APIs..."
gcloud services enable \
    cloudbuild.googleapis.com \
    run.googleapis.com \
    aiplatform.googleapis.com \
    containerregistry.googleapis.com \
    secretmanager.googleapis.com \
    iam.googleapis.com

# Create service account if it doesn't exist
echo "Creating service account..."
gcloud iam service-accounts create lawstronaut-cuad \
    --display-name="Lawstronaut CUAD Service Account" \
    --description="Service account for Lawstronaut CUAD testing with Vertex AI" \
    2>/dev/null || echo "Service account already exists"

# Grant necessary permissions to the service account
echo "Granting permissions..."
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="roles/aiplatform.user" \
    --condition=None

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="roles/logging.logWriter" \
    --condition=None

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${SERVICE_ACCOUNT}" \
    --role="roles/secretmanager.secretAccessor" \
    --condition=None

# Grant Cloud Build service account permissions
BUILD_SA="${PROJECT_ID}@cloudbuild.gserviceaccount.com"
echo "Granting Cloud Build permissions..."
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${BUILD_SA}" \
    --role="roles/run.admin" \
    --condition=None

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:${BUILD_SA}" \
    --role="roles/iam.serviceAccountUser" \
    --condition=None

# Create secrets for API keys
echo "Creating secrets..."
echo -n "${OPENAI_API_KEY}" | gcloud secrets create OPENAI_API_KEY \
    --data-file=- \
    --replication-policy="automatic" \
    2>/dev/null || echo "OPENAI_API_KEY secret already exists"

echo -n "${ANTHROPIC_API_KEY}" | gcloud secrets create ANTHROPIC_API_KEY \
    --data-file=- \
    --replication-policy="automatic" \
    2>/dev/null || echo "ANTHROPIC_API_KEY secret already exists"

echo -n "${PERPLEXITY_API_KEY}" | gcloud secrets create PERPLEXITY_API_KEY \
    --data-file=- \
    --replication-policy="automatic" \
    2>/dev/null || echo "PERPLEXITY_API_KEY secret already exists"

echo -n "${GEMINI_API_KEY}" | gcloud secrets create GEMINI_API_KEY \
    --data-file=- \
    --replication-policy="automatic" \
    2>/dev/null || echo "GEMINI_API_KEY secret already exists"

# Grant service account access to secrets
echo "Granting secret access..."
for SECRET in OPENAI_API_KEY ANTHROPIC_API_KEY PERPLEXITY_API_KEY GEMINI_API_KEY; do
    gcloud secrets add-iam-policy-binding ${SECRET} \
        --member="serviceAccount:${SERVICE_ACCOUNT}" \
        --role="roles/secretmanager.secretAccessor" \
        2>/dev/null || true
done

echo ""
echo "✓ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Submit build: gcloud builds submit --config cloudbuild.yaml"
echo "2. Or set up GitHub trigger: gcloud builds triggers create github ..."
echo "3. View builds: https://console.cloud.google.com/cloud-build/builds?project=${PROJECT_ID}"
echo ""
