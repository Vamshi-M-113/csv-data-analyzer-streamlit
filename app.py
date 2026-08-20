import streamlit as st

import pandas as pd

import streamlit as st
import pandas as pd
st.sidebar.title("📊 CSV Analyzer")

st.sidebar.write(
    "Upload a CSV file and explore "
    "its data, statistics and visualizations."
)

st.title("📊 CSV Data Analyzer")

file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Data Preview")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    col1.metric("Number of Rows", df.shape[0])
    col2.metric("Number of Columns", df.shape[1])

    st.subheader("Basic Statistics")
    st.dataframe(df.describe())

    st.subheader("Missing Values")
    missing = df.isnull().sum().sum()
    st.metric("Total Missing Values", missing)

    st.subheader("Data Types")
    st.dataframe(df.dtypes)

    st.subheader("Duplicate Rows")
    duplicates = df.duplicated().sum()
    st.metric("Total Duplicate Rows", duplicates)

    st.subheader("Data Visualization")

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    column = st.selectbox(
        "Select a column",
        numeric_columns
    )

    chart_type = st.selectbox(
        "Select chart type",
        ["Bar Chart", "Line Chart"]
    )

    if chart_type == "Bar Chart":
        st.bar_chart(df[column])

    elif chart_type == "Line Chart":
        st.line_chart(df[column])


    st.subheader("Download Data")

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="analyzed_data.csv",
        mime="text/csv"
)