import streamlit as st
from project_telkom_padi_umkm import plot_category_fav, line_plot_category
from project_telkom_padi_umkm import table_umkm_lower, box_plot_umkm_lower
from project_telkom_padi_umkm import plot_bar_umkm_loweer,fig_pie_umkm_lower, table_umkm_lower, line_plot_elektronik,line_plot_office, line_plot_barang,line_plot_kebutuhan,line_plot_otomotif,line_plot_hiburan
from project_telkom_padi_umkm import line_plot_kesehatan,line_plot_pertanian,line_plot_pendidikan,line_plot_olahraga, plot_top_category, map_category,umkm_top, umkm_data_detail,map_cluster_rfm, category_cluster_rfm, cluster_top_umkm,cluster_lower, buyer_top_lower, data_buyer_cluster
import humanize

st.set_page_config(page_title="PadiUMKM Telkom", page_icon=":guardsman:", layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True) 

# Add margin between components
st.markdown("""<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>""",unsafe_allow_html=True)
st.markdown("""<style>div.row-widget.stRadio > div{margin-left:20px;margin-right:20px;}</style><br>""",unsafe_allow_html=True)

def main():
    st.sidebar.title("Navigation")
    pages = ["Category PadiUMKM", "Top UMKM", "Lower UMKM", "Clustering"]
    selection = st.sidebar.radio("Go to", pages)

    if selection == "Category PadiUMKM":
        # row 1
        #st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Dashbord PadiUMKM Telkom</b></h1>", unsafe_allow_html=True)
        filter1, filter2 = st.columns(2)
        with filter1:
            option = st.selectbox('Choose Category',
                                  ('All Category', 'Office & Stationery', 'Kebutuhan Sehari-hari', 'Barang,Jasa dan Persewaan', 'Elektronik dan IT', 'Kesehatan/Kecantikan/Fashion', 'Hiburan', 'Otomotif', 'Pertanian & Pertenakan', 'Olahraga', 'Pendidikan dan Pelatihan'))
        with filter2:
            option_month = st.multiselect('Choose Month',['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Desember'], default=['January', 'February', 'March', 'April', 'May'])

        def filter_category(name,column_chart_category, map_plot,  data_map, line_plot):
            st.markdown(f"<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Jumlah Order {name} Category</b></h1>", unsafe_allow_html=True)
            st.plotly_chart(column_chart_category, use_container_width= True)
            st.markdown(f"<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Sales {name} of Province</b></h1>", unsafe_allow_html=True)
            col1, col2 = st.columns((7,3))
            #row 2 column 1
            with col1 :
                st.plotly_chart(map_plot, use_container_width = True)
            #row 2 column 2
            with col2:
                st.dataframe(data_map,  width=400, height=400)
            #row 3
            st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Sales All Category in 2023</b></h1>", unsafe_allow_html=True)
            st.plotly_chart(line_plot, use_container_width= True)
        
        if option == 'All Category':
            list_all_category = ['Elektronik dan IT', 'Office & Stationery', 'Barang,Jasa dan Persewaan', 'Kebutuhan Sehari-hari', 'Otomotif', 'Hiburan', 'Kesehatan/Kecantikan/Fashion','Pertanian & Pertenakan', 'Pendidikan dan Pelatihan', 'Olahraga']
            column_chart_category = plot_top_category(list_all_category,option_month)
            map_plot_category, data_map_category = map_category(list_all_category, option_month)
            filter_category(option, column_chart_category, map_plot_category, data_map_category, line_plot_category)

        elif option == 'Office & Stationery' :
           list_office = [option]
           column_chart_office = plot_top_category(list_office, option_month)
           map_plot_office, data_map_office  = map_category(list_office, option_month)
           filter_category('Office Stationery',column_chart_office, map_plot_office,data_map_office, line_plot_office)

        elif option == 'Kebutuhan Sehari-hari' :
            list_kebutuhan = [option]
            column_chart_kebutuhan = plot_top_category(list_kebutuhan, option_month)
            map_plot_kebutuhan, data_map_kebutuhan = map_category(list_kebutuhan, option_month)
            filter_category('Kebutuhan Sehari-hari', column_chart_kebutuhan,map_plot_kebutuhan,data_map_kebutuhan, line_plot_kebutuhan)

        elif option == 'Barang,Jasa dan Persewaan':
            list_barang = [option]
            column_chart_barang = plot_top_category(list_barang, option_month)
            map_plot_barang, data_map_barang = map_category(list_barang, option_month)
            filter_category('Barang, Jasa dan Persewaan',column_chart_barang, map_plot_barang,data_map_barang, line_plot_barang)

        elif option == 'Elektronik dan IT':
            list_elektronik = [option]
            column_chart_elektronik = plot_top_category(list_elektronik, option_month)
            map_plot_elektronik, data_map_elektronik = map_category(list_elektronik, option_month)
            filter_category('Elektronik & IT',column_chart_elektronik, map_plot_elektronik,data_map_elektronik, line_plot_elektronik)

        elif option == 'Kesehatan/Kecantikan/Fashion':
            list_kesehatan = [option]
            column_chart_kesehatan= plot_top_category(list_kesehatan, option_month)
            map_plot_kesehatan, data_map_kesehatan = map_category(list_kesehatan, option_month)
            filter_category('Kesehatan, Kecantikan & Fashion', column_chart_kesehatan, map_plot_kesehatan,data_map_kesehatan, line_plot_kesehatan)

        elif option == 'Hiburan':
            list_hiburan = [option]
            column_chart_hiburan = plot_top_category(list_hiburan, option_month)
            map_plot_hiburan, data_map_hiburan = map_category(list_hiburan, option_month)
            filter_category('Hiburan', column_chart_hiburan, map_plot_hiburan,data_map_hiburan, line_plot_hiburan)

        elif option == 'Otomotif':
            list_otomotif = [option]
            column_chart_otomotif = plot_top_category(list_otomotif, option_month)
            map_plot_otomotif, data_map_otomotif = map_category(list_otomotif, option_month)
            filter_category('Otomotif',column_chart_otomotif, map_plot_otomotif,data_map_otomotif, line_plot_otomotif)

        elif option == 'Pertanian & Pertenakan':
            list_pertanian = [option]
            column_chart_pertanian = plot_top_category(list_pertanian, option_month)
            map_plot_pertanian, data_map_pertanian = map_category(list_pertanian, option_month)
            filter_category('Pertanian & Perternakan',column_chart_pertanian, map_plot_pertanian,data_map_pertanian, line_plot_pertanian)

        elif option == 'Olahraga':
            list_olahraga = [option]
            column_chart_olahraga = plot_top_category(list_olahraga, option_month)
            map_plot_olahraga, data_map_olahraga = map_category(list_olahraga, option_month)
            filter_category('Olahraga',column_chart_olahraga, map_plot_olahraga,data_map_olahraga, line_plot_olahraga)

        elif option == 'Pendidikan dan Pelatihan':
            list_pendidikan = [option]
            column_chart_pendidikan = plot_top_category(list_pendidikan, option_month)
            map_plot_pendidikan, data_map_pendidikan = map_category(list_pendidikan, option_month)
            filter_category('Pendidikan & Pelatihan',column_chart_pendidikan, map_plot_pendidikan,data_map_pendidikan, line_plot_pendidikan)
        

            
    
    elif selection == "Top UMKM":
        #row 1
        st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Top UMKM</b></h1>", unsafe_allow_html=True)
        filter1, filter2 = st.columns(2)
        with filter1:
            option = st.selectbox('Choose UMKM',
                                  ('teratai indah', 'PT Cahaya Subur Sejahtera', 'KOPEGTEL KANTOR PERUSAHAAN', 'INVESTKO MEGAMART/GratisOngkir S&K berlaku', 'KOPERASI PEGAWAI KERETA API (KOPEKA)', 'Toko Pananjung', 'Sinar Abadi', 'PRIMASARI PANGAN LESTARI', 'KOPEGTEL JAYA', 'PT. Visi Duta Mandiri'))
        with filter2:
            option_month = st.multiselect('Choose Month',['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Desember'])

        
        def filter_top_umkm(plot_top_umkm, total_seler_gain, total_project_value, total_revenue, total_order, first_order, last_recency, data_buyer, pie_chart):
            col1,col2, col3 = st.columns((2,6,2))
            #row 3 column 1
            col1.metric("Seller Gain", f"{humanize.intword(total_seler_gain)}")
            #row 3 column 2
            col1.metric('Project Value', f"{humanize.intword(total_project_value)}")
            #row 3 column 3
            col1.metric('Net Revenue', f"{humanize.intword(total_revenue)}")

            with col2:
                st.plotly_chart(plot_top_umkm, use_container_width= True)

            
            col3.metric('Total Order', f"{humanize.intword(total_order)} Orders")
            col3.metric('First Order', f"{first_order} months ago")
            col3.metric('Last Order', f"{last_recency} days ago")
            

            # make 2 column for row 5
            st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Data Buyer and Presentase Category</b></h1>", unsafe_allow_html=True)
            col1_4,col2_4= st.columns((4,6))
            # row 5 column 1
            with col1_4 :
                st.dataframe(data_buyer, width = 500, height = 400)
            # row 5 column 1
            with col2_4:
                st.plotly_chart(pie_chart, use_container_width= True)

        
        if option == 'teratai indah':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)

        elif option == 'PT Cahaya Subur Sejahtera':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)

        elif option == 'KOPEGTEL KANTOR PERUSAHAAN':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)
        
        elif option == 'INVESTKO MEGAMART/GratisOngkir S&K berlaku':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)
    
        elif option == 'KOPERASI PEGAWAI KERETA API (KOPEKA)':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)
        
        elif option == 'Toko Pananjung':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)
        
        elif option == 'Sinar Abadi':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)
        
        elif option == 'PRIMASARI PANGAN LESTARI':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)     
        
        elif option == 'KOPEGTEL JAYA':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)
        
        elif option == 'PT. Visi Duta Mandiri':
            plot_top_umkm = umkm_top(option_month,option)
            last_recency_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm, total_order_umkm, first_order_umkm, data_buyer_umkm, pie_chart_umkm =umkm_data_detail(option_month, option)
            filter_top_umkm(plot_top_umkm, total_seller_gain_umkm, total_project_value_umkm, total_revenue_umkm,total_order_umkm, first_order_umkm, last_recency_umkm, data_buyer_umkm, pie_chart_umkm)
        
    elif selection == 'Lower UMKM':
        st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>UMKM Bellow Average</b></h1>", unsafe_allow_html=True)
        st.plotly_chart(box_plot_umkm_lower, use_container_width= True)
        st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Category Composition</b></h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(plot_bar_umkm_loweer, use_container_width= True)
        with col2:
            st.plotly_chart(fig_pie_umkm_lower, use_container_width=True)
        st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Data UMKM</b></h1>", unsafe_allow_html=True)
        st.dataframe(table_umkm_lower, width=1300, height=400)

    elif selection =='Clustering' :
        option = st.selectbox('Choose Cluster',
                                  ('Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'))
        st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Clusterin RFM</b></h1>", unsafe_allow_html=True)
        
        
        def filter_clustering(cluster_map, data_map, cluster_category, cluster_top_umkm, cluster_lower, buyer_top_lower, data_cluster_buyer):
            col1, col2 = st.columns((7,3))
            with col1:
                st.plotly_chart(cluster_map, use_container_width= True)
            with col2:
                st.dataframe(data_map, width= 400, height= 400)
            
            st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Total Buyer Based on Category and Buyer in Top UMKM</b></h1>", unsafe_allow_html=True)
            col1_2, col2_2 = st.columns(2)
            with col1_2:
                st.plotly_chart(cluster_category, use_container_width=True)
            with col2_2:
                st.plotly_chart(cluster_top_umkm, use_container_width=True)

            st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Composition Clustering Buyer and Buyer in Top and Bellow Average</b></h1>", unsafe_allow_html=True)
            col1_3,col2_3 = st.columns(2)
            with col1_3:
                st.plotly_chart(cluster_lower, use_container_width=True)
            with col2_3:
                st.plotly_chart(buyer_top_lower, use_container_width=True)

            st.markdown("<h1 style='text-align: center; font-size: 20px; font-family: Arial;'><b>Data Buyer</b></h1>", unsafe_allow_html=True)
            st.dataframe(data_cluster_buyer, height= 500, use_container_width= True)
        

        if option == 'Cluster 1':
            cluster = 1 
            map, data_map = map_cluster_rfm(cluster)
            category_cluster = category_cluster_rfm(cluster)
            cluster_top = cluster_top_umkm(cluster)
            pie_chart_lower = cluster_lower(cluster)
            composition_buyer_top_lower = buyer_top_lower(cluster)
            table_buyer = data_buyer_cluster(cluster)
            filter_clustering(map,data_map,category_cluster,cluster_top,pie_chart_lower, composition_buyer_top_lower, table_buyer)
        
        elif option == 'Cluster 2':
            cluster = 2
            map, data_map = map_cluster_rfm(cluster)
            category_cluster = category_cluster_rfm(cluster)
            cluster_top = cluster_top_umkm(cluster)
            pie_chart_lower = cluster_lower(cluster)
            composition_buyer_top_lower = buyer_top_lower(cluster)
            table_buyer = data_buyer_cluster(cluster)
            filter_clustering(map,data_map,category_cluster,cluster_top,pie_chart_lower, composition_buyer_top_lower, table_buyer)
        
        elif option == 'Cluster 3':
            cluster = 3
            map, data_map = map_cluster_rfm(cluster)
            category_cluster = category_cluster_rfm(cluster)
            cluster_top = cluster_top_umkm(cluster)
            pie_chart_lower = cluster_lower(cluster)
            composition_buyer_top_lower = buyer_top_lower(cluster)
            table_buyer = data_buyer_cluster(cluster)
            filter_clustering(map,data_map,category_cluster,cluster_top,pie_chart_lower, composition_buyer_top_lower, table_buyer)
        
        elif option == 'Cluster 4':
            cluster = 4
            map, data_map = map_cluster_rfm(cluster)
            category_cluster = category_cluster_rfm(cluster)
            cluster_top = cluster_top_umkm(cluster)
            pie_chart_lower = cluster_lower(cluster)
            composition_buyer_top_lower = buyer_top_lower(cluster)
            table_buyer = data_buyer_cluster(cluster)
            filter_clustering(map,data_map,category_cluster,cluster_top,pie_chart_lower, composition_buyer_top_lower, table_buyer)





if __name__ == '__main__':
    main()