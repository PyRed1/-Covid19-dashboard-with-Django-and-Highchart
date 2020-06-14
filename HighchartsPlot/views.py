from django.shortcuts import render, HttpResponse,HttpResponseRedirect


def home(request):
    return render(request,'HighchartsPlot/home.html')

import pandas as pd 


path='/home/red/djProjects/djHighcharts/covidChart/'
global_data = pd.read_csv(path+'time_series_covid19_confirmed_global.csv',index_col=0)
df_temp = global_data.groupby('Country/Region').sum()

df_temp = df_temp.drop(['Lat', 'Long'], axis=1)
    
'''Transpose df_temp'''
cumul=df_temp.T

global_deaths = pd.read_csv(path + 'time_series_covid19_deaths_global.csv',index_col=0)
df_temp = global_deaths.groupby('Country/Region').sum()

df_temp = df_temp.drop(['Lat', 'Long'], axis=1)

'''Transpose df_temp'''
deaths=df_temp.T



global_recovered = pd.read_csv(path + 'time_series_covid19_recovered_global.csv',index_col=0)
df_temp = global_recovered.groupby('Country/Region').sum()

df_temp = df_temp.drop(['Lat', 'Long'], axis=1)

'''Transpose df_temp'''
recovered=df_temp.T



import numpy as np
# '''create deaths_rates dataframe with division of deaths and cumul dataframes'''
deaths_rates=(deaths.div(cumul.replace(0, np.nan)).fillna(0))*100
# '''create date culumn from index'''
deaths_rates['date']=deaths_rates.index
# '''transform date column to datetime '''
deaths_rates['date']=pd.to_datetime(deaths_rates['date'])
# '''create timestamp column with ms values  from date column using lambda function'''
deaths_rates['timestamp']=deaths_rates['date'].apply (lambda x: x.timestamp()*1000)




# '''create Recovery_rates dataframe with division of deaths and cumul dataframes'''
Recovery_rates=(recovered.div(cumul.replace(0, np.nan)).fillna(0))*100
# '''create date culumn from index'''
Recovery_rates['date']=Recovery_rates.index
# '''transform date column to datetime '''
Recovery_rates['date']=pd.to_datetime(Recovery_rates['date'])
# '''create timestamp column with ms values  from date column using lambda function'''
Recovery_rates['timestamp']=Recovery_rates['date'].apply (lambda x: x.timestamp()*1000)






# ca c'est l'objectif de ce projet , c'est de pouvoir manipuler le data venant d'une formulaire
# donc utiliser deux views en un comme dans cet answer 
# https://stackoverflow.com/questions/4808329/can-i-call-a-view-from-within-another-view    

from .forms import CountriesForm
def process(df):
    '''return a dataframe with all countries column and a column with timestamp in ms
        needed in Highcharts '''
    '''create date culumn from index'''
    df['date']=df.index
    
    '''transform date column to datetime '''
    df['date']=pd.to_datetime(df['date'])
    
    '''create timestamp column with ms values  from date column using lambda function'''
    df['timestamp']=df['date'].apply (lambda x: x.timestamp()*1000)
    
    '''return a dataframe with all countries column and a column with timestamp in ms'''
    return df


cumul_df=process(cumul)


# pour bien pouvoir manipuler le data venant du formulaire on utilise la methode POST 
# COMME dans le fichier views.py dans la doc :
# https://docs.djangoproject.com/en/3.0/topics/forms/#using-a-form-in-a-view

def ConfirmedCumulview(request):
    if request.method=='POST':
        form=CountriesForm(request.POST)
        
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[cumul_df[['timestamp',country]].values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_countries.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)

def from_cumul_to_daily(df):
    '''return a dataframe with all countries column and a column with timestamp in ms
        needed in daily Highcharts '''

    '''create daily dataframe '''
    df_daily=df.diff().dropna()
    
    '''create date culumn from index'''
    df_daily['date']=df_daily.index
    '''transform date column to datetime '''
    df_daily['date']=pd.to_datetime(df_daily['date'])
    '''create timestamp column with ms values  from date column using lambda function'''
    df_daily['timestamp']=df_daily['date'].apply (lambda x: x.timestamp()*1000)
    '''return a dataframe with all countries column and a column with timestamp in ms'''
    return df_daily

df_daily=from_cumul_to_daily(cumul)

def ConfirmedDailyview(request):
    if request.method=='POST':
        form=CountriesForm(request.POST)
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[df_daily[['timestamp',country]].values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_countries.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)


deaths_df=process(deaths)
def DeathsCumulview(request):
    if request.method=='POST':
        form=CountriesForm(request.POST)
        
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[deaths_df[['timestamp',country]].values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_countries.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)

deaths_daily=from_cumul_to_daily(deaths)
def DeathsDailyview(request):
    if request.method=='POST':
        form=CountriesForm(request.POST)
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[deaths_daily[['timestamp',country]].values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_countries.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)







def DeathsRatesview(request):    
    if request.method=='POST':
        form=CountriesForm(request.POST)
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[deaths_rates[['timestamp',country]].round(3).values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_percentages.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)

recovered_df=process(recovered)
def RecoveryCumulview(request):
    if request.method=='POST':
        form=CountriesForm(request.POST)
        
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[recovered_df[['timestamp',country]].values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_countries.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)    

def RecoveryRates(request):
    if request.method=='POST':
        form=CountriesForm(request.POST)
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[Recovery_rates[['timestamp',country]].round(3).values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_percentages.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)



Recoveries_daily=from_cumul_to_daily(recovered)
def RecoveriesDailyview(request):
    if request.method=='POST':
        form=CountriesForm(request.POST)
        if form.is_valid():
            countries=form.cleaned_data['countries'].split(',')
            # print(countries)
            
            data=[Recoveries_daily[['timestamp',country]].values.tolist() for country in countries]
            context={'data':data,'countries':countries}

            return render(request,'HighchartsPlot/plot_countries.html',context)
    
    
    else:
        form = CountriesForm() # blank form when the method is GET OR OTHER    
            
    context={'form':form}
    
    return render(request,'HighchartsPlot/postCountriesForm.html',context)



from .forms import myForm
def multipleChoiceview(request):
    if request.method == 'POST':
        form = myForm(request.POST)
        if form.is_valid():
            items = form.cleaned_data.get('choicesList')
            # do something with your results
            print(items,type(items))
            return  HttpResponse(f'/Thanks you have choosen {items}')
    else:
        form = myForm()
    # Countries=['Morocco','Algeria']    
    context={'form':form}
    return render(request,'HighchartsPlot/render_choices.html', context=context)


def BSView(request):
    listCountries=[(1,'Mo'),(2,'Tu'),(3,'Al')]
    context={'listCountries':listCountries}   
    return render(request,'HighchartsPlot/render_choices.html',context)