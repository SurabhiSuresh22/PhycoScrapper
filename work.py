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

#from plotly.offline import download_plotlyjs,init_notebook_mode, plot, iplot
#cf.go_offline()


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

			elif key=='Temperature (C) v/s Heat Index (F)':
				fig=df.iplot(asFigure=True,x='Temperature in F',y='Heat Index in F',z='index',xTitle='Temperature in F',yTitle='Heat Index in F',title='Temperature (F) v/s Heat Index (F)' )
				st.plotly_chart(fig,use_container_width=True)


				
				#altairchart
				#f=alt.Chart(df).mark_circle().encode(x='Temperature', y='Humidity', tooltip=['Temperature', 'Humidity'])
				#st.altair_chart(f,use_container_width=True)

				# st.subheader('Distributive Plot')
				# hist_data = [df['Temperature in C'],df['Humidity in %']] 
				# group_labels=['Temperature in C','Humidity in %',]
				# fig = ff.create_distplot(hist_data, group_labels, bin_size=[5,5])	
				# st.plotly_chart(fig, use_container_width=True)	

					
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

elif choice=="Colour Detection":
		#st.set_page_config(layout="wide")
		#st.title("Phycoscrapper")
	st.subheader("Upload your image")

	uploaded_file = st.file_uploader("Choose an image")

	if uploaded_file:
			img_path = uploaded_file.name
			csv_path = 'colors.csv'

			# reading csv file
			index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
			df2 = pd.read_csv(csv_path, names=index, header=None)

			# reading image
			img = cv2.imread(img_path)
			img = cv2.resize(img, (800,600))
			


			#declaring global variables
			clicked = False
			r = g = b = xpos = ypos = 0

			#function to calculate minimum distance from all colors and get the most matching color
			def get_color_name(R,G,B):
					minimum = 1000
					for i in range(len(df2)):
							d = abs(R - int(df2.loc[i,'R'])) + abs(G - int(df2.loc[i,'G'])) + abs(B - int(df2.loc[i,'B']))
							if d <= minimum:
									minimum = d
									cname = df2.loc[i, 'color_name']

					return cname

			#function to get x,y coordinates of mouse double click
			def draw_function(event, x, y, flags, params):
					if event == cv2.EVENT_LBUTTONDBLCLK:
							global b, g, r, xpos, ypos, clicked
							clicked = True
							xpos = x
							ypos = y
							b,g,r = img[y,x]
							b = int(b)
							g = int(g)
							r = int(r)

			# creating window
			#cv2.namedWindow('image')
			

			while True:
					cv2.imshow('image', img)
					cv2.setMouseCallback('image', draw_function)
					if clicked:
							#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
							cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)

							#Creating text string to display( Color name and RGB values )
							text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
							#cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
							cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)

							#For very light colours we will display text in black colour
							if r+g+b >=600:
									cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

					if cv2.waitKey(20) & 0xFF == 27:
							break

			cv2.destroyAllWindows()


		
			
	

		
			
	
