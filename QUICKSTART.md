# ⚡ Quick Start Guide

Get started in 5 minutes!

---

## 📥 Step 1: Install

```bash
git clone https://github.com/yourusername/supply-chain-intelligence.git
cd supply-chain-intelligence
pip install -r requirements.txt
```

---

## 🚀 Step 2: Run Demo

```bash
python supply_chain_intelligence.py
```

**First run:**
- Downloads AI model (~900MB)
- Takes 1-2 minutes
- Happens only once

**Subsequent runs:**
- Start instantly
- Work offline

---

## 💻 Step 3: Try Basic Features

### Ask Questions

```python
from supply_chain_intelligence import SupplyChainIntelligence

# Initialize
system = SupplyChainIntelligence("data/supply_chain_data.xlsx")

# Ask anything!
system.query("What is the safety stock policy?")
system.query("What should I do if stock is low?")
system.query("How do I handle late suppliers?")
```

### Generate Forecasts

```python
# 30-day demand forecast
forecast = system.forecast_demand("SKU0", days=30)

print(f"Average: {forecast['metrics']['forecast_avg']} units/day")
print(f"Trend: {forecast['metrics']['trend']}")
print(f"Action: {forecast['recommendations']['action']}")
```

### Analyze Risks

```python
# Risk assessment
risks = system.analyze_risks(top_n=20)

# View results
print(risks)

# Save to CSV
risks.to_csv('risks.csv')
```

---

## 🎯 Common Use Cases

### 1. Inventory Management

```python
# Check safety stock compliance
system.query("How much safety stock do I need for Class A items?")

# Get reorder recommendations
forecast = system.forecast_demand("SKU5")
print(f"Reorder at: {forecast['recommendations']['reorder_point']} units")
```

### 2. Supplier Issues

```python
# Policy questions
system.query("What penalties apply for late deliveries?")
system.query("What are acceptable lead times for haircare products?")
```

### 3. Quality Management

```python
# Quality standards
system.query("What defect rates are acceptable?")

# Risk assessment
risks = system.analyze_risks()
quality_issues = risks[risks['risk_factors'].str.contains('Defect')]
```

---

## 🔧 Customize for Your Data

### Replace Sample Data

```python
# Put your Excel file in data/
system = SupplyChainIntelligence("data/YOUR_DATA.xlsx")

# That's it! System adapts automatically
```

### Required Columns

Your Excel file should have:
- `SKU` - Product identifier
- `Product type` - Category
- `Stock levels` - Current inventory
- `Lead time` - Supplier lead time (days)
- `Defect rates` - Quality metric (%)
- `Number of products sold` - Sales history

---

## 💡 Tips

### Faster Startup

```python
# Disable AI for instant startup
system = SupplyChainIntelligence(
    "data/supply_chain_data.xlsx",
    use_ai=False  # 10x faster, still works!
)
```

### Better Quality Answers

```python
# Edit Config class in supply_chain_intelligence.py
class Config:
    AI_MODEL = "google/flan-t5-large"  # Better but slower
```

### Save Results

```python
# Forecast to JSON
import json
forecast = system.forecast_demand("SKU0")
with open('forecast.json', 'w') as f:
    json.dump(forecast, f, indent=2)

# Risks to CSV
risks = system.analyze_risks(top_n=50)
risks.to_csv('full_risk_analysis.csv')
```

---

## 🆘 Troubleshooting

**Problem: "ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

**Problem: Model download fails**
```bash
# Check internet connection
# Try again - downloads resume automatically
python supply_chain_intelligence.py
```

**Problem: Out of memory**
```python
# Use smaller model
# Edit Config.AI_MODEL = "google/flan-t5-small"
```

**Problem: Slow responses**
```python
# Disable AI for testing
system = SupplyChainIntelligence(data_file, use_ai=False)
```

---

## 📚 Learn More

- [Full README](README.md) - Complete documentation
- [Installation Guide](docs/INSTALLATION.md) - Detailed setup
- [Examples](examples/) - More code samples
- [API Docs](docs/API.md) - All functions explained

---

## 🎓 For Students

Perfect for:
- ✅ Capstone projects
- ✅ Portfolio demonstrations
- ✅ Research projects
- ✅ Learning AI/ML

Shows:
- ✅ RAG implementation
- ✅ AI integration
- ✅ Data analysis
- ✅ Clean code practices
- ✅ Real-world application

---

**Ready to explore? Start with `python supply_chain_intelligence.py`** 🚀
