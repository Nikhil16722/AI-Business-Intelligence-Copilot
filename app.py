import streamlit as st
import pandas as pd
import os

from utils.cleaning import clean_data

from utils.ai_engine import (
    generate_insights,
    ask_question,
    summarize_pdf,
    auto_summary
)

from utils.kpi import (
    generate_dynamic_kpis,
    get_dataset_quality
)

from utils.charts import (
    create_dynamic_charts
)

from utils.pdf_utils import (
    extract_pdf_text,
    generate_pdf_report,
    pdf_statistics,
    preview_text
)

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="AI Business Intelligence Copilot",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# Glassmorphism CSS
# -----------------------------------

# -----------------------------------
# Glassmorphism CSS
# -----------------------------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
135deg,
#0f172a,
#111827,
#1e293b
);
}

.main-title{
font-size:48px;
font-weight:700;
text-align:center;
color:white;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:#cbd5e1;
font-size:18px;
margin-bottom:25px;
}

.glass{
background: rgba(255,255,255,0.08);
backdrop-filter: blur(14px);
-webkit-backdrop-filter: blur(14px);
border-radius:20px;
padding:20px;
border:1px solid rgba(255,255,255,0.1);
box-shadow:0 8px 32px rgba(0,0,0,0.3);
}

.ai-box{
background: rgba(255,255,255,0.08);
backdrop-filter: blur(16px);
-webkit-backdrop-filter: blur(16px);
border-radius:20px;
padding:25px;
border:1px solid rgba(255,255,255,0.1);
color:white;
font-size:16px;
line-height:1.8;
box-shadow:0 8px 32px rgba(0,0,0,0.3);
margin-top:10px;
}

</style>
""", unsafe_allow_html=True
)

# -----------------------------------
# Header
# -----------------------------------

st.markdown("""
<div class="main-title">
📊 AI Business Intelligence Copilot
</div>

<div class="subtitle">
Analyze CSV, Excel and PDF files using Gemini AI
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("⚙ Dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload File",
    type=["csv", "xlsx", "pdf"]
)

# -----------------------------------
# PDF FLOW
# -----------------------------------

if uploaded_file and uploaded_file.name.endswith(".pdf"):

    text = extract_pdf_text(
        uploaded_file
    )

    stats = pdf_statistics(text)

    st.subheader("📄 PDF Overview")

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Words",
        stats["words"]
    )

    c2.metric(
        "Characters",
        stats["characters"]
    )

    c3.metric(
        "Lines",
        stats["lines"]
    )

    st.subheader("📖 Preview")

    st.text_area(
        "",
        preview_text(text),
        height=300
    )

    if st.button(
        "🤖 Analyze PDF"
    ):

        with st.spinner(
            "Analyzing..."
        ):

            summary = summarize_pdf(text)

            st.subheader("🤖 AI PDF Summary")

            st.markdown(
                f"""
                <div class='ai-box'>
                {summary.replace(chr(10), "<br>")}
                </div>
                """,
                unsafe_allow_html=True
            )

            report_path = (
                generate_pdf_report(
                    summary
                )
            )

            with open(
                report_path,
                "rb"
            ) as f:

                st.download_button(
                    "📥 Download Report",
                    f,
                    file_name="AI_Report.pdf"
                )

# -----------------------------------
# CSV / EXCEL FLOW
# -----------------------------------

elif uploaded_file:

    file_type = (
        uploaded_file.name
        .split(".")[-1]
        .lower()
    )

    if file_type == "csv":

        df = pd.read_csv(
            uploaded_file
        )

    else:

        df = pd.read_excel(
            uploaded_file
        )

    df = clean_data(df)

    # -------------------------
    # Dynamic Filters
    # -------------------------

    st.sidebar.markdown("---")

    st.sidebar.subheader(
        "Filters"
    )

    categorical_cols = (
        df.select_dtypes(
            include="object"
        )
        .columns
        .tolist()
    )

    for col in categorical_cols[:5]:

        selected = (
            st.sidebar.multiselect(
                col,
                df[col]
                .dropna()
                .unique(),
                default=df[col]
                .dropna()
                .unique()
            )
        )

        if selected:

            df = df[
                df[col]
                .isin(selected)
            ]

    # -------------------------
    # Dataset Overview
    # -------------------------

    st.subheader(
        "📂 Dataset Overview"
    )

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    # -------------------------
    # KPI Cards
    # -------------------------

    st.subheader(
        "📊 Business KPIs"
    )

    kpis = (
        generate_dynamic_kpis(df)
    )

    cols = st.columns(
        len(kpis)
    )

    for i,(key,value) in enumerate(
        kpis.items()
    ):

        cols[i].metric(
            key,
            value
        )

    # -------------------------
    # Quality Score
    # -------------------------

    quality = (
        get_dataset_quality(df)
    )

    st.success(
        f"Dataset Quality Score: {quality}%"
    )

    # -------------------------
    # Auto Summary
    # -------------------------

    st.subheader("🧠 Dataset Summary")

    summary_text = auto_summary(df)

    st.markdown(
        f"""
        <div class='ai-box'>
        {summary_text.replace(chr(10), "<br>")}
        </div>
        """,
        unsafe_allow_html=True
    )
    # -------------------------
    # Analytics Dashboard
    # -------------------------

    st.subheader(
          "📈 Analytics Dashboard"
    )

    charts = create_dynamic_charts(df)

    for i, chart in enumerate(charts):

        st.plotly_chart(
            chart,
            use_container_width=True,
            key=f"chart_{i}"
            )
        
    # -------------------------
    # AI Insights
    # -------------------------

    st.markdown("---")

    if st.button(
        "🤖 Generate AI Insights"
    ):

        with st.spinner(
            "Generating Insights..."
        ):

            insights = (
                generate_insights(df)
            )

            st.subheader("🤖 AI Executive Summary")

            st.markdown(
                f"""
                <div class='ai-box'>
                {insights.replace(chr(10), "<br>")}
                </div>
                """,
                unsafe_allow_html=True
            )

            report_path = (
                generate_pdf_report(
                    insights
                )
            )

            with open(
                report_path,
                "rb"
            ) as f:

                st.download_button(
                    "📥 Download Report",
                    f,
                    file_name="AI_Report.pdf"
                )

    # -------------------------
    # AI Chat
    # -------------------------

    st.markdown("---")

    st.subheader(
        "💬 AI Data Assistant"
    )

    question = st.chat_input(
        "Ask anything about your data..."
    )

    if question:

        with st.chat_message(
            "user"
        ):
            st.write(question)

        answer = ask_question(
            df,
            question
        )

        with st.chat_message(
            "assistant"
        ):
            st.write(answer)

# -----------------------------------
# Footer
# -----------------------------------

st.markdown("---")

st.caption(
    "AI Business Intelligence Copilot • Gemini AI • Streamlit • Plotly • Pandas"
)