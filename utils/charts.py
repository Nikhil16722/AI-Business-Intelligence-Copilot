import plotly.express as px

def monthly_sales_chart(df):

    monthly = (
        df.groupby(
            df["Date"].dt.month
        )["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Date",
        y="Sales",
        title="Monthly Sales"
    )

    return fig


def region_sales_chart(df):

    region = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region,
        x="Region",
        y="Sales",
        title="Region Sales"
    )

    return fig