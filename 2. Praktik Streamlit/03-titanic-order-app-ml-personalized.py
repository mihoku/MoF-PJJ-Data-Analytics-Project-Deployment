# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:49:06 2023

@author: reza.darmawan
"""

import streamlit as st
import pickle
import numpy as np
from urllib.request import urlopen
import datetime as dt
import pandas as pd

st.title('Titanic Online Booking')
st.image("""https://img.freepik.com/free-photo/large-luxurious-cruise-ship-sailing-sea-sunny-day-ai-generative_123827-23857.jpg?w=996&t=st=1693237135~exp=1693237735~hmac=e5d83509fdbf194196c3f594affaabc89cb1d3ef5a0f4dc952bca2f80f2e685e""")
st.header('Detail Pemesanan:')

name = st.text_input('Nama Pemesan:',
                     placeholder='Masukkan nama pemesan')

jenis_kelamin = st.selectbox(
    'Jenis Kelamin:',
    ('Laki-laki','Perempuan'))

tanggal_lahir = st.date_input('Tanggal Lahir:',dt.date(1987,12,10),
                              min_value=dt.date(1920,1,1))

jumlah_tiket = st.slider('Jumlah Tiket yang Dipesan:',
                         1,15,1)

kelas = st.selectbox(
    'Pilih Kelas:',
    ('Kelas 1','Kelas 2','Kelas 3'))

dermaga_keberangkatan = st.selectbox(
    'Pilih Dermaga Keberangkatan:',
    ('Cherbourg (C)','Queenstown (Q)','Southampton(S)'))

def process_order(name, jenis_kelamin, tanggal_lahir, 
                  jumlah_tiket, kelas, dermaga_keberangkatan):
    
    
    #import model
    with urlopen('https://github.com/mihoku/MoF-PJJ-Data-Analytics-Project-Deployment/raw/main/1.%20Titanic%20Model/rf_titanic_model.sav') as file:
        model_titanic = pickle.load(file)
    
    #tambahkan dictionary untuk kodifikasi
    genders = {"Laki-laki": 0, "Perempuan": 1}
    Pclass = {"Kelas 1":1,"Kelas 2":2, "Kelas 3":3}
    ports = {"Southampton(S)": 0, "Cherbourg (C)": 1, "Queenstown (Q)": 2}
    
    
    #satukan data dalam format dataframe
    columns=['Pclass','Sex','Age','relatives','Embarked']
    today = dt.date.today()    
    passenger_data = pd.DataFrame([[Pclass[kelas],
                                    genders[jenis_kelamin],
                                    today.year-tanggal_lahir.year,
                                    jumlah_tiket, 
                                    ports[dermaga_keberangkatan]
                                    ]],columns=columns)
    
    
    #prediksi berdasarkan profil penumpang
    prediction = model_titanic.predict(passenger_data)[0]
    
    result_text = f'RINGKASAN PEMESANAN \n\n Nama: {name} \n\n Jenis Kelamin: {jenis_kelamin} \n\n Tanggal Lahir: {tanggal_lahir} ({today.year-tanggal_lahir.year} tahun) \n\n Jumlah Tiket Dipesan: {jumlah_tiket} \n\n Kelas: {kelas} \n\n Dermaga Keberangkatan: {dermaga_keberangkatan}'
    
    #lengkapi dengan conditional agar rekomendasi sesuai dengan sasaran
    if(prediction==0):
        result_text+='\n\n\n Kami merekomendasikan kepada Anda tambahan asuransi perjalanan '
        if(jumlah_tiket>1):
            result_text+='secara paket bundling asuransi perjalanan family '
        else:
            result_text+='secara paket bundling asuransi perjalanan personal '
    
        if(Pclass[kelas]==3):
            result_text+='(budget edition)'
        
        return result_text
    
    else:
        return result_text

if st.button('Submit'):
    result_text = process_order(name, jenis_kelamin, tanggal_lahir, 
                      jumlah_tiket, kelas, dermaga_keberangkatan)
    st.info(result_text)
    