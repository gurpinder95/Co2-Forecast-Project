# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 09:44:43 2021

@author: Priyanka Kadale
"""

##################      IMPORT LIBRARIES   ############################################
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  ### To plot graph
from statsmodels.tsa.arima.model import ARIMA
import plotly.express as px #### To plot graph
import warnings   ####### To ignore convergence warning
from statsmodels.tools.sm_exceptions import ConvergenceWarning
warnings.simplefilter('ignore', ConvergenceWarning)

##############    TITLE AND CONTENT   ###################################################                                   
st.title("Forecast Co2 Levels  For An Organization")
st.write("Air Quality time series consist of complex linear and non linear patterns.An Auto Regressive Integrated Moving Average Model [ARIMA] modeling approach has been adapted to forecast yearly mean ambient Air pollutant. ")



st.image("c2.jpg", width=700)  ##### Image below title

##########################     SIDEBAR HEADER CONTENT    ########################################
st.sidebar.image("fore.jpg", width=300)  ####Image for sidebar
st.sidebar.write("To forecast Co2 levels for next 30 years for an organization")


df = pd.read_csv("CO2 data.csv")  ###### Import data
df1 = df.drop("Year", axis=1)
index = pd.date_range(start="1800", end="2015", freq="A-JAN")  ### Converting year into date range
df1.set_index(index, inplace=True)
model_arima_final = ARIMA(df1, order = (14,1,15)).fit() 

list1 = ["Type of Visualization", "Tabular", "Graphical"]
list2 =["Select Type of Data","Original Data", "Predicted Data"]
option1  = st.sidebar.selectbox("Select Type of Data", list2)

if option1:
        st.write('**You have selected:**',option1)
#########################  ORIGINAL DATA   ####################################################
if option1 =="Original Data":
                st.header("Original Data")
                st.table(df.head(10)) ##Display table
                
                st.set_option('deprecation.showPyplotGlobalUse', False) ###Display Line Graph
                fig = plt.figure(figsize=(8,6))
                plt.plot (df1, label='Original Data', color="#3b5998")
                plt.title('Previous data',color="#ff6700")
                plt.xlabel("Year",color="#f44336")
                plt.ylabel("CO2 emission levels",color="#f44336")
                plt.grid(True)
                plt.legend()
                st.plotly_chart(fig)
                st.write("The Co2 emission levels seems to be increasing since the year 1879 and hit the highest in the year 1979 by the value of 18.2")
                st.write("**Note:** We have used only one variable here , Co2 (Emission values for past 200 years).Hence this is called as the Univariate Time Series Analysis/Forecasting. When the time series analysis shows a general trend , that is upward . It is called uptrend.")
               
elif option1=="Select Type of Data":  ##### When no option is selected
                    st.write("**Please select the type of Data**")
                    
##############################  PREDICTED DATA  ##############################################
else:  
        number=st.sidebar.slider("Pick the year from 1-30",1,30)
        option2 = st.sidebar.selectbox("Select Visualization Type:", list1)
        b3= st.sidebar.button(label="Show")
        
        if b3:
            if option2 =="Tabular":     ########  Display data in tabular format
                forecast =model_arima_final.forecast(number)
                st.header("**Forecasted/Predicted values:**")
                st.table(forecast)
            
            else :
                future_values =model_arima_final.forecast(number)  ##### Display data in graphical format
                st.set_option('deprecation.showPyplotGlobalUse',False)
                fig = plt.figure(figsize=(8,6))
                plt.plot(df1, label='Original data', color="#3b5998")
                plt.plot(future_values, label='Predicted data', color="#f44336")
                plt.title('Forecasted Data',color="#16537e")
                plt.xlabel("Number of Years",color="#16537e")
                plt.ylabel("CO2 emission",color="#16537e")
                plt.legend(loc='upper left', fontsize=8)                
                plt.grid(True)
                plt.legend()
                st.plotly_chart(fig)
                
################################# SIDE BAR FOOTER CONTENT ############################################     
st.sidebar.title("**About**")  ######### ABOUT Section
       
st.sidebar.header("Guided by:-")
st.sidebar.title("***Parth***")
st.sidebar.title("Made With Streamlit by")
st.sidebar.image("streamlitlogo1.png", width=180)    ####  Displaying streamlit logo
st.sidebar.header("P-81 Group 3:")
st.sidebar.write("***Priyanka***",",","***Prithvi***")
st.sidebar.write("***Gurpinder***",",","***Vishal***")
