import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    return data

def plot_top_cities(df):
    final_order_counts = pd.read_csv('lokasipembeli.csv')
    final_order_counts_sorted = final_order_counts.sort_values(by='order_count', ascending=False)
    top_cities = final_order_counts_sorted[final_order_counts_sorted['grouped_city'] != 'others'].head(10)


    plt.figure(figsize=(12, 8))
    bars = plt.bar(top_cities['grouped_city'], top_cities['order_count'], color='skyblue')

    plt.title('Top 10 Kota dengan Jumlah Pembelian Tertinggi')
    plt.xlabel('City')
    plt.ylabel('Order Count')
    plt.xticks(rotation=45, ha="right")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, str(int(yval)), ha='center', va='bottom')

    st.pyplot(plt.gcf())

def plot_top_product_categories(data):
    category_counts = pd.read_csv("category_order_counts.csv")
    top_categories = category_counts.sort_values(by='order_count', ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(top_categories['product_category_name_english'], top_categories['order_count'], color='skyblue')
    plt.title('Top 10 Product Categories by Order Count')
    plt.xlabel('Product Category')
    plt.ylabel('Order Count')
    plt.xticks(rotation=45, ha="right")  
    for index, value in enumerate(top_categories['order_count']):
        plt.text(index, value, str(value), ha='center', va='bottom')
    st.pyplot(plt.gcf())

order_counts_data = load_data('lokasipembeli.csv')
product_categories_data = load_data('category_order_counts.csv')



st.sidebar.title("Pilih Chart")
options = st.sidebar.radio('Choose a chart:', ['Semua Data', 'Top 10 Kota dengan Jumlah Pembelian Tertinggi', 'Top 10 Katagori Produk dengan Jumlah Pembelian Tertinggi'])

st.title('INSIGHTS FROM E-COMMERCE DATA')

if options == 'Semua Data':
    st.header('Top 10 Kota dengan Jumlah Pembelian Tertinggi')
    plot_top_cities(order_counts_data)
    st.header('Top 10 Katagori Produk dengan Jumlah Pembelian Tertinggi')
    plot_top_product_categories(product_categories_data)
elif options == 'Top 10 Kota dengan Jumlah Pembelian Tertinggi':
    st.header('Top 10 Kota dengan Jumlah Pembelian Tertinggi')
    plot_top_cities(order_counts_data)
elif options == 'Top 10 Katagori Produk dengan Jumlah Pembelian Tertinggi':
    st.header('Top 10 Katagori Produk dengan Jumlah Pembelian Tertinggi')
    plot_top_product_categories(product_categories_data)