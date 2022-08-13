from pandas import to_datetime
import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config()
'''
# TaxiFareModel front
'''

pickup_datetime = to_datetime(
    st.text_input('date and time', '2012-10-06 12:10:20', key='pickup_date'))

pickup_longitude = st.text_input('pickup longitude',
                                 40.7614327,
                                 key='pickup_long')
pickup_latitude = st.text_input('pickup latitude',
                                -73.9798156,
                                key='pickup_lat')
dropoff_longitude = st.text_input('dropoff longitude',
                                  40.6513111,
                                  key='dropoff_long')
dropoff_latitude = st.text_input('dropoff latitude',
                                 -73.8803331,
                                 key='dropoff_lat')
passenger_count = st.text_input('passenger count', 2, key='p_count')

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

url = 'https://taxifare.lewagon.ai/predict'
if st.button('Get Fare'):
    request = requests.get(url, params)
    res = request.json()
    st.write(res['fare'])
