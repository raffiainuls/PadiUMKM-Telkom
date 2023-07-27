

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import requests
from datetime import datetime
from scipy.stats import zscore






# Commented out IPython magic to ensure Python compatibility.
# Ubah lokasi direktori kerja
# Sesuaikan dengan path anda
# %cd /content/drive/MyDrive/Project_PadiUMKM



data_category = pd.read_csv('data.csv')

"""## Categori Favorit

"""
plot_category = []
plot_elektronik = ['Office & Stationery',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga']
plot_office = ['Elektronik dan IT',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga',]
plot_barang = ['Elektronik dan IT', 'Office & Stationery',
        'Kebutuhan Sehari-hari', 'Otomotif',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga']
plot_kebutuhan_sehari_hari = ['Elektronik dan IT', 'Office & Stationery',
       'Barang,Jasa dan Persewaan',  'Otomotif',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga']
plot_otomotif = ['Elektronik dan IT', 'Office & Stationery',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga']
plot_hiburan = ['Elektronik dan IT', 'Office & Stationery',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga']
plot_kesehatan = ['Elektronik dan IT', 'Office & Stationery',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif',
       'Hiburan',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga']
plot_pertanian = ['Elektronik dan IT', 'Office & Stationery',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
        'Pendidikan dan Pelatihan', 'Olahraga']
plot_pendidikan = ['Elektronik dan IT', 'Office & Stationery',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan',  'Olahraga']
plot_olahraga = ['Elektronik dan IT', 'Office & Stationery',
       'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif',
       'Hiburan', 'Kesehatan/Kecantikan/Fashion',
       'Pertanian & Pertenakan', 'Pendidikan dan Pelatihan']
#data_category_fav = data_category[data_category['rating'] != 0]
#data_category_fav

#aggegsi count po_number
category_fav = data_category.pivot_table(values = 'po_number', index = 'sum_category', aggfunc = 'count')
category_fav.sort_values(by = 'po_number', ascending = True, inplace = True)
category_fav.reset_index(inplace = True)
category_fav.rename(columns= {'po_number' : 'Total Order', 'sum_category' : 'Category'}, inplace = True)

#plot column chart
plot_category_fav = px.bar(category_fav, x = 'Total Order', y = 'Category')
plot_category_fav.update_layout(height = 400, title = 'Category Favorite', title_x=0.5)
plot_category_fav.update_xaxes(title = 'Total Order')
plot_category_fav.update_yaxes(title = 'Category')



def plot_top_category(category,list_bulan, data_category=data_category):
    data_category['order_month'] = data_category['order_date'].str.slice(0, 7)
    data = data_category.groupby(['sum_category', 'order_month']).agg({'po_number': 'count'})
    data.reset_index(inplace=True)

    # Splitting 'order_month' into 'year' and 'month' columns
    data['month'] = data_category['order_date'].str.slice(5, 7)

    month = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    data['month'] = data['month'].map(month)
    data = data.loc[data['month'].isin(list_bulan)]
    data.reset_index(inplace=True)
    data.rename(columns={'po_number': 'Total Order', 'sum_category': 'Category'}, inplace=True)
    data.sort_values('Total Order', ascending=False, inplace=True)

    color_map = {'Office & Stationery' : '#35A29F',
               'Kebutuhan Sehari-hari' : '#35A29F',
               'Barang,Jasa dan Persewaan' : '#35A29F',
               'Elektronik dan IT' : '#35A29F',
               'Kesehatan/Kecantikan/Fashion': '#35A29F',
               'Hiburan' : '#35A29F',
               'Otomotif' : '#35A29F',
               'Pertanian & Pertenakan' : '#35A29F',
               'Olahraga' : '#35A29F',
               'Pendidikan dan Pelatihan' : '#35A29F'}
    
    for key in color_map:
      if key in category:
        continue
      color_map[key] = '#DAFFFB'

    fig = px.bar(data, x = 'Total Order', y = 'Category', color= 'Category', color_discrete_map=color_map)
    fig.update_yaxes(title = '')

    return  fig

# replace name_provinsi to adapt geojson indonesia
data_category = data_category.replace('KALIMANTAN TIMUR', 'Kalimantan Timur')
data_category = data_category.replace('DKI JAKARTA', 'Jakarta Raya')
data_category = data_category.replace('BENGKULU', 'Bengkulu')
data_category = data_category.replace('KALIMANTAN TIMUR', 'Sumatera Selatan')
data_category = data_category.replace('SUMATERA SELATAN', 'Kalimantan Timur')
data_category = data_category.replace('MALUKU', 'Maluku')
data_category = data_category.replace('RIAU', 'Riau')
data_category = data_category.replace('SULAWESI SELATAN', 'Sulawesi Selatan')
data_category = data_category.replace('KALIMANTAN BARAT', 'Kalimantan Barat')
data_category = data_category.replace('JAWA TIMUR', 'Jawa Timur')
data_category = data_category.replace('SUMATERA UTARA', 'Sumatera Utara')
data_category = data_category.replace('BALI', 'Bali')
data_category = data_category.replace('JAWA TENGAH', 'Jawa Tengah')
data_category = data_category.replace('JAWA BARAT', 'Jawa Barat')
data_category = data_category.replace('ACEH', 'Aceh')
data_category = data_category.replace('BANTEN', 'Banten')
data_category = data_category.replace('KEPULAUAN RIAU', 'Kepulauan Riau')
data_category = data_category.replace('PAPUA', 'Papua')
data_category = data_category.replace('PAPUA BARAT', 'Papua Barat')
data_category = data_category.replace('SULAWESI TENGAH', 'Sulawesi Tengah')
data_category = data_category.replace('LAMPUNG', 'Lampung')
data_category = data_category.replace('KEPULAUAN BANGKA BELITUNG', 'Bangka-Belitung')
data_category = data_category.replace('SUMATERA BARAT', 'Sumatera Barat')
data_category = data_category.replace('NUSA TENGGARA BARAT', 'Nusa Tenggara Barat')
data_category = data_category.replace('DI YOGYAKARTA', 'Yogyakarta')
data_category = data_category.replace('SULAWESI UTARA', 'Sulawesi Utara')
data_category = data_category.replace('JAMBI', 'Jambi')
data_category = data_category.replace('GORONTALO', 'Gorontalo')
data_category = data_category.replace('KALIMANTAN TENGAH', 'Kalimantan Tengah')
data_category = data_category.replace('SULAWESI TENGGARA', 'Sulawesi Tenggara')
data_category = data_category.replace('KALIMANTAN UTARA', 'Kalimantan Utara')
data_category = data_category.replace('KALIMANTAN SELATAN', 'Kalimantan Selatan')
data_category = data_category.replace('NUSA TENGGARA TIMUR', 'Nusa Tenggara Timur')
data_category = data_category.replace('MALUKU UTARA', 'Maluku Utara')
data_category = data_category.replace('D.I. Aceh', 'Aceh')
data_category = data_category.replace('Papua Barat', 'Papua')
data_category = data_category.replace('D.I. Yogyakarta', 'Yogyakarta')
data_category = data_category.replace('Papua Selatan', 'Papua')

data_category ['order_month'] = data_category['order_date'].str.slice(0,7)
data_category

#add column order_month
"""data_category ['order_month'] = data_category['order_date'].str.slice(0,7)
data_category

#groupby order_month and sum_category
line_category = data_category.groupby(['order_month', 'sum_category']).agg({'po_number' : 'count'})
line_category.reset_index(inplace = True)
#change type data order_month to datetime with format Y-m
line_category['order_month'] = pd.to_datetime(line_category['order_month'], format = '%Y-%m')
#take unique_date month
unique_dates = line_category['order_month'].dt.to_period('M').unique()
# make line chart
fig_line = px.line(line_category, x = 'order_month', y = 'po_number', color = 'sum_category', markers = True)

# edit tickvls that the xaxes date show online uniqe dates
fig_line.update_xaxes(tickvals=unique_dates.to_timestamp(),tickformat = '%b %Y')
fig_line.show()
"""

def line_category(data, list_not_category):
  #groupby order_month and sum_category
  data_line = data.groupby(['order_month', 'sum_category']).agg({'po_number' : 'count'})
  data_line.reset_index(inplace = True)

  #change type data order_month to datetime with format Y-m
  data_line['order_month'] = pd.to_datetime(data_line['order_month'], format = '%Y-%m')

  #take unique_date month
  unique_dates = data_line['order_month'].dt.to_period('M').unique()

  #take sum_category only not in list
  data_line = data_line.loc[~data_line['sum_category'].isin(list_not_category)]

  #make line_chart
  fig = px.line(data_line, x = 'order_month',  y = 'po_number', color = 'sum_category', markers = True)

  # edit tickvls that the xaxes date show online uniqe dates
  fig.update_xaxes(tickvals = unique_dates.to_timestamp(), tickformat = '%b %Y')
  return fig



line_plot_category = line_category(data_category, plot_category)
line_plot_elektronik = line_category(data_category, plot_elektronik)
line_plot_office = line_category(data_category, plot_office)
line_plot_barang = line_category(data_category, plot_barang)
line_plot_kebutuhan = line_category(data_category, plot_kebutuhan_sehari_hari)
line_plot_otomotif = line_category(data_category, plot_otomotif)
line_plot_hiburan = line_category(data_category, plot_hiburan)
line_plot_kesehatan = line_category(data_category, plot_kesehatan)
line_plot_pertanian = line_category(data_category, plot_pertanian)
line_plot_pendidikan = line_category(data_category, plot_pendidikan)
line_plot_olahraga = line_category(data_category, plot_olahraga)

"""data_map_category = data_category.groupby('provinsi').agg({'po_number' : 'count'})
data_map_category.reset_index(inplace = True)
geojson = requests.get(
    "https://raw.githubusercontent.com/superpikar/indonesia-geojson/master/indonesia.geojson"
).json()


plot_map_category = go.Figure(
    data=go.Choropleth(
        geojson=geojson,
        locations=data_map_category["provinsi"],  # Spatial coordinates
        featureidkey="properties.state",
        z=data_map_category["po_number"],  # Data to be color-coded
        colorscale="bluered",
        colorbar_title="po_number",
    )
)
plot_map_category.update_geos(fitbounds="locations", visible=False)

plot_map_category
"""

def map_category(list_category, list_bulan, data = data_category):
  #take only sum_category not in list
  data = data.loc[data['sum_category'].isin(list_category)]
  data ['month'] = data['order_date'].str.slice(5,7)
  #gropby data base on provinsi and  agg po_number count
  data_map = data.groupby(['provinsi', 'month']).agg({'po_number' : 'count'})
  data_map.reset_index(inplace = True)


  month = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

  data_map['month'] = data_map['month'].map(month)
  data_map = data_map.loc[data_map['month'].isin(list_bulan)]
  data_map.reset_index(inplace=True, drop = True)
  data_map = data_map.groupby(['provinsi']).agg({'po_number' : 'sum'})
  data_map.reset_index(inplace = True)
    # take geojson
  geojson = requests.get(
    "https://raw.githubusercontent.com/superpikar/indonesia-geojson/master/indonesia.geojson"
    ).json()
  data_map.sort_values(by = 'po_number', ascending = False, inplace = True)
  data_map.reset_index(drop = True, inplace = True)
  data_map.rename(columns = {'po_number' : 'Total Order'},inplace = True)
  
  fig = go.Figure(
      data=go.Choropleth(
          geojson=geojson,
          locations=data_map["provinsi"],  # Spatial coordinates
          featureidkey="properties.state",
          z=data_map["Total Order"],  # Data to be color-coded
          colorscale="Emrld",
          colorbar_title="Total Order"
        )
     )
  #fig.update_layout(template='plotly_dark')
  fig.update_geos(fitbounds="locations", visible=False)
  data_map['Number'] = range(1,len(data_map)+1)
  data_map.set_index('Number', inplace = True)

  return fig, data_map
map_plot_category, data_map_category = map_category(data_category, plot_category)
map_plot_elektronik, data_map_elektronik = map_category(data_category, plot_elektronik)
map_plot_office, data_map_office = map_category(data_category, plot_office)
map_plot_barang, data_map_barang = map_category(data_category, plot_barang)
map_plot_kebutuhan, data_map_kebutuhan = map_category(data_category, plot_kebutuhan_sehari_hari)
map_plot_otomotif, data_map_otomotif = map_category(data_category, plot_otomotif)
map_plot_hiburan, data_map_hiburan = map_category(data_category, plot_hiburan)
map_plot_kesehatan, data_map_kesehatan = map_category(data_category, plot_kesehatan)
map_plot_pertanian, data_map_pertanian = map_category(data_category, plot_pertanian)
map_plot_pendidikan, data_map_pendidikan = map_category(data_category, plot_pendidikan)
map_plot_olahraga, data_map_olahraga = map_category(data_category, plot_olahraga)


"""##Top UMKM"""



#load data_umkm
umkm_data = pd.read_csv('umkm_data_update.csv')

umkm_data = pd.read_csv('data_umkm_per_month.csv')
umkm_data['order_month'] = umkm_data['purchase_order_date'].str.slice(0,7)
umkm_data = umkm_data.groupby(['umkm_name', 'order_month', 'umkm_category']).agg({'total_project_value' : 'sum', 'total_seller_gain' : 'sum', 'total_revenue' : 'sum'})
umkm_data.reset_index(inplace = True)

jumlah_order = data_category.groupby(['umkm_name', 'order_month']).agg({'po_number' : 'count'})
jumlah_order.reset_index(inplace = True)
#join data_umkm and count po_number
data_umkm = pd.merge(umkm_data, jumlah_order, left_on = ['umkm_name', 'order_month'], right_on = ['umkm_name', 'order_month'], how = 'left')
data_umkm

def umkm_top(list_bulan,umkm,data= data_umkm):
  data_top = data.groupby(['umkm_name']).agg({'po_number' : 'sum'})
  data_top.reset_index(inplace = True)
  data_top.sort_values(by = 'po_number', ascending = False,inplace = True)
  data_top = data_top.head(10)

  detail_umkm = data.loc[data['umkm_name'].isin(data_top['umkm_name'])]
  detail_umkm.reset_index(inplace = True, drop = True)
  detail_umkm['month'] = data['order_month'].str.slice(5,7)
  month = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

  detail_umkm['month'] = detail_umkm['month'].map(month)
  detail_umkm = detail_umkm.loc[detail_umkm['month'].isin(list_bulan)]
  detail_umkm = detail_umkm.groupby(['umkm_name','umkm_category']).agg({'total_project_value' : 'sum', 'total_seller_gain' : 'sum', 'total_revenue' : 'sum', 'po_number' : 'sum'})
  detail_umkm.reset_index(inplace = True)
  detail_umkm.sort_values(by = 'po_number', ascending = False, inplace = True)
  detail_umkm.reset_index(inplace = True)
  detail_umkm = detail_umkm.rename(columns = {'umkm_name' : 'UMKM', 'po_number' : 'Total Order'})

  color_map = {'teratai indah' : '#35A29F',
               'INVESTKO MEGAMART/GratisOngkir S&K berlaku' : '#35A29F',
               'KOPEGTEL JAYA' : '#35A29F',
               'KOPEGTEL KANTOR PERUSAHAAN' : '#35A29F',
               'KOPERASI PEGAWAI KERETA API (KOPEKA)': '#35A29F',
               'PRIMASARI PANGAN LESTARI' : '#35A29F',
               'Toko Pananjung' : '#35A29F',
               'Sinar Abadi' : '#35A29F',
               'PT. Visi Duta Mandiri' : '#35A29F',
               'PT Cahaya Subur Sejahtera' : '#35A29F'}
  for key in color_map:
    if key == umkm:
      continue
    color_map[key] = '#DAFFFB'

  fig = px.bar(detail_umkm, x ='UMKM', y = 'Total Order', color = 'UMKM', color_discrete_map=color_map)
  fig.update_xaxes(title = '')
  fig.update_yaxes(title = 'Total Order')

  return fig

def umkm_data_detail(list_bulan, umkm_name, data = data_category, data_umkm = data_umkm):
  data['month'] = data['order_date'].str.slice(5,7)
  month = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

  data['month'] = data['month'].map(month)
  #take only 1 umkm_name
  detail_umkm = data.loc[data['umkm_name'] == umkm_name]
  detail_umkm_month = detail_umkm.loc[detail_umkm['month'].isin(list_bulan)]
  detail_umkm_month.reset_index(inplace = True)
  
  #groupby sum_category and agg sum category this data for pie chart category

  cat_data = detail_umkm_month.groupby('sum_category')['sum_category'].count().rename('Total_order')
  cat_data.sort_values( ascending = False, inplace = True)

  #make pie chart
  fig = px.pie(cat_data,
               values = cat_data,
               names = cat_data.index,
               color = cat_data.index,
               color_discrete_sequence= ['#97FEED', '#35A29F', '#0B666A', '#071952', '#176B87', '#DAFFFB', '#001C30','#64CCC5'],
               hole = 0.5)
  

  #chage type data order date to datetime with format y-m-d
  detail_umkm['order_date'] = pd.to_datetime(detail_umkm['order_date'], format = '%Y-%m-%d')
  detail_umkm.sort_values(by = 'order_date', ascending = False, inplace = True)
  detail_umkm.reset_index(drop = True, inplace = True)

  #take current date
  current_date = datetime.now()
  #make column recency based on current_date - order_date
  detail_umkm['recency'] = (current_date - detail_umkm['order_date'])
  #take last_recency order
  last_recency = detail_umkm.loc[0, 'recency']
  #change output
  last_recency = last_recency.days


  #make variabel for seller_gain, total_project_value, revenue, order
  data_umkm_top = data_umkm.groupby('umkm_name').agg({'po_number' : 'sum'})
  data_umkm_top.reset_index(inplace = True)
  data_umkm_top.sort_values(by ='po_number', ascending = False, inplace = True)
  data_umkm_top.reset_index(inplace = True)
  data_umkm_top = data_umkm_top.head(10)

  data_umkm['month'] = data_umkm['order_month'].str.slice(5,7)
  data_umkm['month'] = data_umkm['month'].map(month)
  umkm_detail = data_umkm.loc[data_umkm['umkm_name'] == umkm_name].reset_index()
  umkm_detail= umkm_detail.loc[umkm_detail['month'].isin(list_bulan)]
  umkm_detail.reset_index(inplace = True)
  
  total_seller_gain = umkm_detail['total_seller_gain'].sum()
  total_project_value = umkm_detail['total_project_value'].sum()
  total_revenue = umkm_detail['total_revenue'].sum()
  total_order = umkm_detail['po_number'].sum()
  
  #take data first order from umkm_name
  first_order = detail_umkm.tail(1)
  first_order.reset_index(drop = True, inplace = True)
  #take recency of first order
  first_order = first_order.loc[0,'recency']
  first_order = first_order.days
  #convert to month
  first_order = round(first_order/30)

  

  #make data_buyer
  data_buyer = detail_umkm_month.groupby(['buyer_name', 'buyer_provinsi', 'sum_category']).agg({'po_number' : 'count'})
  data_buyer.reset_index(inplace = True)
  data_buyer.sort_values(by = 'po_number', ascending = False, inplace = True)
  data_buyer.reset_index(drop = True, inplace = True)
  data_buyer['Number'] = range(1,len(data_buyer)+1)
  data_buyer.set_index('Number', inplace = True)


               
  return last_recency,total_seller_gain,total_project_value, total_revenue, total_order,first_order,data_buyer, fig



"""## UMKM Lower"""

def umkm_detail_lower(data_umkm, data_category):
  # drop outlier with zscores method
  data_umkm.fillna(0, inplace=True)
  z_scores = np.abs(zscore(data_umkm['po_number']))
  thereshold = 0.1
  data_umkm_clean = data_umkm[z_scores < thereshold]
  #find mean with data that clean with zscore
  mean_order = round(data_umkm_clean['po_number'].mean())
  #make variabel umkm and umkm_category total_order
  data_umkm_lower = data_category.groupby(['umkm_name', 'umkm_category']).agg({'po_number' : 'count'}).reset_index()
  #add column type_order with condition if total_order > mean 'above_mean' else 'bellow mean'
  data_umkm_lower['type_order'] = data_umkm_lower.apply(lambda row : 'Above_mean' if row['po_number']> mean_order else 'Bellow_mean', axis = 1)
  #add umkm_lower for data column typeorder = 'bellow mean'
  data_umkm_lower = data_umkm_lower.loc[data_umkm_lower['type_order'] == 'Bellow_mean']
  data_detail_umkm_lower = data_category.loc[data_category['umkm_name'].isin(data_umkm_lower['umkm_name'])]

  data_bar = data_detail_umkm_lower.groupby(['umkm_category', 'sum_category']).agg({'po_number' : 'count'})
  data_bar.reset_index(inplace = True)
  data_bar.sort_values(by = 'po_number', ascending = True)

  color_category = {'Barang_jasa dan Persewaan' :'#38A3A5',
                    'Elektronik dan IT' : '#80ED99',
                    'Kebutuhan Sehari-hari' : '#57CC99',
                    'Kesehatan/Kecantikan/Fashion' : '#97FEED',
                    'Office & Stationery': '#80ED99',
                    'Otomotif' : '#B4FE98',
                    'Hiburan' :'#22577A',
                    'Pertanian & Pertenakan' : '#018383',
                    'Pendidikan dan Pelatihan': '#42E6A4',
                    'Olahraga' : '#C6FFC1',
                    }



  cat_data = data_category.loc[data_category['umkm_name'].isin(data_umkm_lower['umkm_name'])]
  cat_data = data_category.groupby('sum_category')['sum_category'].count().rename('Total_order')
  cat_data.sort_values( ascending = False, inplace = True)

  
  box_plot = px.box(data_umkm_lower, x = 'umkm_category',  y = 'po_number', points = 'all', hover_data = ['umkm_name'], color= 'umkm_category',color_discrete_sequence=['#38A3A5','#57CC99', '#80ED99', '#B4FE98' ] )
  box_plot.update_yaxes(title = 'Total Order')
  box_plot.update_xaxes(title = 'UMKM Category')

  

  fig_pie = px.pie(cat_data,
               values = cat_data,
               names = cat_data.index,
               color = cat_data.index,
               color_discrete_map = color_category,
               hole = 0.5)
  

  plot_bar = px.bar(data_bar, x = 'umkm_category', y = 'po_number', color = 'sum_category', color_discrete_map= color_category)
  for trace in plot_bar.data:
    trace.update(showlegend=False)
  category_order = ['Mikro', 'Kecil', 'Menengah', 'Besar', 'Swasta']
  plot_bar.update_xaxes(categoryorder = 'array', title = 'UMKM Category')
  plot_bar.update_yaxes(title = 'Total Order')

  data_detail_umkm_lower['order_date'] = pd.to_datetime(data_detail_umkm_lower['order_date'], format = '%Y-%m-%d')
  data_detail_umkm_lower.sort_values(by = 'order_date', ascending = False, inplace = True)
  data_detail_umkm_lower.reset_index(inplace = True)

  current_date = datetime.now()
  data_detail_umkm_lower['recency'] = (current_date - data_detail_umkm_lower['order_date'])
  data_last_umkm_lower = data_detail_umkm_lower.groupby(['umkm_name', 'umkm_category', 'buyer_name','buyer_provinsi', 'buyer_kota', 'order_date', 'provinsi', 'kota']).agg({'recency' : 'min'})
  data_last_umkm_lower.reset_index(inplace = True)
  data_last_umkm_lower.sort_values(by = ['umkm_name', 'recency'], ascending = [True, True], inplace = True)
  data_last_umkm_lower = data_last_umkm_lower.groupby('umkm_name').first().reset_index()

  data_first_order = data_detail_umkm_lower.groupby(['umkm_name', 'order_month']).agg({'recency' : 'max'}).reset_index()
  data_first_order.sort_values(by = ['umkm_name', 'recency'], ascending = [True, False])
  data_first_order = data_first_order.groupby('umkm_name').first().reset_index()
  data_first_order.rename(columns = {'order_month':'first_month_order', 'recency' : 'first_recency_order'}, inplace = True)

  table_umkm_lower = pd.merge(data_last_umkm_lower, data_first_order, left_on = 'umkm_name', right_on = 'umkm_name', how = 'left')
  table_umkm_lower.rename(columns = {'umkm_name' : 'UMKM', 'umkm_category': 'Category UMKM', 'buyer_name' : 'Last Buyer Name', 'buyer_provinsi' : 'Last Buyer Provinsi', 'buyer_kota' :'Last Buyer Kota', 'provinsi' : 'Provinsi UMKM', 'kota' : 'Kota UMKM', 'recency' : 'Last Recency', 'first_month_order': 'First Order Month', 'first_recency_order' : 'First Order Recency'}, inplace = True)
  table_umkm_lower['Last Recency'] = table_umkm_lower['Last Recency'].dt.days
  table_umkm_lower['First Order Recency'] = table_umkm_lower['First Order Recency'].dt.days
  table_umkm_lower.sort_values(by = 'Last Recency', ascending = False, inplace = True)
  table_umkm_lower.reset_index(drop =True, inplace = True)
  table_umkm_lower['Number'] = range(1,len(table_umkm_lower)+1)
  table_umkm_lower.set_index('Number', inplace = True)
  
  
  return table_umkm_lower, box_plot,plot_bar,fig_pie

table_umkm_lower, box_plot_umkm_lower,plot_bar_umkm_loweer,fig_pie_umkm_lower = umkm_detail_lower(data_umkm, data_category)

data_update_rfm = pd.read_csv('data_update_rfm.csv')
data_update_rfm.sort_values(by = 'buyer_name')

# replace name_provinsi to adapt geojson indonesia
data_update_rfm = data_update_rfm.replace('KALIMANTAN TIMUR', 'Kalimantan Timur')
data_update_rfm = data_update_rfm.replace('DKI JAKARTA', 'Jakarta Raya')
data_update_rfm = data_update_rfm.replace('BENGKULU', 'Bengkulu')
data_update_rfm = data_update_rfm.replace('KALIMANTAN TIMUR', 'Sumatera Selatan')
data_update_rfm = data_update_rfm.replace('SUMATERA SELATAN', 'Kalimantan Timur')
data_update_rfm = data_update_rfm.replace('MALUKU', 'Maluku')
data_update_rfm = data_update_rfm.replace('RIAU', 'Riau')
data_update_rfm = data_update_rfm.replace('SULAWESI SELATAN', 'Sulawesi Selatan')
data_update_rfm = data_update_rfm.replace('KALIMANTAN BARAT', 'Kalimantan Barat')
data_update_rfm = data_update_rfm.replace('JAWA TIMUR', 'Jawa Timur')
data_update_rfm = data_update_rfm.replace('SUMATERA UTARA', 'Sumatera Utara')
data_update_rfm = data_update_rfm.replace('BALI', 'Bali')
data_update_rfm = data_update_rfm.replace('JAWA TENGAH', 'Jawa Tengah')
data_update_rfm = data_update_rfm.replace('JAWA BARAT', 'Jawa Barat')
data_update_rfm = data_update_rfm.replace('ACEH', 'Aceh')
data_update_rfm = data_update_rfm.replace('BANTEN', 'Banten')
data_update_rfm = data_update_rfm.replace('KEPULAUAN RIAU', 'Kepulauan Riau')
data_update_rfm = data_update_rfm.replace('PAPUA', 'Papua')
data_update_rfm = data_update_rfm.replace('PAPUA BARAT', 'Papua Barat')
data_update_rfm = data_update_rfm.replace('SULAWESI TENGAH', 'Sulawesi Tengah')
data_update_rfm = data_update_rfm.replace('LAMPUNG', 'Lampung')
data_update_rfm = data_update_rfm.replace('KEPULAUAN BANGKA BELITUNG', 'Bangka-Belitung')
data_update_rfm = data_update_rfm.replace('SUMATERA BARAT', 'Sumatera Barat')
data_update_rfm = data_update_rfm.replace('NUSA TENGGARA BARAT', 'Nusa Tenggara Barat')
data_update_rfm = data_update_rfm.replace('DI YOGYAKARTA', 'Yogyakarta')
data_update_rfm = data_update_rfm.replace('SULAWESI UTARA', 'Sulawesi Utara')
data_update_rfm = data_update_rfm.replace('JAMBI', 'Jambi')
data_update_rfm = data_update_rfm.replace('GORONTALO', 'Gorontalo')
data_update_rfm = data_update_rfm.replace('KALIMANTAN TENGAH', 'Kalimantan Tengah')
data_update_rfm = data_update_rfm.replace('SULAWESI TENGGARA', 'Sulawesi Tenggara')
data_update_rfm = data_update_rfm.replace('KALIMANTAN UTARA', 'Kalimantan Utara')
data_update_rfm = data_update_rfm.replace('KALIMANTAN SELATAN', 'Kalimantan Selatan')
data_update_rfm = data_update_rfm.replace('NUSA TENGGARA TIMUR', 'Nusa Tenggara Timur')
data_update_rfm = data_update_rfm.replace('MALUKU UTARA', 'Maluku Utara')
data_update_rfm = data_update_rfm.replace('D.I. Aceh', 'Aceh')
data_update_rfm = data_update_rfm.replace('Papua Barat', 'Papua')
data_update_rfm = data_update_rfm.replace('D.I. Yogyakarta', 'Yogyakarta')
data_update_rfm = data_update_rfm.replace('Papua Selatan', 'Papua')
data_update_rfm ['order_month'] = data_update_rfm['order_date'].str.slice(0,7)


def map_cluster_rfm(cluster, data = data_update_rfm):
  #take only sum_category not in list
  data = data.loc[data['Cluster_Id'] == cluster]
  data = data.groupby(['provinsi', 'buyer_name']).agg({'Cluster_Id' : 'count'})
  data.reset_index(inplace = True)

  #gropby data base on provinsi and  agg po_number count
  data_map = data.groupby(['provinsi']).agg({'buyer_name' : 'count'})
  data_map.reset_index(inplace = True)

    # take geojson
  geojson = requests.get(
    "https://raw.githubusercontent.com/superpikar/indonesia-geojson/master/indonesia.geojson"
    ).json()
  data_map.sort_values(by = 'buyer_name', ascending = False, inplace = True)
  data_map.reset_index(drop = True, inplace = True)
  data_map.rename(columns = {'buyer_name' : 'Total'},inplace = True)

  fig = go.Figure(
      data=go.Choropleth(
          geojson=geojson,
          locations=data_map["provinsi"],  # Spatial coordinates
          featureidkey="properties.state",
          z=data_map["Total"],  # Data to be color-coded
          colorscale="Emrld",
          colorbar_title="Total"
        )
     )
  #fig.update_layout(template='plotly_dark')
  fig.update_geos(fitbounds="locations", visible=False)
  data_map['Number'] = range(1,len(data_map)+1)
  data_map.set_index('Number', inplace = True)

  return fig, data_map

def category_cluster_rfm(cluster, data= data_update_rfm):
  data = data.loc[data['Cluster_Id']== cluster]
  data = data.groupby(['sum_category', 'buyer_name']).agg({'Cluster_Id' : 'count'})
  data.reset_index(inplace = True)
  data = data.groupby(['sum_category']).agg({'buyer_name' : 'count'})
  data.sort_values(by = 'buyer_name', ascending = False, inplace = True)
  data.reset_index(inplace = True)
  fig = px.bar(data, x = 'sum_category', y = 'buyer_name', color_discrete_sequence=['#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F'])
  return fig

def cluster_top_umkm(cluster, data = data_update_rfm):
  data_top = data.groupby(['umkm_name']).agg({'po_number' : 'count'})
  data_top.reset_index(inplace = True)
  data_top.sort_values(by = 'po_number', ascending = False, inplace = True)
  data_top.reset_index(drop = True, inplace = True)
  data_top = data_top.head(10)

  data_umkm = data.loc[data['umkm_name'].isin(data_top['umkm_name'])]
  data_umkm = data_umkm.loc[data_umkm['Cluster_Id'] == cluster]
  data_umkm = data_umkm.groupby(['umkm_name', 'buyer_name']).agg({'Cluster_Id' : 'count'})
  data_umkm.reset_index(inplace = True)
  data_umkm = data_umkm.groupby(['umkm_name']).agg({'buyer_name' : 'count'})
  data_umkm.reset_index(inplace = True)
  data_umkm.sort_values(by = 'buyer_name', ascending = False, inplace = True)



  fig = px.bar(data_umkm, x = 'umkm_name', y = 'buyer_name',color_discrete_sequence=['#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F','#35A29F'])


  return fig

def cluster_lower(cluster, data = data_update_rfm):
  data_umkm = data.groupby(['umkm_name']).agg({'po_number' : 'count'})
  data_umkm.reset_index(inplace = True)

  # drop outlier with zscores method
  z_scores = np.abs(zscore(data_umkm['po_number']))
  thereshold = 0.1
  data_umkm_clean = data_umkm[z_scores < thereshold]
  #find mean with data that clean with zscore
  mean_order = round(data_umkm_clean['po_number'].mean())
  #make variabel umkm and umkm_category total_order
  data_umkm_lower = data.groupby(['umkm_name']).agg({'po_number' : 'count'}).reset_index()
  #add column type_order with condition if total_order > mean 'above_mean' else 'bellow mean'
  data_umkm_lower['type_order'] = data_umkm_lower.apply(lambda row : 'Above_mean' if row['po_number']>= mean_order else 'Bellow_mean', axis = 1)
  #add umkm_lower for data column typeorder = 'bellow mean'
  data_umkm_lower = data_umkm_lower.loc[data_umkm_lower['type_order'] == 'Bellow_mean']

  data = data.loc[data['umkm_name'].isin(data_umkm_lower['umkm_name'])]
  data = data.groupby(['buyer_name', 'umkm_name', 'Cluster_Id']).size().reset_index(name = 'count')
  data = data.groupby(['Cluster_Id']).agg({'buyer_name' : 'count'})
  data.reset_index(inplace = True)
  data.replace(1, 'Cluster 1', inplace = True)
  data.replace(2, 'Cluster 2', inplace = True)
  data.replace(3, 'Cluster 3', inplace = True)
  data.replace(4, 'Cluster 4', inplace = True)

  if cluster == 1 :
    pull = [0.2,0,0,0]
  elif cluster == 2:
    pull = [0,0.2,0,0]
  elif cluster == 3:
    pull = [0,0,0.2,0]
  elif cluster == 4:
    pull = [0,0,0,0.2]


  fig = px.pie(data,
               values = data['buyer_name'],
               names = data['Cluster_Id'],
               color = data['Cluster_Id'],
               color_discrete_sequence=['#35A29F', '#22577A', '#57CC99', '#B4FE98'],
               hole = 0.5)
  fig.update_traces( pull = pull)


  return fig

def buyer_top_lower(cluster, data = data_update_rfm):
  data_top = data.groupby(['umkm_name']).agg({'po_number' : 'count'})
  data_top.reset_index(inplace = True)
  data_top.sort_values(by = 'po_number', ascending = False, inplace = True)
  data_top.reset_index(drop = True, inplace = True)
  data_top = data_top.head(10)
  data_top_umkm = data.loc[data['umkm_name'].isin(data_top['umkm_name'])]


  data_umkm = data.groupby(['umkm_name']).agg({'po_number' : 'count'})
  data_umkm.reset_index(inplace = True)

  # drop outlier with zscores method
  z_scores = np.abs(zscore(data_umkm['po_number']))
  thereshold = 0.1
  data_umkm_clean = data_umkm[z_scores < thereshold]
  #find mean with data that clean with zscore
  mean_order = round(data_umkm_clean['po_number'].mean())
  #make variabel umkm and umkm_category total_order
  data_umkm_lower = data.groupby(['umkm_name']).agg({'po_number' : 'count'}).reset_index()
  #add column type_order with condition if total_order > mean 'above_mean' else 'bellow mean'
  data_umkm_lower['type_order'] = data_umkm_lower.apply(lambda row : 'Above_mean' if row['po_number']>= mean_order else 'Bellow_mean', axis = 1)
  #add umkm_lower for data column typeorder = 'bellow mean'
  data_umkm_lower = data_umkm_lower.loc[data_umkm_lower['type_order'] == 'Bellow_mean']
  umkm_lower = data.loc[data['umkm_name'].isin(data_umkm_lower['umkm_name'])]

  data_buyer = data.groupby(['buyer_name', 'umkm_name', 'Cluster_Id']).size().reset_index(name = 'count')
  #data_buyer['buyer_top_lower'] = data_buyer.loc[data_buyer['buyer_name'].isin(data_top_umkm['buyer_name']) & data_buyer['buyer_name'].isin(umkm_lower['buyer_name'])] else 'False', axis = 1)
  data_buyer['buyer_top_lower'] =( data_buyer['buyer_name'].isin(data_top_umkm['buyer_name']) & data_buyer['buyer_name'].isin(umkm_lower['buyer_name'])).map({True: 'True', False: 'False'})

  data_buyer = data_buyer.loc[data_buyer['Cluster_Id'] == cluster]
  data_buyer = data_buyer.groupby(['buyer_top_lower']).size().reset_index(name = 'count')


  fig = px.bar(data_buyer, x = 'buyer_top_lower', y = 'count', color_discrete_sequence=['#35A29F', '#35A29F'])
  return fig

def data_buyer_cluster(cluster, data = data_update_rfm):
  nama_buyer = data.groupby(['buyer_name', 'Cluster_Id']).size().reset_index(name = 'count')
  order_buyer = data.groupby('buyer_name').agg({'po_number' : 'count'}).reset_index()

  data['order_date'] = pd.to_datetime(data['order_date'], format = '%Y-%m-%d')
  data.sort_values(by = 'order_date', ascending = False, inplace = True)
  data.reset_index(drop = True, inplace = True)

  current_date = datetime.now()
  data['recency'] = (current_date - data['order_date'])
  data_last_order = data.groupby(['buyer_name', 'umkm_name', 'buyer_provinsi', 'provinsi', 'order_date','sum_category']).agg({'recency' : 'min'}).reset_index()
  data_last_order.sort_values(by = ['buyer_name', 'recency'], ascending = [True, True], inplace = True)
  data_last_order.reset_index(drop = True, inplace = True)
  data_last_order = data_last_order.groupby('buyer_name').first().reset_index()
  data_last_order.rename(columns = {'umkm_name' : 'umkm_name_last_order', 'provinsi' : 'umkm_provinsi_last_order', 'order_date' : 'last_order_date', 'sum_category' : 'last_category_order', 'recency' :'last_order_recency'}, inplace = True)

  data_first_order = data.groupby(['buyer_name', 'umkm_name']).agg({'recency': 'max'}).reset_index()
  data_first_order.sort_values(by = ['buyer_name', 'recency'], ascending = [True, False], inplace = True)
  data_first_order.reset_index(drop = True, inplace = True)
  data_first_order = data_first_order.groupby('buyer_name').first().reset_index()
  data_first_order.rename(columns = {'umkm_name' : 'umkm_name_first_order', 'recency' : 'first_order'}, inplace = True)


  data_buyer_category = data.groupby(['buyer_name', 'sum_category']).agg({'po_number' : 'count'})
  data_buyer_category.reset_index(inplace = True)
  data_buyer_category = data_buyer_category.pivot_table(index = 'buyer_name', columns = 'sum_category', values = 'po_number', aggfunc = 'sum', fill_value = 0)
  data_buyer_category.reset_index(inplace = True)

  nama_buyer.drop('count',axis = 1, inplace = True)
  data_buyer = pd.merge(nama_buyer, order_buyer, left_on = 'buyer_name',right_on = 'buyer_name', how = 'left')
  data_buyer = pd.merge(data_buyer, data_last_order, left_on = 'buyer_name', right_on = 'buyer_name', how = 'left')
  data_buyer = pd.merge(data_buyer, data_first_order, left_on = 'buyer_name', right_on = 'buyer_name', how = 'left')
  data_buyer = pd.merge(data_buyer, data_buyer_category, left_on = 'buyer_name', right_on = 'buyer_name', how = 'left')
  data_buyer['last_order_recency'] = data_buyer['last_order_recency'].dt.days
  data_buyer['first_order'] = data_buyer['first_order'].dt.days

  return data_buyer
  




