"""
Created on Tue Aug 29 11:23:49 2023

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
st.header('Survival Rate Penumpang')

file_upload = st.file_uploader('File daftar penumpang:',type=['csv'],accept_multiple_files=False)

def upload_file(file_upload):
    
    
    #import model
    with urlopen('https://github.com/mihoku/MoF-PJJ-Data-Analytics-Project-Deployment/raw/main/1.%20Titanic%20Model/rf_titanic_model.sav') as file:
        model_titanic = pickle.load(file)
    
    #parse uploaded csv file
    data = pd.read_csv(file_upload,sep=';', header=0)    
        
    
    #prediksi berdasarkan profil penumpang
    prediction = model_titanic.predict(data)
    
    #menghitung persentase penumpang selamat
    count_of_value = np.count_nonzero(prediction == 1)
    total_elements = prediction.size    
    percentage = (count_of_value / total_elements) * 100
    
    return f'Persentase Penumpang Selamat: \n\n {percentage:.0f}%'

if st.button('Submit'):
        result_text = upload_file(file_upload)
        st.info(result_text)
    