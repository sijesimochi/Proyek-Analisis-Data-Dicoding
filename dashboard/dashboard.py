import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# from babel.numbers import format_currency
sns.set_theme(style='dark')

def create_daily_rent_df(df):
    daily_rent_df = df.resample(rule='D', on='date').agg({
        'rental_count' : 'sum'
    })
    daily_rent_df = daily_rent_df.reset_index()
    return daily_rent_df

def create_monthly_rent_df(df):
    monthly_rent_df = df.resample(rule='ME', on='date').agg({
        'rental_count' : 'sum'
    })
    monthly_rent_df = monthly_rent_df.reset_index()
    return monthly_rent_df

def create_rent_by_season_df(df):
    rent_by_season_df = df.groupby(by='season', sort=False)['rental_count'].mean().sort_values(ascending = False).reset_index()
    return rent_by_season_df

def create_working_day_df(df):
    working_day_df = df.groupby(by='workingday')['rental_count'].sum().reset_index()
    return working_day_df

def create_days_df(df):
    days_df = df.groupby(by='weekday', sort=False)['rental_count'].sum().reset_index()
    return days_df

# load final/cleaned data
all_df = pd.read_csv("/dashboard/day_modified.csv")

datetime_columns = ['date']
all_df.sort_values(by='date', inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df['date'])

min_date = all_df['date'].min()
max_date = all_df['date'].max()


with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    start_date, end_date = st.date_input(
        label='Select Time Span',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
st.set_option('deprecation.showPyplotGlobalUse', False)

main_df = all_df[(all_df['date'] >= str(start_date)) & 
                (all_df['date'] <= str(end_date))]
    
daily_rent_df = create_daily_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
rent_by_season_df = create_rent_by_season_df(main_df)
working_day_df = create_working_day_df(main_df)
days_df = create_days_df(main_df)


st.subheader('Total Rents')
col1 = st.columns(1)[0]
with col1:
    total_rent = monthly_rent_df.rental_count.sum()
    st.metric("Total rents", value=total_rent)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(daily_rent_df["date"], daily_rent_df["rental_count"], marker='.')
ax.set_title("Daily Bikes Rental Trend")
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly_rent_df["date"], monthly_rent_df["rental_count"], marker='.')
ax.set_title("Monthly Bikes Rental Trend")
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
st.pyplot(fig)

st.header('How seasons affect Rental Count')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    data = rent_by_season_df, 
    x="season",
    y="rental_count"
)

ax.set_title("Rental count based on Season")
ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=12)
st.pyplot()


st.header('How workday affect Rental Count')
labels = working_day_df['workingday']
sizes = working_day_df['rental_count']

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(sizes, labels=labels, autopct='%1.2f%%')

ax.set_title('Percentage of Total Rental Bikes by Working Day')
ax.axis('equal')
st.pyplot(fig)


st.header('How every days in a week affect Rental Count')
labels = days_df['weekday']
sizes = days_df['rental_count']

fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(sizes, labels=labels, autopct='%1.2f%%', counterclock=False, startangle=180)

ax.set_title('Percentage of Total Rental Bikes by Days')
ax.axis('equal')
st.pyplot(fig)