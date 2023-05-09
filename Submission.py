import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='dteday').agg({
        "casual_x": "sum",
        "registered_x": "sum"
    })
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        "casual_x": "casual",
        "registered_x": "registered"
    }, inplace=True)

    return daily_orders_df

##
all_df = pd.read_csv("bike.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

## Filter
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

st.header("Krisna's Submission")

# Mengambil start_date & end_date dari date_input
start_date, end_date = st.date_input(
    label='Rentang Waktu', min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

main_df = all_df[(all_df["dteday"] >= str(start_date)) &
                (all_df["dteday"] <= str(end_date))]

## Apply Function
daily_orders_df = create_daily_orders_df(main_df)

## Viz
st.subheader('Daily Bike Orders')

totals = main_df.cnt_x.sum()
st.metric("Total Orders", value=totals)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20, 10))

colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

sns.barplot(x="hr", y="cnt_x", data=main_df, palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Total User of Bike Rental", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=12)

st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    total_casual = daily_orders_df.casual.sum()
    st.metric("Casual User Orders", value=total_casual)

with col2:
    total_registered = daily_orders_df.registered.sum()
    st.metric("Registered Orders", value=total_registered)


st.subheader('Hourly Bike Orders')

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20, 10))

colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

sns.barplot(x="hr", y="casual_x", data=main_df, palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Casual User of Bike Rental", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20, 10))
sns.barplot(x="hr", y="registered_x", data=main_df, palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()
ax.set_title("Registered User of Bike Rental", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

st.caption('Copyright (c) Krisna 2023')