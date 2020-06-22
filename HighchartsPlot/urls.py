from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ConfirmedCumul', views.ConfirmedCumulview, name='postcumul'),
    path('ConfirmedDaily', views.ConfirmedDailyview, name='postDaily'),
    path('DeathsCumul', views.DeathsCumulview, name='postDeaths'),
    path('DeathsDaily', views.DeathsDailyview, name='postDeathsDaily'),
    path('DeathsRates', views.DeathsRatesview, name='postDeathsRates'),
    path('RecoveriesCumul', views.RecoveryCumulview, name='RecoveriesCumul'),
    path('RecoveriesDaily', views.RecoveriesDailyview, name='RecoveriesDaily'),
    path('RecoveryRates', views.RecoveryRates, name='postRecoveryRates'),
    path('testMultiple', views.multipleChoiceview, name='testMultiple'),
    # this 2 urls for the json exempe see:
    # https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html
    path('json-exemple', views.json_example, name='json_example'),
    path('json-exemple/data', views.asyncRecoveryRates, name='asyncRecoveryRates'),
    # this for testing ajax with submitting button see
    # https://www.youtube.com/watch?v=QDdLvImfq_g
    path('ajax-exemple', views.ajaxview, name='ajaxview')

]
