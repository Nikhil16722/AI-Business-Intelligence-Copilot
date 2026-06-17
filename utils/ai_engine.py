from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import pandas as pd
import os

load_dotenv()

# ----------------------------
# Gemini Configuration
# ----------------------------

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

# ----------------------------
# Dataset Insights
# ----------------------------

def generate_insights(df):

    summary = df.describe(
        include="all"
    ).to_string()

    columns = ", ".join(df.columns)

    prompt = f"""
You are a senior business analyst.

Dataset Columns:
{columns}

Dataset Statistics:
{summary}

Generate:

1. Executive Summary
2. Key Insights
3. Trends
4. Risks
5. Recommendations

Use clear business language.
"""

    response = model.generate_content(
        prompt
    )

    return response.text


# ----------------------------
# Dataset Q&A
# ----------------------------

def ask_question(df, question):

    sample = df.head(100).to_string()

    prompt = f"""
You are an AI Data Analyst.

Dataset Sample:

{sample}

Question:

{question}

Answer ONLY using information
available in the dataset.
"""

    response = model.generate_content(
        prompt
    )

    return response.text


# ----------------------------
# PDF Analysis
# ----------------------------

def summarize_pdf(text):

    prompt = f"""
Analyze the following document.

{text[:15000]}

Generate:

1. Executive Summary
2. Main Topics
3. Key Insights
4. Important Findings
5. Recommendations
"""

    response = model.generate_content(
        prompt
    )

    return response.text


# ----------------------------
# Dataset Description
# ----------------------------

def dataset_overview(df):

    columns = list(df.columns)

    numeric_cols = (
        df.select_dtypes(
            include="number"
        )
        .columns
        .tolist()
    )

    categorical_cols = (
        df.select_dtypes(
            include="object"
        )
        .columns
        .tolist()
    )

    return {
        "rows": len(df),
        "columns": len(columns),
        "numeric": numeric_cols,
        "categorical": categorical_cols
    }


# ----------------------------
# AI KPI Suggestions
# ----------------------------

def generate_kpi_suggestions(df):

    stats = df.describe(
        include="all"
    ).to_string()

    prompt = f"""
Dataset Statistics:

{stats}

Suggest:

1. Important KPIs
2. Metrics to Monitor
3. Dashboard Recommendations

Keep response concise.
"""

    response = model.generate_content(
        prompt
    )

    return response.text


# ----------------------------
# Auto Insights
# ----------------------------

def auto_summary(df):

    rows = len(df)
    cols = len(df.columns)

    numeric_cols = (
        df.select_dtypes(
            include="number"
        )
        .columns
        .tolist()
    )

    categorical_cols = (
        df.select_dtypes(
            include="object"
        )
        .columns
        .tolist()
    )

    summary = f"""
Dataset contains {rows:,} rows
and {cols} columns.

Numeric Columns:
{', '.join(numeric_cols)}

Categorical Columns:
{', '.join(categorical_cols)}
"""

    return summary