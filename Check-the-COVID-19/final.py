# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:53:24 2020

@authors: Andrzej Krzyżanowski (shaidel@wp.pl) – PM, visionary, backend
          Bartosz Sadocha – tester 
          Bartosz Sokół – GUI, backend helper
"""

"""
MIT LicenseCopyright (c) [2020] [Andrzej Krzyżanowski]

Permission is hereby granted, free of charge, to any person obtaining acopyof 
this software and associated documentation files (the "Software"),to dealin the Software 
without restriction, including without limitation therightsto use, copy, modify, merge, publish,
distribute, sublicense, and/orsellcopies of the Software, and to permit persons to whom 
the Software isfurnished to do so, subject to the following conditions:The above copyright 
notice and this permission notice shall be includedin allcopies or substantial portions of 
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESSORIMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OFMERCHANTABILITY,FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALLTHEAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR 
ANY CLAIM, DAMAGES OR OTHERLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISINGFROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
plt.rcParams['figure.figsize'] = [15, 5]
import os
import tkinter as tk
from PIL import ImageTk, Image
 

values="bg"
if not os.path.exists("images"):
    os.mkdir("images")
 
def cleandata(df_raw):
    df_cleaned=df_raw.melt(id_vars=['Province/State','Country/Region','Lat','Long'],value_name='Sick',var_name='Date')
    df_cleaned=df_cleaned.set_index(['Country/Region','Province/State','Date'])
    return df_cleaned
 
def CONF():
    conf=1
 
def DEAD():
    dead=1
 
def RECOV():
    rec=1

def SUBMIT():
    ConfirmedCases_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
    Deaths_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv')
    Recoveries_raw=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv')
    
    ConfirmedCases=cleandata(ConfirmedCases_raw)
    Deaths=cleandata(Deaths_raw)
    Recoveries=cleandata(Recoveries_raw)
   
    values=name.get()
   
    conf=var_confirmed.get()
    dead=var_deaths.get()
    rec=var_recoveries.get()
   
    country_conf=ConfirmedCases.loc[values]
 
    country_conf.tail(1000)
 
    country_death=Deaths.loc[values]
 
    country_death.tail(1000)
 
    sigma=country_conf.merge(country_death, left_on="Date", right_on="Date")
 
   
    sigma
   
    country_rec=Recoveries.loc[values]
    sigma2=sigma.merge(country_rec, left_on="Date", right_on="Date")
   
    print(dead, conf, rec)
    if dead==1 and conf==1 and rec==1 :
        sigma2.plot(y=['Sick_x', 'Sick_y','Sick'], figsize=(12,8), marker='o', title='COVID-19 in '+values )
    elif dead==1 and conf==1 and rec==0 :
        sigma2.plot(y=['Sick_x','Sick_y'], figsize=(12,8), marker='o', title='COVID-19 in '+values )
    elif dead==1 and conf==0 and rec==0 :
        sigma2.plot(y=['Sick_y'], figsize=(12,8), marker='o', title='COVID-19 in '+values )
    elif dead==0 and conf==1 and rec==0 :
        sigma2.plot(y=['Sick_x'], figsize=(12,8), marker='o', title='COVID-19 in '+values )
    elif dead==0 and conf==0 and rec==1 :
        sigma2.plot(y=['Sick'], figsize=(12,8), marker='o', title='COVID-19 in '+values )
    elif dead==0 and conf==1 and rec==1 :
        sigma2.plot(y=['Sick_x', 'Sick'], figsize=(12,8), marker='o', title='COVID-19 in '+values )
    elif dead==1 and conf==0 and rec==1 :
        sigma2.plot(y=['Sick_y', 'Sick'], figsize=(12,8), marker='o', title='COVID-19 in '+values )
    else:
        print('No data')
    plt.savefig("images/chart.png")
    

    img2 = ImageTk.PhotoImage(Image.open("images/chart.png"))
    panel.configure(image=img2)
    panel.image = img2
   

window = tk.Tk() 
window.title( "Check the COVID-19" )
window.maxsize(800,750) 
 
img = ImageTk.PhotoImage(Image.open("images/initial.png"))
panel = tk.Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
    
text = tk.StringVar()
label = tk.Label(window, textvariable = text)
label.pack()
 
description = tk.Label(window, text="Please enter your test country/province/state/region").pack()
name = tk.Entry(window,width=40)
name.pack()
 
var_confirmed = tk.IntVar() 
var_deaths = tk.IntVar()
var_recoveries = tk.IntVar()
 
checkbutton_confirmed = tk.Checkbutton(window, text="Confirmed Cases", variable=var_confirmed, command=CONF)
checkbutton_confirmed.pack()
checkbutton_confirmed.select() 
 
deaths = tk.Checkbutton(window, text="Deaths", variable=var_deaths, command=DEAD)
deaths.pack()
deaths.select() 
 
recoveries = tk.Checkbutton(window, text="Recoveries", variable=var_recoveries, command=RECOV)
recoveries.pack()
recoveries.select() 
 
ok = tk.Button(window, text="OK", width=20, command=SUBMIT)
ok.pack()
   
tk.mainloop() 