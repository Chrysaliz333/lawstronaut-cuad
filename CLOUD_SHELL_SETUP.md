# Run Tests in Google Cloud Shell

## Why Cloud Shell?

- ✅ No local setup needed
- ✅ `gcloud` already installed and authenticated
- ✅ Free (5GB persistent storage)
- ✅ Runs in your browser
- ✅ Already connected to your Google Cloud project

---

## Quick Start (2 Minutes)

### 1. Open Cloud Shell

Go to: https://console.cloud.google.com/

Click the **Cloud Shell icon** (>_) in the top-right corner.

A terminal opens at the bottom of your screen.

### 2. Clone Your Repo

```bash
git clone https://github.com/Chrysaliz333/lawstronaut-cuad.git
cd lawstronaut-cuad
```

### 3. Set Your Project

```bash
# Set your project ID
gcloud config set project YOUR-PROJECT-ID

# Verify it's set
gcloud config get-value project
```

### 4. Create .env File

```bash
# Get your project ID automatically
PROJECT_ID=$(gcloud config get-value project)

# Create .env file
cat > .env << EOF
GOOGLE_CLOUD_PROJECT=${PROJECT_ID}
GOOGLE_CLOUD_LOCATION=us-central1
EOF

# Verify
cat .env
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Tests!

```bash
# Single test
python tests/test_gemini_vertex.py --questions=5A --rate-limit=15

# All tests
python tests/test_gemini_vertex.py --questions=all --rate-limit=15
```

### 7. Download Results

```bash
# View results in terminal
cat gemini_vertex_results.json | python -m json.tool | less

# Or download to your computer
# Click the 3-dot menu in Cloud Shell > "Download file"
# Enter: gemini_vertex_results.json
```

---

## Advantages of Cloud Shell

✅ **Already authenticated** - no `gcloud auth` needed
✅ **No local Python setup** - Python 3.11 pre-installed
✅ **No gcloud install** - already there
✅ **Free** - included with Google Cloud
✅ **Fast network** - direct connection to Vertex AI
✅ **Persistent storage** - your files stay between sessions

---

## Enable Required APIs (First Time)

If you haven't enabled the APIs yet:

```bash
# Enable Vertex AI
gcloud services enable aiplatform.googleapis.com

# Enable Generative Language API
gcloud services enable generativelanguage.googleapis.com

# Verify
gcloud services list --enabled | grep -E "(aiplatform|generativelanguage)"
```

---

## Tips

### Run in Background

```bash
# Run tests and log output
nohup python tests/test_gemini_vertex.py --questions=all --rate-limit=15 > test_output.log 2>&1 &

# Check progress
tail -f test_output.log

# Check if still running
ps aux | grep test_gemini
```

### Download Results to Local Machine

**Option A: Using Cloud Shell Download**
1. Click 3-dot menu in Cloud Shell
2. Select "Download file"
3. Enter: `gemini_vertex_results.json`

**Option B: Using gcloud command (from local)**
```bash
# From your local machine
gcloud cloud-shell scp cloudshell:~/lawstronaut-cuad/gemini_vertex_results.json ./
```

**Option C: Push to GitHub**
```bash
# In Cloud Shell
git add gemini_vertex_results.json
git commit -m "Add Gemini test results"
git push
```

### Edit Files in Cloud Shell

Cloud Shell has a built-in code editor:

```bash
# Open editor
cloudshell edit .env

# Or use nano
nano .env
```

---

## Troubleshooting

### "Permission denied" when installing packages

```bash
# Use --user flag
pip install --user -r requirements.txt
```

### Cloud Shell times out

Cloud Shell sessions timeout after 20 minutes of inactivity. Your files persist, just reconnect and continue.

### Can't see output

```bash
# Add verbose output
python tests/test_gemini_vertex.py --questions=5A --rate-limit=15 2>&1 | tee output.log
```

---

## Cost

**Cloud Shell is FREE!**
- Included with every Google Cloud account
- No additional charges
- You only pay for the Vertex AI API calls (~$0.22 for 6 tests)

---

## Next Steps

After running tests in Cloud Shell:

1. Download `gemini_vertex_results.json`
2. Compare with your Perplexity results
3. Document findings in `PERPLEXITY_COMPARISON.md`
4. Push results to GitHub
