import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

st.header('Bike Sharing Dashboard')

day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

main_df = pd.read_csv("main_data.csv")

# Menghitung rata-rata rental bike per month
month_counts = day_df.groupby('mnth')['cnt'].mean()

print(month_counts)

# Convert the dteday column to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

day_df['day_of_week'] = day_df['dteday'].dt.day_name()
rentals_by_day = day_df.groupby('day_of_week')['cnt'].mean()

# Plot grafik 1
st.subheader("Rental Bike Performance in One Month")

# Plotting a pie chart using Matplotlib and displaying it with Streamlit
fig, ax = plt.subplots()
ax.pie(month_counts, labels=[
    'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli',
    'Agustus', 'September', 'Oktober', 'November', 'Desember'
], autopct='%1.1f%%', startangle=90)

ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
ax.set_title('Rata-Rata Dalam Sebulan')

# Display the pie chart in the Streamlit app
st.pyplot(fig)

# Grafik 2
st.subheader("Total Rentals per Hour")

# Read sample data into a DataFrame
hour_df = pd.read_csv('hour.csv')

# Calculate total rentals per hour
total_rentals_per_hour = hour_df.groupby(hour_df['hr'])['cnt'].sum()

# Display the total rentals per hour
# st.write('Total Rentals Per Hour:', total_rentals_per_hour)

# Plotting a line chart using Matplotlib and displaying it with Streamlit
fig, ax = plt.subplots()
ax.plot(total_rentals_per_hour.index, total_rentals_per_hour.values, marker='o')
ax.set(xlabel='Jam', ylabel='Jumlah Rental Bike', title='Total Rentals Per Hour')
st.pyplot(fig)

st.caption('Copyright (c) Dicoding 2023')