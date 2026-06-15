import streamlit as st
import pandas as pd
import plotly.express as px

from utils.cleaning import clean_data
from utils.kpi import calculate_kpis
from utils.ai_engine import (
    generate_insights,
    ask_question
)

from database.db import save_to_db

st.set_page_config(
    page_title="AI BI Copilot",
    page_icon="📊",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.kpi-card{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,0.3);
}

.kpi-title{
    color:#94a3b8;
    font-size:18px;
}

.kpi-value{
    font-size:32px;
    font-weight:bold;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<h1 style='text-align:center'>
📊 AI Business Intelligence Copilot
</h1>

<p style='text-align:center;color:gray'>
Upload CSV files, generate insights, analyze KPIs,
and ask questions in natural language.
</p>
""", unsafe_allow_html=True)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    df = clean_data(df)

    save_to_db(df)

    # ---------------- SIDEBAR FILTERS ---------------- #

    st.sidebar.title("⚙ Filters")

    region_filter = st.sidebar.multiselect(
        "Region",
        df["Region"].unique(),
        default=df["Region"].unique()
    )

    product_filter = st.sidebar.multiselect(
        "Product",
        df["Product"].unique(),
        default=df["Product"].unique()
    )

    df = df[
        (df["Region"].isin(region_filter))
        &
        (df["Product"].isin(product_filter))
    ]

    # ---------------- DATASET ---------------- #

    st.subheader("📂 Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # ---------------- KPI ---------------- #

    kpis = calculate_kpis(df)

    total_sales = kpis["sales"]
    total_profit = kpis["profit"]
    profit_margin = kpis["margin"]

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class='kpi-card'>
        <div class='kpi-title'>💰 Total Sales</div>
        <div class='kpi-value'>
        ₹{total_sales:,.0f}
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class='kpi-card'>
        <div class='kpi-title'>📈 Total Profit</div>
        <div class='kpi-value'>
        ₹{total_profit:,.0f}
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class='kpi-card'>
        <div class='kpi-title'>🎯 Profit Margin</div>
        <div class='kpi-value'>
        {profit_margin:.2f}%
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ---------------- TOP METRICS ---------------- #

    top_product = (
        df.groupby("Product")["Sales"]
        .sum()
        .idxmax()
    )

    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    m1,m2 = st.columns(2)

    m1.metric(
        "🏆 Top Product",
        top_product
    )

    m2.metric(
        "🌍 Best Region",
        top_region
    )

    # ---------------- CHARTS ---------------- #

    monthly_sales = (
        df.groupby(
            df["Date"].dt.month
        )["Sales"]
        .sum()
        .reset_index()
    )

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    product_sales = (
        df.groupby("Product")["Sales"]
        .sum()
        .reset_index()
    )

    chart1, chart2 = st.columns(2)

    with chart1:

        fig1 = px.line(
            monthly_sales,
            x="Date",
            y="Sales",
            title="Monthly Sales Trend",
            markers=True
        )

        fig1.update_layout(
            template="plotly_dark",
            title_x=0.5
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with chart2:

        fig2 = px.bar(
            region_sales,
            x="Region",
            y="Sales",
            title="Region Sales"
        )

        fig2.update_layout(
            template="plotly_dark",
            title_x=0.5
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ---------------- SECOND ROW ---------------- #

    c4,c5 = st.columns(2)

    with c4:

        fig3 = px.pie(
            product_sales,
            names="Product",
            values="Sales",
            title="Product Contribution"
        )

        fig3.update_layout(
            template="plotly_dark",
            title_x=0.5
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with c5:

        fig4 = px.scatter(
            df,
            x="Sales",
            y="Profit",
            color="Product",
            size="Quantity",
            title="Sales vs Profit"
        )

        fig4.update_layout(
            template="plotly_dark",
            title_x=0.5
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )

    # ---------------- AI INSIGHTS ---------------- #

    st.markdown("---")

    if st.button("🤖 Generate AI Insights"):

        with st.spinner("Analyzing Data..."):

            insights = generate_insights(df)

            st.markdown(
                "### 🤖 AI Executive Summary"
            )

            st.info(insights)

    # ---------------- Q&A ---------------- #

    st.markdown("---")

    st.subheader("💬 Ask AI About Your Data")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        with st.spinner("Thinking..."):

            answer = ask_question(
                df,
                question
            )

            st.success(answer)

    # ---------------- FOOTER ---------------- #

    st.markdown("---")

    st.caption(
        "AI Business Intelligence Copilot • Powered by Gemini AI, Streamlit, Plotly & SQL"
    )