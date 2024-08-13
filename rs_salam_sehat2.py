import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

#visualisasi
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="RS Salam Sehat",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.big-font {
    font-size:38px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Preview Dashboard Analisis Omset dan Sebaran Pasien RS Salam Sehat</h1>", unsafe_allow_html=True)
st.image("rs33b.png")

st.markdown("--------")

st.markdown('<p class="big-font">Kompleksitas Bisnis Rumah Sakit</p>', unsafe_allow_html=True)
st.subheader(''':red[*Apakah Owner dan Direktur RS Bingung dan Kesulitan melihat Progres Bisnis RS ??*]''')
st.subheader(''':red[*Apa yang harus dilakukan ?? Mulai dari mana ??*]''')
st.subheader(''':yellow-background[*.....Sementara Biaya Rutin Operasional, Angsuran Alkes dan Biaya Lainnya harus tetap keluar dan menggerus Cash flow RS*]''')


with st.expander("Lingkup dan Penerapan Data Analis untuk Bisnis Rumah Sakit"):
    col5az, col6az = st.columns(2)
    with col5az:
        st.subheader("Lingkup Bisnis Rumah Sakit")
        st.image("ba1.png")
        st.write("*Kompleksitas Bisnis RS secara umum tidak dimiliki oleh bentuk bisnis lainnya karena di dalam RS terdapat 3 Bisnis sekaligus yaitu Jasa, Dagang dan Industri*")
    with col6az:
        st.subheader("Penerapan Data Analisis untuk Bisnis Rumah Sakit")
        st.image("ba2.png")
        st.write("*Pasien yang datang harus dapat dipetakan dengan baik terkait Poli/Unit dan Dokter yang dikunjungi serta Pembayaran yang dilakukan menggunakan Penjamin apa, sehingga dari pemetaan/deskriptif analitik tersebut dapat diambil Business Insight dalam pengambilan keputusan oleh Manajemen*")


st.markdown("--------")

## Read Data
#conn = st.connection("gsheet", type=GSheetsConnection)

#df2 = conn.read(
    #spreadsheet = st.secrets.gsheet_omshosp["spreadsheet"],
    #worksheet = st.secrets.gsheet_omshosp["worksheet"]
   # )


#df4 = df2.tail(5)
#st.markdown("*Preview Data Transaksi Pasien*")
#st.dataframe(df4)
#st.markdown(
                #"""
                #<style>
                #[data-testid="stElementToolbar"] {
                    #display: none;
                #}
                #</style>
                #""",
                #unsafe_allow_html=True
           # )



# Memisahkan layar menjadi 2 kolom
#col1, col2 = st.columns(2)

#fig2 = px.bar(df2['Penanggung'].value_counts())

#fig3 = px.bar(df2['Unit'].value_counts())


# Menampilkan teks di kolom pertama
#with col1:
    #st.markdown("*Jumlah Pasien per Poli/Unit*")
    #st.write(fig3)

# Menampilkan teks di kolom kedua
#with col2:
    #st.markdown("*Jumlah Pasien per Penjamin*")
    #st.write(fig2)


#st.markdown("--------")
st.markdown('<p class="big-font">Highlight Preview Dashboard Analisis Omset dan Sebaran Pasien RS Salam Sehat</p>', unsafe_allow_html=True)

with st.expander("Overview Dashboard dan Sebaran Omset"):
    col5, col6 = st.columns(2)
    with col5:
        st.subheader("Overview Sebaran Omset, Sebaran Jumlah Pasien dan Disclaimer")
        st.image("ars3_overview1.png")
        st.write("*Dashboard ini memberikan gambaran/deskripsi analitik terkait sebaran omset dan jumlah pasien pada masing2 Poli/Unit dan Dokter serta analisa statistik lainnya sehingga dapat memberikan insight bagi manajemen dalam pengambilan keputusan bisnis yang efektif dan efesien*")
        st.write("*Discalimer : Rumah Sakit Salam Sehat (RS3) adalah rumah sakit fiktif, dimana data yg diolah didalam rangka Analisa, Evaluasi dan Visualisasinya merupakan Data Dummy/Bukan Data yg sebenarnya dan Bilamana ada kesamaan data ataupun pola/trend data dengan perusahaan real sejenis, maka itu adalah sebuah kebetulan yg tidak mencerminkan kondisi real dari Dokter maupun Rumah Sakit/Perusahaan sejenis tsb*")
   
    with col6:
        st.subheader("Komparasi Omset per Periode")
        st.image("ars3_overview1a.png")
        st.write("*Grafik ini tidak hanya menunjukkan bagaimana fluktuasi omset yg terjadi mulai dari awal periode sd periode tahun berjalan namun dapat dilihat juga komparasinya antar tahun pada masing-masing periodenya dengan memilih (klik) tahun yang akan dikomparasikan*")
        st.write("*Pada masing-masing info box juga dapat dilihat total omset setiap tahunnya serta rata2 omset per periode/per bulan pada masing-masing tahun*")
        st.write("*Pada infobox note dapat dilihat dari seluruh periode omset, periode manakah yang menghasilkan performa omset terbaik/terbesar ?*")

with st.expander("Overview Jumlah Omset per Penjamin"):
    col7, col8 = st.columns(2)
    with col7:
        st.subheader("Jumlah Omset per Penjamin")
        st.image("ars3_overview5.png")
        st.write("*Diagram batang ini menunjukkan rangking/urutan jumlah omset berdasarkan masing-masing penjamin pasien setiap tahunnya. Hal tsb memberikan gambaran siapa penjamin sebagai kontributor terbesar omset sehingga dapat menjadi pertimbangan tim marketing dlm mengalokasikan fokus target pasar RS*")
    with col8:
        st.subheader("Komparasi Jumlah Omset tiap Penjamin per Periode")
        st.image("ars3_overview5a.png")
        st.write("*Grafik ini menunjukan komparasi jumlah omset masing-masing penjamin pada setiap periode/bulan di setiap tahunnya (klik Pilihan Tahun)*")

with st.expander("Overview Jumlah Pasien per Penjamin"):
    col9, col10 = st.columns(2)
    with col9:
        st.subheader("Jumlah Pasien per Penjamin")
        st.image("ars3_overview6.png")
        st.write("*Diagram batang ini menunjukkan rangking/urutan jumlah pasien berdasarkan masing-masing penjamin pasien setiap tahunnya. Hal tsb memberikan gambaran siapa penjamin sebagai kontributor terbesar jumlah pasien sehingga dapat menjadi pertimbangan tim marketing dlm mengalokasikan fokus target pasar RS*")

    with col10:
        st.subheader("Komparasi Jumlah Pasien tiap Penjamin per Periode")
        st.image("ars3_overview6a.png")
        st.write("*Grafik ini menunjukan komparasi jumlah pasien masing-masing penjamin pada setiap periode/bulan di setiap tahunnya (klik Pilihan Tahun)*")


tabs = st.tabs(["POLI/UNIT", "DOKTER", "BPJS KESEHATAN", "STATISTIK","RAJAL (OP) DAN RANAP (IP)"])
with tabs[0]:
    with st.expander("Rangking Omset dan Jumlah Pasien Poli/Unit"):
        col11, col12, col11a, col12a = st.columns(4)
        with col11:
            st.subheader("Rangking Omset per Poli/Unit")
            st.image("bomset_poli.png")
        with col12:
            st.subheader("Komparasi Rangking Omset Poli/Unit per Periode")
            st.image("bomset_poli2.png")
        with col11a:
            st.subheader("Rangking Jumlah Pasien per Poli/Unit")
            st.image("cpasien_poli.png")
        with col12a:
            st.subheader("Komparasi Rangking Jumlah Pasien Poli/Unit per Periode")
            st.image("cpasien_poli2.png")

    with st.expander("Trend Omset dan Jumlah Pasien Poli/Unit"):
        col13, col14, col13a, col14a = st.columns(4)
        with col13:
            st.subheader("Trend Omset per Poli/Unit")
            st.image("bomset_poli3.png")
        with col14:
            st.subheader("Komparasi Trend Omset Poli/Unit per Periode")
            st.image("bomset_poli3a.png")

        with col13a:
            st.subheader("Trend Jumlah Pasien per Poli/Unit")
            st.image("cpasien_poli3.png")
        with col14a:
            st.subheader("Komparasi Trend Jumlah Pasien Poli/Unit per Periode")
            st.image("cpasien_poli3a.png")

    with st.expander("Omset dan Jumlah Pasien Poli/Unit per Penjamin"):
        col13c, col14d, col13e, col14f = st.columns(4)
        with col13c:
            st.subheader("Komparasi Jumlah Omset Tahunan per Poli/Unit per Penjamin")
            st.image("bomset_poli4.png")
        with col14d:
            st.subheader("Komparasi Jumlah Omset Poli/Unit per Penjamin per Periode")
            st.image("bomset_poli4a.png")
        with col13e:
            st.subheader("Komparasi Jumlah Pasien Tahunan per Poli/Unit per Penjamin")
            st.image("cpasien_poli4.png")
        with col14f:
            st.subheader("Komparasi Jumlah Pasien Poli/Unit per Penjamin per Periode")
            st.image("cpasien_poli4a.png")

    with st.expander("Omset dan Jumlah Pasien Poli/Unit di Atas Rata2 nya dari Seluruh Periode"):
        col15,col16 = st.columns(2)
        with col15:
            st.subheader("Omset Poli/Unit di Atas Rata2 nya dari Seluruh Periode")
            st.image("bomset_poli5.png")
        with col16:
            st.subheader("Jumlah Pasien Poli/Unit di Atas Rata2 nya dari Seluruh Periode")
            st.image("cpasien_poli4b.png")

    with st.expander("Omset Poli/Unit Pareto"):
        st.subheader("Poli/Unit Pareto (Penopang 80% Omset RS)")
        st.image("dpareto_poli5a.png")


with tabs[1]:
    with st.expander("Rangking Omset dan Jumlah Pasien Dokter"):
        col11x, col12x, col11ax, col12ax = st.columns(4)
        with col11x:
            st.subheader("Rangking Omset per Dokter")
            st.image("eomset_dokter.png")
        with col12x:
            st.subheader("Komparasi Rangking Omset Dokter per Periode")
            st.image("eomset_dokter2.png")
        with col11ax:
            st.subheader("Rangking Jumlah Pasien per Dokter")
            st.image("fpasien_dokter.png")
        with col12ax:
            st.subheader("Komparasi Rangking Jumlah Pasien Dokter per Periode")
            st.image("fpasien_dokter2.png")
    
    with st.expander("Trend Omset dan Jumlah Pasien Dokter"):
        col13x, col14x, col13ax, col14ax = st.columns(4)
        with col13x:
            st.subheader("Trend Omset per Dokter")
            st.image("eomset_dokter3.png")
        with col14x:
            st.subheader("Komparasi Trend Omset Dokter per Periode")
            st.image("eomset_dokter3a.png")

        with col13ax:
            st.subheader("Trend Jumlah Pasien per Dokter")
            st.image("fpasien_dokter3.png")
        with col14ax:
            st.subheader("Komparasi Trend Jumlah Pasien Dokter per Periode")
            st.image("fpasien_dokter3a.png")

    with st.expander("Omset dan Jumlah Pasien Dokter per Penjamin"):
        col13cx, col14dx, col13ex, col14fx = st.columns(4)
        with col13cx:
            st.subheader("Komparasi Jumlah Omset Tahunan per Dokter per Penjamin")
            st.image("eomset_dokter4.png")
        with col14dx:
            st.subheader("Komparasi Jumlah Omset Poli/Unit per Dokter per Periode")
            st.image("eomset_dokter4a.png")
        with col13ex:
            st.subheader("Komparasi Jumlah Pasien Tahunan per Dokter per Penjamin")
            st.image("fpasien_dokter4.png")
        with col14fx:
            st.subheader("Komparasi Jumlah Pasien Dokter per Penjamin per Periode")
            st.image("fpasien_dokter4a.png")

    with st.expander("Omset dan Jumlah Pasien Dokter di Atas Rata2 nya dari Seluruh Periode"):
        col15x,col16x = st.columns(2)
        with col15x:
            st.subheader("Omset Dokter di Atas Rata2 nya dari Seluruh Periode")
            st.image("eomset_dokter5.png")
        with col16x:
            st.subheader("Jumlah Pasien Dokter di Atas Rata2 nya dari Seluruh Periode")
            st.image("fpasien_dokter5.png")

    with st.expander("Omset Dokter Pareto"):
        st.subheader("Dokter Pareto (Penopang 80% Omset RS)")
        st.image("fpareto_pasiendokter.png")

with tabs[2]:
    with st.expander("Trend Omset dan Jumlah Pasien BPJS kesehatan"):
        col11xy, col12xy, col11axy, col12axy = st.columns(4)
        with col11xy:
            st.subheader("Trend Omset BPJS Kesehatan Seluruh Periode")
            st.image("htrendomset_bpjs.png")
        with col12xy:
            st.subheader("Komparasi Trend Omset BPJS Kesehatan per Periode")
            st.image("htrendomset_bpjs2.png")
        with col11axy:
            st.subheader("Trend Jumlah Pasien BPJS Kesehatan Seluruh Periode")
            st.image("htrendpasien_bpjs.png")
        with col12axy:
            st.subheader("Komparasi Trend Jumlah Pasien BPJS Kesehatan per Periode")
            st.image("htrendpasien_bpjs2.png")

    with st.expander("Rangking Omset dan Rangking Jumlah Pasien Poli/Unit dan Dokter"):
        col13xy, col14xy, col13axy, col14axy = st.columns(4)
        with col13xy:
            st.subheader("Rangking Omset BPJS Kesehatan per Poli")
            st.image("iomsetpoli_bpjs.png")
        with col14xy:
            st.subheader("Rangking Jumlah Pasien BPJS Kesehatan per Poli")
            st.image("ipasienpoli_bpjs.png")

        with col13axy:
            st.subheader("Rangking Omset BPJS Kesehatan per Dokter")
            st.image("jomsetdr_bpjs.png")
        with col14axy:
            st.subheader("Rangking Jumlah Pasien BPJS Kesehatan per Dokter")
            st.image("jpasiendr_bpjs.png")

    with st.expander("Historical Peluang Kedatangan Pasien BPJS Kesehatan"):
        st.subheader("Historical Peluang Kedatangan Pasien BPJS Kesehatan per Poli/Unit")
        st.image("khistoricalpasien_bpjs.png")

with tabs[3]:
    with st.expander("Statistik Sebaran Omset per Poli"):
        col11xyz, col12xyz = st.columns(2)
        with col11xyz:
            st.subheader("Histogram Sebaran Omset per Poli")
            st.image("histo_poli.png")
        with col12xyz:
            st.subheader("Boxplot dan 5 Number Summary Sebaran Omset per Poli")
            st.image("histo_bp_poli.png")

    with st.expander("Statistik Sebaran Omset per Dokter"):
        col11xyza, col12xyza = st.columns(2)
        with col11xyza:
            st.subheader("Histogram Sebaran Omset per Dokter")
            st.image("histo_dr.png")
        with col12xyza:
            st.subheader("Boxplot dan 5 Number Summary Sebaran Omset per Dokter")
            st.image("histo_bp_dr.png")

with tabs[4]:
    with st.expander("Trend dan Jumlah Omset Rajal (OP) dan Omset Ranap (IP) Seluruh Periode"):
        col13xyb, col14xyb, col13axyb, col14axyb = st.columns(4)
        with col13xyb:
            st.subheader("Trend Omset Rajal (OP) dan Ranap (IP)")
            st.image("ltrendopip.png")
        with col14xyb:
            st.subheader("Komparasi Omset Rajal (OP) dan Ranap (IP)")
            st.image("ltrendopip2.png")

        with col13axyb:
            st.subheader("Resume Omset Rajal (OP) dan Ranap (IP)")
            st.image("ltrendopip3.png")
        with col14axyb:
            st.subheader("Jumlah Omset Rajal (OP) dan Ranap (IP) di Atas Rata2 nya dari Seluruh Periode")
            st.image("ltrendopip4.png")

    with st.expander("Trend dan Jumlah Pasien Rajal (OP) dan Omset Ranap (IP) Seluruh Periode"):
        col13xybz, col14xybz, col13axybz, col14axybz = st.columns(4)
        with col13xybz:
            st.subheader("Trend Jumlah Pasien Rajal (OP) dan Ranap (IP)")
            st.image("mtrenpasopip.png")
        with col14xybz:
            st.subheader("Komparasi Jumlah Pasien Rajal (OP) dan Ranap (IP)")
            st.image("mtrenpasopip2.png")

        with col13axybz:
            st.subheader("Resume Jumlah Pasien Rajal (OP) dan Ranap (IP)")
            st.image("mtrenpasopip3.png")
        with col14axybz:
            st.subheader("Jumlah Pasien Rajal (OP) dan Ranap (IP) di Atas Rata2 nya dari Seluruh Periode")
            st.image("mtrenpasopip4.png")
            
st.markdown("--------")
col100, col200 = st.columns(2)
with col100:
    st.markdown("[(Klik disini untuk Contoh Dashboard lainnya - Analisis dan Prediksi Machine Learning)](https://abdr.shinyapps.io/rs_salam_sehat/)")
with col200:
    st.markdown("[(Klik disini untuk Penjelasan Contoh Dashboard lainnya - Youtube video)](https://youtu.be/WHpYuC6DRhk?feature=shared)")

st.markdown("--------")
st.write("*Created by Hospital Financial Analyst - HFA*")
st.write("*Mico Chandra*")
st.markdown("[(Klik Linkedin)](https://www.linkedin.com/in/mico-chandra-3a1708202/)")

