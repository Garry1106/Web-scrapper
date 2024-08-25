import schedule
import time as tm
import streamlit as st
import requests
from bs4 import BeautifulSoup

st.header('Python Based Website Scrapper')
# Taking input from the User
url = st.chat_input("Paste the URL over here for Scrapping...")



if url:
    
    st.subheader('Recieved the Input!')
    def scrap():
        # Fetching Data From the Url
        html_file = requests.get(f'{url}').text

        soup = BeautifulSoup(html_file,'lxml')
        div = soup.find_all('li')

        for el in div:
            st.write(el.text)
            
    schedule.every(5).seconds.do(scrap)
    
    while True:
        schedule.run_pending()
        tm.sleep(1)       