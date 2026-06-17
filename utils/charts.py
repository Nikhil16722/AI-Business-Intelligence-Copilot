import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_dynamic_charts(df):

    charts = []

    numeric_cols = (
        df.select_dtypes(
            include="number"
        )
        .columns
        .tolist()
    )

    categorical_cols = (
        df.select_dtypes(
            include=["object", "category"]
        )
        .columns
        .tolist()
    )

    datetime_cols = (
        df.select_dtypes(
            include=["datetime64[ns]", "datetime"]
        )
        .columns
        .tolist()
    )

    # ----------------------------------
    # Chart 1
    # Numeric Distribution
    # ----------------------------------

    if len(numeric_cols) >= 1:

        fig = px.histogram(
            df,
            x=numeric_cols[0],
            title=f"{numeric_cols[0]} Distribution",
            nbins=30
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        charts.append(fig)

    # ----------------------------------
    # Chart 2
    # Category Distribution
    # ----------------------------------

    if len(categorical_cols) >= 1:

        counts = (
            df[categorical_cols[0]]
            .value_counts()
            .head(10)
            .reset_index()
        )

        counts.columns = [
            categorical_cols[0],
            "Count"
        ]

        fig = px.bar(
            counts,
            x=categorical_cols[0],
            y="Count",
            title=f"{categorical_cols[0]} Analysis"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        charts.append(fig)

    # ----------------------------------
    # Chart 3
    # Pie Chart
    # ----------------------------------

    if len(categorical_cols) >= 1:

        counts = (
            df[categorical_cols[0]]
            .value_counts()
            .head(10)
            .reset_index()
        )

        counts.columns = [
            categorical_cols[0],
            "Count"
        ]

        fig = px.pie(
            counts,
            names=categorical_cols[0],
            values="Count",
            title=f"{categorical_cols[0]} Share"
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        charts.append(fig)

    # ----------------------------------
    # Chart 4
    # Trend Analysis
    # ----------------------------------

    if len(numeric_cols) >= 2:

        temp_df = df.sort_values(
            by=numeric_cols[0]
        )

        fig = px.line(
            temp_df,
            x=numeric_cols[0],
            y=numeric_cols[1],
            markers=True,
            title=f"{numeric_cols[0]} vs {numeric_cols[1]}"
        )

        fig.update_traces(
            line=dict(width=4),
            marker=dict(size=8)
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        charts.append(fig)

    # ----------------------------------
    # Chart 5
    # Time Series Trend
    # ----------------------------------

    if len(datetime_cols) >= 1 and len(numeric_cols) >= 1:

        fig = px.line(
            df,
            x=datetime_cols[0],
            y=numeric_cols[0],
            markers=True,
            title=f"{numeric_cols[0]} Trend Over Time"
        )

        fig.update_traces(
            line=dict(width=4),
            marker=dict(size=8)
        )

        fig.update_layout(
            template="plotly_dark",
            height=450
        )

        charts.append(fig)

    return charts