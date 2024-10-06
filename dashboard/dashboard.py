import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

main_data = pd.read_csv('dashboard/main_data.csv')

main_data['dteday'] = pd.to_datetime(main_data['dteday'])

st.title("Dashboard Penggunaan Sepeda")

selected_date = st.date_input("Pilih Tanggal", value=pd.to_datetime("2011-01-01"), min_value=main_data['dteday'].min(), max_value=main_data['dteday'].max())

filtered_data = main_data[main_data['dteday'] == pd.to_datetime(selected_date)]

st.subheader("Penggunaan Sepeda Berdasarkan Jam")

# Menghitung jumlah penyewaan rata-rata berdasarkan jam
hourly_summary = filtered_data.groupby('hr')['cnt'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hourly_summary, marker='o', palette="Blues")
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Rata-rata Penyewaan Sepeda')
st.pyplot(plt)

st.subheader("Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")

main_data['weekday'] = main_data['weekday'].replace({
    0: 'Minggu',
    1: 'Senin',
    2: 'Selasa',
    3: 'Rabu',
    4: 'Kamis',
    5: 'Jumat',
    6: 'Sabtu',
})

main_data['weekday'] = pd.Categorical(main_data['weekday'], categories=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'], ordered=True)

# Menghitung jumlah penyewaan rata-rata berdasarkan hari dalam seminggu
daily_summary = main_data.groupby('weekday')['cnt'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='weekday', y='cnt', data=daily_summary, palette="coolwarm")
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Hari')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Rata-rata Penyewaan Sepeda')
st.pyplot(plt)

st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")

main_data['weathersit'] = main_data['weathersit'].replace({
    1: 'Cerah',
    2: 'Mendung',
    3: 'Gerimis',
    4: 'Badai'
})

main_data['weathersit'] = pd.Categorical(main_data['weathersit'], categories=['Cerah', 'Mendung', 'Gerimis', 'Badai'], ordered=True)
weather_summary = main_data.groupby('weathersit')['cnt'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_summary, palette="Blues")
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Penyewaan Sepeda')
st.pyplot(plt)