#  Supply Chain Intelligence System

An intelligent supply chain management system combining **RAG (Retrieval-Augmented Generation)**, **AI-powered natural language understanding**, and **demand forecasting**.

> **100% Free** | No API costs | Works offline | Perfect for student projects

---

##  Features

-  **Smart Document Search** - Find policies and procedures instantly using RAG
-  **FREE AI Answers** - Natural language responses using Google's Flan-T5
-  **Demand Forecasting** - Predict future demand with 95% confidence intervals
-  **Risk Analysis** - Automated risk scoring and recommendations
-  **Visual Analytics** - Professional charts and reports
-  **Zero Cost** - No API fees, runs completely locally

---

##  Use Cases

- **Inventory Management** - Optimize stock levels and reorder points
- **Supplier Analysis** - Evaluate supplier performance and risks
- **Demand Planning** - Forecast future demand for better planning
- **Risk Mitigation** - Identify and address supply chain risks
- **Policy Compliance** - Quick access to company policies and procedures

---

##  Demo

```python
from supply_chain_intelligence import SupplyChainIntelligence

# Initialize system
system = SupplyChainIntelligence("data/supply_chain_data.xlsx")

# Ask questions in natural language
system.query("What should I do if stock is critically low?")
# → AI generates actionable answer

# Generate demand forecast
forecast = system.forecast_demand("SKU0", days=30)
# → Returns 30-day forecast with recommendations

# Analyze risks
risks = system.analyze_risks(top_n=20)
# → Returns risk assessment for products
```

---

##  Quick Start

### Prerequisites

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/supply-chain-intelligence.git
   cd supply-chain-intelligence
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download AI model** (automatic on first run)
   ```bash
   # Model downloads automatically (~900MB) on first use
   # Takes 1-2 minutes
   ```

4. **Run the demo**
   ```bash
   python supply_chain_intelligence.py
   ```

---

##  Usage

### Basic Query

```python
from supply_chain_intelligence import SupplyChainIntelligence

# Initialize
system = SupplyChainIntelligence("data/supply_chain_data.xlsx")

# Ask a question
result = system.query("What is the safety stock policy?")
print(result['answer'])
```

### Demand Forecasting

```python
# Generate 30-day forecast
forecast = system.forecast_demand("SKU0", days=30)

print(f"Average forecast: {forecast['metrics']['forecast_avg']} units/day")
print(f"Trend: {forecast['metrics']['trend']}")
print(f"Recommended action: {forecast['recommendations']['action']}")

# Access daily predictions
for day in forecast['predictions'][:7]:
    print(f"{day['date']}: {day['predicted_demand']} units")
```

### Risk Analysis

```python
# Analyze top 20 products
risk_df = system.analyze_risks(top_n=20)

# Filter high-risk products
high_risk = risk_df[risk_df['risk_level'] == 'HIGH']
print(f"High-risk products: {len(high_risk)}")

# Save to CSV
risk_df.to_csv('risk_analysis.csv', index=False)
```

---

##  Project Structure

```
supply-chain-intelligence/
├── supply_chain_intelligence.py  # Main system
├── requirements.txt               # Dependencies
├── README.md                      # This file
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
├── data/                          # Data files
│   └── supply_chain_data.xlsx    # Sample dataset
├── outputs/                       # Generated reports
├── examples/                      # Usage examples
│   ├── basic_usage.py
│   ├── forecasting_demo.py
│   └── risk_analysis_demo.py
└── docs/                          # Documentation
    ├── INSTALLATION.md
    ├── API.md
    └── FAQ.md
```


##  How It Works

### 1. Document Search (RAG)

```
User Query → TF-IDF Search → Top 3 Documents → Context
```

- Indexes all company policies and product data
- Uses TF-IDF for relevance scoring
- No external APIs needed

### 2. AI Answer Generation

```
Context + Query → Flan-T5 (FREE) → Natural Language Answer
```

- Uses Google's Flan-T5 model (250M parameters)
- Runs locally on your machine
- No API costs, works offline

### 3. Demand Forecasting

```
Historical Data → Multi-Method Forecast → Predictions + Insights
```

- Combines moving average, exponential smoothing, and trend analysis
- Generates 95% confidence intervals
- Provides actionable recommendations

### 4. Risk Analysis

```
Product Data → Risk Scoring → Automated Recommendations
```

- Evaluates stock levels, lead times, defect rates
- Scores risks as HIGH/MEDIUM/LOW
- Suggests specific actions

---

##  Sample Output

### Query Example

**Input:**
```
"What should I do if I have only 15% safety stock remaining?"
```

**Output (with AI):**
```
Based on the inventory management policy, 15% safety stock places you in 
RED ALERT status (below the 20% threshold). You should:

1. Initiate an emergency reorder immediately
2. Calculate reorder quantity using: ROP = (Daily Demand × Lead Time) + Safety Stock
3. Consider expedited shipping to restore safety levels quickly

This is a high-priority situation requiring immediate action to avoid stockouts.
```

### Forecast Example

```
SKU: SKU0
Forecast Period: 30 days
Average Forecast: 33.5 units/day
Growth Rate: +12.3%
Trend: Increasing
Confidence: 89%

Recommendations:
  Action: INCREASE inventory
  Target Stock: 469 units (2 weeks coverage)
  Reorder Point: 235 units (1 week coverage)
```

---

### Why This Stands Out

1. **100% Free** - No API costs or subscriptions
2. **Production-Ready** - Clean code, error handling, documentation
3. **AI Integration** - Shows understanding of modern ML
4. **Real-World Application** - Solves actual business problems
5. **Comprehensive** - Covers multiple technical areas

---

##  Configuration

Edit `Config` class in `supply_chain_intelligence.py`:

```python
class Config:
    # AI Model (options: flan-t5-base, flan-t5-large, flan-t5-xl)
    AI_MODEL = "google/flan-t5-base"  # 250M params, fast
    
    # Search settings
    SEARCH_TOP_K = 3  # Number of documents to retrieve
    
    # Forecasting
    FORECAST_DAYS = 30  # Forecast horizon
    FORECAST_HISTORY_DAYS = 90  # Historical data to use


##  Performance

| Metric | Value |
|--------|-------|
| Search Speed | < 100ms |
| AI Response Time | 1-2 seconds |
| Forecast Generation | < 1 second |
| Memory Usage | ~2GB (with AI model) |
| Disk Space | ~1GB (including model) |

---

##  Contributing

Contributions welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---


##  Acknowledgments

- **Google** - For the free Flan-T5 model
- **Hugging Face** - For the transformers library
- **Open Source Community** - For amazing tools and libraries



- [ ] Web interface (Streamlit dashboard)
- [ ] API endpoints (FastAPI)
- [ ] Real-time monitoring
- [ ] Additional forecasting models
- [ ] Multi-language support
- [ ] Mobile app

---


