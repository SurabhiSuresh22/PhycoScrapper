import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from PIL import Image
import datetime
import time
import cufflinks as cf
import altair as alt
import plotly.figure_factory as ff
import base64
from io import BytesIO
import cv2
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")
st.title("Phycoscrapper")

activities = ["Upload Data","Colour Detection","About"]
choice = st.sidebar.selectbox("Select Activty",activities)

if choice=='Upload Data':
	st.subheader("Upload Phycoscrapper data")
	file = st.file_uploader("",type=([".txt"]))
		
	if file:
		df=pd.read_csv(file,names=['Light Intensity', 'Temperature of Algae', 'Humidity in %', 'Temperature in C','Temperature in F', 'Heat Index in C', 'Heat Index in F',''])
		l=len(df.columns)
		df.dropna(axis=1, how='all', inplace=True)
		l=len(df)
		df['index']=list(range(1,l+1))
		df.set_index('index',inplace=True)

		option=st.sidebar.radio("Study Data",['Data','Analyse','Light Intensity', 'Temperature of Algae', 'Humidity in %', 'Temperature in C','Temperature in F', 'Heat Index in C', 'Heat Index in F','Data Summary','Download as CSV'])
		if option=='Data':
			st.table(df)

		elif option=='Heat Index in F':
			with st.container():
				col1, col2 = st.columns(2)
				with col1:
					st.subheader('Line Chart')
					st.line_chart(df['Heat Index in F'])
				with col2:
					st.subheader('Bar Chart')
					st.bar_chart(df['Heat Index in F'])

		elif option=='Heat Index in C':
			with st.container():
				col1, col2 = st.columns(2)
				with col1:
					st.subheader('Line Chart')
					st.line_chart(df['Heat Index in C'])
				with col2:
					st.subheader('Bar Chart')
					st.bar_chart(df['Heat Index in C'])

		elif option=='Temperature in F':
			with st.container():
				col1, col2 = st.columns(2)
				with col1:
					st.subheader('Line Chart')
					st.line_chart(df['Temperature in F'])
				with col2:
					st.subheader('Bar Chart')
					st.bar_chart(df['Temperature in F'])	

		elif option=='Temperature in C':
			with st.container():
				col1, col2 = st.columns(2)
				with col1:
					st.subheader('Line Chart')
					st.line_chart(df['Temperature in C'])
				with col2:
					st.subheader('Bar Chart')
					st.bar_chart(df['Temperature in C'])	

		elif option=='Humidity in %':
			with st.container():
				col1, col2 = st.columns(2)
				with col1:
					st.subheader('Line Chart')
					st.line_chart(df['Humidity in %'])
				with col2:
					st.subheader('Bar Chart')
					st.bar_chart(df['Humidity in %'])	
			
		elif option=='Light Intensity':
			with st.container():
				col1, col2 = st.columns(2)
				with col1:
					st.subheader('Line Chart')
					st.line_chart(df['Light Intensity'])
				with col2:
					st.subheader('Bar Chart')
					st.bar_chart(df['Light Intensity'])
				
		elif option=='Temperature of Algae':
			with st.container():
				col1, col2 = st.columns(2)
				with col1:
					st.subheader('Line Chart')
					st.line_chart(df['Temperature of Algae'])
				with col2:
					st.subheader('Bar Chart')
					st.bar_chart(df['Temperature of Algae'])

		elif option=='Analyse':
			st.header('Analyse')
			key=st.radio('Select',['Line Chart','Temperature of Algae v/s Light Intensity','Temperature (C) v/s Humidity (%)','Temperature (C) v/s Heat Index (C)','Temperature (F) v/s Humidity (%)','Temperature (F) v/s Heat Index (F)'])

			if key=='Line Chart':
				st.line_chart(df,use_container_width=True)
				
			elif key=='Temperature of Algae v/s Light Intensity':
				fig=df.iplot(asFigure=True,x='Temperature of Algae',y='Light Intensity',z='index',xTitle='Temperature of Algae',yTitle='Light Intensity',title='Temperature of Algae v/s Light Intensity' )
				st.plotly_chart(fig,use_container_width=True)

			elif key=='Temperature (C) v/s Humidity (%)':
				fig=df.iplot(asFigure=True,x='Temperature in C',y='Humidity in %',z='index',xTitle='Temperature in C',yTitle='Humidity in %',title='Temperature (C) v/s Humidity (%)' )
				st.plotly_chart(fig,use_container_width=True)

			elif key=='Temperature (C) v/s Heat Index (C)':
				fig=df.iplot(asFigure=True,x='Temperature in C',y='Heat Index in C',z='index',xTitle='Temperature in C',yTitle='Heat Index in C',title='Temperature (C) v/s Heat Index (C)' )
				st.plotly_chart(fig,use_container_width=True)

			elif key=='Temperature (F) v/s Humidity (%)':
				fig=df.iplot(asFigure=True,x='Temperature in F',y='Humidity in %',z='index',xTitle='Temperature in F',yTitle='Humidity in %',title='Temperature (F) v/s Humidity (%)' )
				st.plotly_chart(fig,use_container_width=True)

# 			elif key=='Temperature (C) v/s Heat Index (F)':
# 				fig=df.iplot(asFigure=True,x='Temperature in F',y='Heat Index in F',z='index',xTitle='Temperature in F',yTitle='Heat Index in F',title='Temperature (F) v/s Heat Index (F)' )
# 				st.plotly_chart(fig,use_container_width=True)

					
		elif option=='Data Summary':				
			st.table(df.describe())

		elif option=='Download as CSV':
			def get_table_download_link_csv(df):
				#csv = df.to_csv(index=False)
				csv = df.to_csv().encode()
				#b64 = base64.b64encode(csv.encode()).decode() 
				b64 = base64.b64encode(csv).decode()
				href = f'<a href="data:file/csv;base64,{b64}" download="data.csv" target="_blank">Download csv file</a>'
				return href

			st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)


elif choice=='About':
		
	st.subheader('Introduction')
	st.write("""Phyco means relating to ALGAE. This device helps to collect terrestrial algae,measure the  the surrounding habitat temperature of the algae,the humidity of the surroundings and the light intensity at the place.
			""")
	img1=Image.open('PHYCOBOT.jpeg')
	st.image(img1,width=800,caption='Electronics Part')

	st.subheader('Brief Idea of Working')
	st.write("""
			The MCU is known as the heart of an embedded system.It coordinates the working of all components efficiently.We have used Arduino Uno here as the MC.The different sensors used here are:Temperature and humidity sensor and Light intensity sensor.We also have used a camera module.The readings of the sensors and the picture captured are sent to the Arduino which process  the data and sends it to the SD Card module.The SD Card module can be read using a PC and the data collected will be tabulated and arranged with the help of a web app.
""")

elif choice=="Color Detection":
	st.subheader('Green Area Detection')
	st.write("""Click the button below to open the green area detector app""")
	link = '[Green Area Detector](https://colordetectorapp.herokuapp.com/)'
	st.markdown(link, unsafe_allow_html=True)
		
	
