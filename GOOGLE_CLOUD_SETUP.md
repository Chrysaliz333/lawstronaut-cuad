# Google Cloud Setup for Gemini with Search Grounding

## Overview

Google Search grounding is **built into Vertex AI** - you don't need a separate Search API key. You just need to enable the right APIs in your Google Cloud project.

---

## Step-by-Step Setup

### 1. Create Google Cloud Project (if you don't have one)

1. Go to: https://console.cloud.google.com/
2. Click **"Select a project"** (top bar)
3. Click **"New Project"**
4. Enter project name (e.g., "lawstronaut-testing")
5. Click **"Create"**
6. **Copy your Project ID** (not the name - the ID looks like `lawstronaut-testing-123456`)

---

### 2. Enable Required APIs

Google Search grounding requires these APIs to be enabled:

#### **Option A: Enable via Console (Easiest)**

Click these links (they'll auto-select your project):

1. **Vertex AI API**: https://console.cloud.google.com/apis/library/aiplatform.googleapis.com
   - Click **"Enable"**

2. **Generative Language API**: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com
   - Click **"Enable"**

3. **Check if enabled**: https://console.cloud.google.com/apis/dashboard
   - You should see "Vertex AI API" and "Generative Language API" in the list

#### **Option B: Enable via Command Line**

```bash
# Set your project
gcloud config set project YOUR-PROJECT-ID

# Enable required APIs
gcloud services enable aiplatform.googleapis.com
gcloud services enable generativelanguage.googleapis.com

# Verify enabled
gcloud services list --enabled | grep -E "(aiplatform|generativelanguage)"
```

---

### 3. Set Up Billing

**Important:** Vertex AI requires billing enabled (but you get free credits).

1. Go to: https://console.cloud.google.com/billing
2. Link a billing account (requires credit card)
3. **Free tier:** $300 in credits for 90 days for new users

**Cost for this project:** ~$0.22 for all 6 tests (very cheap!)

---

### 4. Install Google Cloud CLI (gcloud)

#### **Check if already installed:**
```bash
gcloud --version
```

#### **If not installed:**

**Linux/macOS:**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

**Or use package manager:**
```bash
# Ubuntu/Debian
sudo apt-get install google-cloud-cli

# macOS
brew install google-cloud-sdk
```

**Windows:**
Download from: https://cloud.google.com/sdk/docs/install

---

### 5. Authenticate

```bash
# Initialize gcloud (sets project, region, etc.)
gcloud init

# Or set project manually
gcloud config set project YOUR-PROJECT-ID

# Authenticate for application default credentials
gcloud auth application-default login
```

This opens a browser and asks you to log in with your Google account.

---

### 6. Configure Your Project

Edit `.env` file in project root:

```bash
GOOGLE_CLOUD_PROJECT=your-project-id-here
GOOGLE_CLOUD_LOCATION=us-central1
```

**Replace** `your-project-id-here` with your actual project ID.

---

### 7. Test Your Setup

```bash
# Quick test to see if authentication works
python -c "from google import genai; print('✓ google-genai installed')"

# Test Vertex AI connection (run after auth)
python tests/test_gemini_vertex.py --questions=5A --rate-limit=15
```

---

## Google Search Grounding - How It Works

### **Automatic Grounding**

In `test_gemini_vertex.py`, search grounding is enabled with this code:

```python
from google.genai.types import GoogleSearch, Tool

# Create Google Search tool
search_tool = Tool(google_search=GoogleSearch())

# Use it in generation
config = GenerateContentConfig(
    tools=[search_tool],  # This enables search grounding!
    temperature=0.2,
)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp",
    contents=prompt,
    config=config
)
```

**That's it!** No API key needed - it's built into Vertex AI.

### **What Search Grounding Does**

- Gemini automatically searches Google when it needs current information
- Returns grounding metadata showing what it searched for
- Cites sources with URLs
- Accesses post-cutoff information (2024 regulations)

### **Cost**

- **$35 per 1,000 queries**
- Each question typically = 1 search query
- 6 questions ≈ $0.21

---

## Troubleshooting

### Error: "Could not automatically determine credentials"

**Fix:**
```bash
gcloud auth application-default login
```

### Error: "Permission denied" or "403"

**Fix:** Make sure APIs are enabled:
```bash
gcloud services enable aiplatform.googleapis.com
gcloud services enable generativelanguage.googleapis.com
```

### Error: "Billing not enabled"

**Fix:** Enable billing at: https://console.cloud.google.com/billing

### Error: "GOOGLE_CLOUD_PROJECT not set"

**Fix:** Edit `.env` file with your project ID

### Error: "The model gemini-2.0-flash-exp is not found"

**Fix:** Make sure you're using Vertex AI (not the free API). The model name might change - check: https://console.cloud.google.com/vertex-ai/publishers/google/model-garden

---

## Alternative: Use Free Gemini API (No Search Grounding)

If you don't want to set up Vertex AI, you can use the free Gemini API:

1. Get API key: https://aistudio.google.com/app/apikey
2. Edit `test_gemini_vertex.py` to use API key instead of Vertex AI

**But:** The free API **does NOT have Google Search grounding**. It will miss 2024 regulations.

---

## Verify Search Grounding Works

After setup, run Q5A (Non-Compete test):

```bash
python tests/test_gemini_vertex.py --questions=5A --rate-limit=15
```

**Check the output for:**
- ✅ "FTC" or "16 CFR § 910" mentioned
- ✅ "August 2024" or "finalized"
- ✅ Grounding metadata showing search queries

If you see these, **search grounding is working!** 🎉

---

## Summary

1. ✅ Create Google Cloud project
2. ✅ Enable Vertex AI API
3. ✅ Enable billing (get $300 free credits)
4. ✅ Install gcloud CLI
5. ✅ Run `gcloud auth application-default login`
6. ✅ Edit `.env` with your project ID
7. ✅ Run tests!

**Search grounding is automatic** - no separate API key needed!
