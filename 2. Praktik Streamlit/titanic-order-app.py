# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:49:06 2023

@author: reza.darmawan
"""

import streamlit as st
import pickle
import cloudpickle as cp
import numpy as np
from urllib.request import urlopen
import datetime as dt

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
    result_text = f'RINGKASAN PEMESANAN \n\n Nama: {name} \n\n Jenis Kelamin: {jenis_kelamin} \n\n Tanggal Lahir: {tanggal_lahir} \n\n Jumlah Tiket Dipesan: {jumlah_tiket} \n\n Kelas: {kelas} \n\n Dermaga Keberangkatan: {dermaga_keberangkatan}'
    return result_text

if st.button('Submit'):
    result_text = process_order(name, jenis_kelamin, tanggal_lahir, 
                      jumlah_tiket, kelas, dermaga_keberangkatan)
    st.info(result_text)
    