# 📊 AI Business Intelligence Copilot

An AI-powered Business Intelligence platform that enables users to upload datasets, visualize KPIs, generate business insights, and interact with data using natural language powered by Gemini AI.

---
## 🌐 Live Demo

🚀 **Try the application here:**  
https://ai-business-intelligence-copilot-34aj4lqmsvchvd42hvnebm.streamlit.app

## 🚀 Features
## 📸 Application Preview

### Dashboard Overview

![Dashboard Overview](https://github.com/Nikhil16722/AI-Business-Intelligence-Copilot/blob/main/assets/dashboard-overview.png.png)

---

### Sales Analytics Dashboard

![Sales Analytics](assets/sales-analytics.png)

---

### Product Performance Analysis

![Product Analysis](assets/product-analysis.png)

---

### AI-Powered Data Assistant

![AI Query Interface](https://github.com/Nikhil16722/AI-Business-Intelligence-Copilot/blob/main/assets/ai-query-interface.png.png)
### 📂 Data Management
- Upload CSV datasets
- Automatic data cleaning and preprocessing
- Missing value handling
- Duplicate record removal

### 📈 Business Analytics
- Total Sales Analysis
- Profit Analysis
- Profit Margin Calculation
- Region-wise Performance Tracking
- Product-wise Performance Tracking

### 📊 Interactive Dashboards
- Monthly Sales Trends
- Region Sales Comparison
- Product Contribution Analysis
- Sales vs Profit Visualization
- Dynamic Filtering by Product and Region

### 🤖 AI-Powered Insights
- AI-generated executive summaries
- Automated trend identification
- Risk analysis
- Business recommendations

### 💬 Natural Language Querying
Ask questions like:

- Which region generated the highest sales?
- What is the total profit?
- Which product performed best?
- Give me business recommendations.
- Explain sales trends.

### 🗄️ Database Integration
- SQLite database storage
- Structured analytics workflow

---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Visualization | Plotly |
| AI | Google Gemini AI |
| Backend | Python |
| Environment | Python Dotenv |

---

## 🏗️ System Architecture

```text
User Uploads CSV
        │
        ▼
Data Cleaning Layer
        │
        ▼
 KPI Calculation Engine
        │
        ▼
 Interactive Dashboard
        │
        ▼
 Gemini AI Analysis
        │
        ▼
 Natural Language Q&A
```

---

## 📁 Project Structure

```text
AI-Business-Intelligence-Copilot
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── sales.csv
│
├── database/
│   └── db.py
│
└── utils/
    ├── ai_engine.py
    ├── charts.py
    ├── cleaning.py
    └── kpi.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Business-Intelligence-Copilot.git
```

```bash
cd AI-Business-Intelligence-Copilot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run Application

```bash
python -m streamlit run app.py
```

Application launches at:

```text
http://localhost:8501
```

---

## 📸 Dashboard Preview

### KPI Dashboard

- Total Sales
- Total Profit
- Profit Margin

### Interactive Visualizations

- Monthly Sales Trends
- Region Analysis
- Product Contribution
- Sales vs Profit

### AI Executive Summary

Automatically generates:

- Key Insights
- Business Trends
- Risks
- Recommendations

---

## 📋 Sample Questions

```text
Which product generated the highest revenue?
```

```text
What is the profit margin?
```

```text
Which region has the highest sales?
```

```text
Give me 5 business recommendations.
```

```text
Explain the sales trend.
```

---

## 🎯 Business Impact

This platform helps organizations:

- Reduce manual reporting effort
- Improve decision-making speed
- Discover hidden business trends
- Generate automated executive reports
- Democratize data analytics through natural language

---

## 🔮 Future Enhancements

- Sales Forecasting using Machine Learning
- PDF Report Generation
- Power BI Integration
- Role-Based Access Control
- Multi-Dataset Analytics
- Real-Time Data Streaming
- Advanced SQL Query Generator

---

## 👨‍💻 Author

**Nikhil**

AI Engineer | Data Analytics Enthusiast | Python Developer

LinkedIn: https://www.linkedin.com/in/nikhil-lingala-a26030266

GitHub: https://github.com/Nikhil16722

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
