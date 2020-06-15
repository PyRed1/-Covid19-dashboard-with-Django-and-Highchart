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


]
