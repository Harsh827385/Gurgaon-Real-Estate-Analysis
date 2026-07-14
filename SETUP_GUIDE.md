# 🚀 Quick Setup Guide

## Prerequisites

- Python 3.8 or higher
- Git (optional, for version control)
- Pip (comes with Python)
- ~100MB disk space

## Step-by-Step Installation

### 1. Clone or Download the Project

```bash
# Clone from GitHub
git clone https://github.com/yourname/Gurgaon-Real-Estate-Analysis.git
cd Gurgaon-Real-Estate-Analysis

# Or extract the ZIP file and navigate to the folder
```

### 2. Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (web framework)
- pandas (data manipulation)
- numpy (numerical computing)
- plotly (visualizations)
- scikit-learn (machine learning)
- matplotlib & seaborn (additional plotting)
- openpyxl (Excel support)

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501` in your default browser.

### 5. Deactivate Virtual Environment (When Done)

```bash
deactivate
```

## Troubleshooting

### Issue: Command not found `streamlit`

**Solution:**
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install --upgrade streamlit
```

### Issue: Port 8501 already in use

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: ModuleNotFoundError

**Solution:**
```bash
# Reinstall all requirements
pip install -r requirements.txt --force-reinstall
```

### Issue: Data file not found

**Solution:**
- Ensure `dataset/data.csv` exists
- Check file path in `app.py`
- Verify CSV format and encoding

## File Structure

```
Gurgaon-Real-Estate-Analysis/
├── app.py                    ← Start here
├── requirements.txt          ← Dependencies
├── README.md                 ← Full documentation
├── SETUP_GUIDE.md            ← This file
│
├── dataset/
│   └── data.csv             ← Your data
│
├── pages/
│   ├── Home.py
│   ├── Dashboard.py
│   ├── Analysis.py
│   ├── Business_Insights.py
│   ├── Price_Predictor.py
│   └── About.py
│
└── utils/
    ├── __init__.py
    ├── cleaning.py
    ├── analysis.py
    └── charts.py
```

## Features Guide

### 📊 Dashboard
- View KPIs and real-time metrics
- Apply filters by locality, BHK, price, area
- Sort and explore property data
- Download filtered results

### 📈 Analysis
- Statistical analysis by locality
- Builder benchmarking
- Property type comparison
- Correlation analysis

### 💡 Business Insights
- 10 key business questions answered
- Strategic recommendations
- Market trends analysis

### 🤖 Price Predictor
- ML-based price prediction
- Market comparison
- Similar property finder

### 📥 Data Export
- CSV download
- Excel download
- Filtered datasets

## Next Steps

1. **Customize:** Modify colors, settings, company name
2. **Update Data:** Replace data.csv with your dataset
3. **Deploy:** Push to GitHub and deploy to Streamlit Cloud
4. **Share:** Share the link with others

## Common Customizations

### Change Company/Project Name

Edit [app.py](app.py), line ~30:
```python
st.title("Your Company Name - Real Estate Analysis")
```

### Change Dataset

Replace [dataset/data.csv](dataset/data.csv) with your CSV file

### Add Your Contact Info

Edit [pages/About.py](pages/About.py), update email, LinkedIn, website

## Deployment

### Deploy to Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect GitHub repo
4. Deploy with one click!

### Deploy to Heroku

See Streamlit Cloud for easiest option (recommended)

## Performance Tips

- Filter data before analysis for faster results
- Close unused browser tabs
- Restart the app if performance degrades

## Getting Help

- Check README.md for detailed documentation
- Review comments in source code
- Check Streamlit documentation: https://docs.streamlit.io

## Next Features to Add

- [ ] Time-series analysis
- [ ] Advanced ML models
- [ ] API integration
- [ ] Mobile responsive design
- [ ] Real-time data updates

---

**Happy Analyzing! 📊✨**

For questions or support, contact the author or check the project README.
