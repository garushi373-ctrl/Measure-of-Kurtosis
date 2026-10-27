
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Measure of Kurtosis",
    page_icon="🌧️",
    layout="wide"
)

st.title("🌧️ Measure of Kurtosis")
st.subheader("Nagpur Daily Rainfall Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("Nagpur_Daily_Rainfall_Cleaned.csv")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Rainfall_mm"] = pd.to_numeric(
        df["Rainfall_mm"], errors="coerce"
    )
    df = df.dropna(subset=["Date", "Rainfall_mm"])
    df = df[df["Rainfall_mm"] >= 0]
    return df.sort_values("Date")

try:
    df = load_data()
    
    rainfall = df["Rainfall_mm"]

    st.success("Rainfall dataset loaded successfully!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(df))
    col2.metric("Average Rainfall", f"{rainfall.mean():.2f} mm")
    col3.metric("Maximum Rainfall", f"{rainfall.max():.2f} mm")

    st.divider()

    
    st.subheader("Daily Rainfall Chart")

    # Ensure dates are correctly interpreted
    chart_data = df[["Date", "Rainfall_mm"]].copy()
    chart_data["Date"] = pd.to_datetime(chart_data["Date"])

    chart_data = chart_data.sort_values("Date")
    chart_data = chart_data.set_index("Date")

    st.line_chart(chart_data, x_label="Date", y_label="Rainfall (mm)")

    
    st.subheader("Rainfall Distribution Histogram")

    
    st.subheader("Rainfall Distribution Histogram")

    fig, ax = plt.subplots()
    ax.hist(df["Rainfall_mm"], bins=10, edgecolor="black")
    ax.set_xlabel("Rainfall (mm)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Daily Rainfall")


    st.pyplot(fig)
    plt.close(fig)

    
    st.divider()

    st.subheader("📊 Kurtosis Result Interpretation")

    kurtosis_value = rainfall.kurt()
    skewness_value = rainfall.skew()

    st.write(f"**Excess Kurtosis:** {kurtosis_value:.4f}")
    st.write(f"**Skewness:** {skewness_value:.4f}")

    if kurtosis_value > 0:
        st.info(
            "The distribution is Leptokurtic. "
            "It has positive excess kurtosis, suggesting "
            "heavier tails than a normal distribution."
        )
    elif kurtosis_value < 0:
        st.info(
            "The distribution is Platykurtic. "
            "It has negative excess kurtosis, suggesting "
            "lighter tails than a normal distribution."
        )
    else:
        st.info(
            "The distribution has zero excess kurtosis, "
            "matching the normal distribution's kurtosis level."
            )

    if skewness_value > 0:
        st.write(
            "**Skewness:** The rainfall distribution is "
            "positively skewed, with a tail toward higher rainfall."
        )
    elif skewness_value < 0:
        st.write(
            "**Skewness:** The rainfall distribution is "
            "negatively skewed."
        )
    else:
        st.write("**Skewness:** The distribution is approximately symmetric.")


    st.subheader("Statistical Analysis")

    col4, col5, col6 = st.columns(3)

    col4.metric("Variance", f"{rainfall.var():.4f}")
    col5.metric("Skewness", f"{rainfall.skew():.4f}")
    col6.metric("Excess Kurtosis", f"{rainfall.kurt():.4f}")

    st.subheader("Rainfall Dataset")
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "Download Cleaned Dataset",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="cleaned_rainfall.csv",
        mime="text/csv"
    )

except FileNotFoundError:
    st.error(
        "CSV file sapadli nahi. CSV file app.py sobat "
        "same project folder madhye aahe ka te check kar."
    )
