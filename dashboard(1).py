import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from gpt_wrapper import GPTwrapper

st.set_page_config(page_title="Jeld_Wen Analytics Dashboard", layout="wide")

st.title("Jeld-Wen AI-Powered Analytics Dashboard")
st.write("This dashboard provides predictive sales insight and GPT-generated summaries based on our large-scale sales data.")

@st.cache
def load_data():
    df = pd.read_csv("sales_data.csv", parse_dates=["sales_date"])
    return df

df = load_data()

st.subheader("Sales Data Preview")
st.dataframe(df.head())

import numpy as np
future_dates = pd.date_range(start=datetime.today(), periods=30)
predicted_sales = np.random.uniform(low=500, high=1500, size=30)
predictions_df = pd.DataFrame({"sales_date": future_dates, "predicted_sales": predicted_sales})

st.subheader("Predicted Sales for the Next 30Days")
st.line_chart(predictions_df.set_index("sales_date"))

if "region" in df.columns and "sales_amount" in df.columns:
    region_sales = df.groupby("region")["sales_amount"].sum().reset_index()