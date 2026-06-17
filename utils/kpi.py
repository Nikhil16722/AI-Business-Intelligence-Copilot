import pandas as pd

def get_dataset_quality(df):

    total_cells = (
        len(df)
        * len(df.columns)
    )

    missing_cells = (
        df.isna()
        .sum()
        .sum()
    )

    quality_score = (
        (
            total_cells
            - missing_cells
        )
        /
        total_cells
    ) * 100

    return round(
        quality_score,
        2
    )

def generate_dynamic_kpis(df):

    kpis = {}

    # --------------------------------
    # Total Records
    # --------------------------------

    kpis["📋 Records"] = len(df)

    # --------------------------------
    # Missing Values
    # --------------------------------

    kpis["⚠ Missing"] = int(
        df.isna().sum().sum()
    )

    # --------------------------------
    # Numeric Analysis
    # --------------------------------

    numeric_cols = (
        df.select_dtypes(
            include="number"
        )
        .columns
        .tolist()
    )

    if numeric_cols:

        primary_col = None

        for col in numeric_cols:

            if "id" not in col.lower():

                primary_col = col
                break

        if primary_col:

            kpis[f"📊 Avg {primary_col}"] = round(
                df[primary_col].mean(),
                2
            )

            kpis[f"📈 Max {primary_col}"] = round(
                df[primary_col].max(),
                2
            )

    # --------------------------------
    # Categories
    # --------------------------------

    categorical_cols = (
        df.select_dtypes(
            include="object"
        )
        .columns
        .tolist()
    )

    if categorical_cols:

        kpis["🏷 Categories"] = (
            df[
                categorical_cols[0]
            ].nunique()
        )

    return kpis