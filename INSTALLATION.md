# 📦 Installation Guide

Complete step-by-step installation instructions for the Supply Chain Intelligence System.

---

## 🖥️ System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.15+, or Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB (8GB recommended)
- **Disk Space**: 2GB free
- **Internet**: Required for initial model download only

### Recommended Setup
- **RAM**: 8GB+
- **Python**: 3.10+
- **Disk Space**: 5GB free

---

## 🚀 Quick Installation

### Option 1: Using pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/supply-chain-intelligence.git
cd supply-chain-intelligence

# Install dependencies
pip install -r requirements.txt

# Run the demo
python supply_chain_intelligence.py
```

### Option 2: Using conda

```bash
# Clone repository
git clone https://github.com/yourusername/supply-chain-intelligence.git
cd supply-chain-intelligence

# Create conda environment
conda create -n supply-chain python=3.10
conda activate supply-chain

# Install dependencies
pip install -r requirements.txt

# Run
python supply_chain_intelligence.py
```

---

## 📝 Detailed Installation Steps

### Step 1: Install Python

**Check if Python is installed:**
```bash
python --version
```

If not installed:

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

**macOS:**
```bash
brew install python@3.10
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.10 python3-pip
```

### Step 2: Clone Repository

```bash
# Using HTTPS
git clone https://github.com/yourusername/supply-chain-intelligence.git

# OR using SSH
git clone git@github.com:yourusername/supply-chain-intelligence.git

# Navigate to directory
cd supply-chain-intelligence
```

### Step 3: Create Virtual Environment (Recommended)

**Why?** Keeps dependencies isolated from other projects.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# You should see (venv) in your terminal
```

### Step 4: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# This will install:
# - pandas, numpy (data processing)
# - transformers, torch (FREE AI model)
# - matplotlib, seaborn (visualization)
# - and other utilities
```

**⏳ Installation time:** 2-5 minutes depending on internet speed

### Step 5: Download AI Model (Automatic)

The AI model downloads automatically on first run:

```bash
# Run the system
python supply_chain_intelligence.py

# First run will download ~900MB
# ⏳ Takes 1-2 minutes
# ✅ Subsequent runs are instant!
```

---

## 🔧 Troubleshooting

### Problem: "pip: command not found"

**Solution:**
```bash
# Use python -m pip instead
python -m pip install -r requirements.txt
```

### Problem: "Permission denied"

**Solution:**
```bash
# Add --user flag
pip install --user -r requirements.txt

# Or use sudo (Linux/macOS)
sudo pip install -r requirements.txt
```

### Problem: "torch not found" or CUDA errors

**Solution:**
```bash
# Install CPU-only version of PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Problem: "No module named 'transformers'"

**Solution:**
```bash
# Install transformers specifically
pip install transformers sentencepiece
```

### Problem: Model download fails

**Solution:**
```bash
# Download model manually
python -c "from transformers import pipeline; pipeline('text2text-generation', model='google/flan-t5-base')"
```

### Problem: Out of memory errors

**Solution:**
```bash
# Use smaller model
# Edit supply_chain_intelligence.py
# Change: AI_MODEL = "google/flan-t5-small"  # 60M params vs 250M
```

---

## ✅ Verify Installation

Run this to check everything is working:

```python
# test_installation.py

try:
    import pandas
    print("✅ pandas installed")
except:
    print("❌ pandas missing")

try:
    import numpy
    print("✅ numpy installed")
except:
    print("❌ numpy missing")

try:
    import transformers
    print("✅ transformers installed")
except:
    print("❌ transformers missing")

try:
    import torch
    print("✅ torch installed")
except:
    print("❌ torch missing")

print("\nAll dependencies installed! 🎉")
```

---

## 🎓 For Students

### University Computer Labs

If you can't install locally:

1. **Use Google Colab** (Free, runs in browser)
   ```bash
   # Upload files to Google Drive
   # Open Colab notebook
   !git clone https://github.com/yourusername/supply-chain-intelligence.git
   !pip install -r supply-chain-intelligence/requirements.txt
   ```

2. **Use Replit** (Free online IDE)
   - Fork repository on Replit
   - Dependencies install automatically

### No Internet After Installation?

The system works offline after first run:

```bash
# First run (needs internet)
python supply_chain_intelligence.py

# After model is cached, disconnect internet
# Run again - works offline! ✅
python supply_chain_intelligence.py
```

---

## 🚀 Next Steps

After installation:

1. **Run the demo**
   ```bash
   python supply_chain_intelligence.py
   ```

2. **Try examples**
   ```bash
   python examples/basic_usage.py
   ```

3. **Read the docs**
   - `docs/API.md` - API documentation
   - `docs/FAQ.md` - Frequently asked questions

4. **Customize for your data**
   - Replace `data/supply_chain_data.xlsx` with your data
   - Update policies in `_create_documents()` method

---

## 💾 Disk Space Breakdown

```
Total: ~2GB

transformers library: ~500MB
torch library: ~200MB
Flan-T5 model: ~900MB
Other dependencies: ~200MB
Code & data: ~200MB
```

---

## 🆘 Still Having Issues?

1. **Check Python version**
   ```bash
   python --version  # Should be 3.8+
   ```

2. **Update pip**
   ```bash
   pip install --upgrade pip
   ```

3. **Clear cache and reinstall**
   ```bash
   pip cache purge
   pip install -r requirements.txt --force-reinstall
   ```

4. **Ask for help**
   - Open GitHub Issue
   - Include error message
   - Include `python --version` output

---

**Installation successful? Great! See [README.md](../README.md) for usage examples.**
