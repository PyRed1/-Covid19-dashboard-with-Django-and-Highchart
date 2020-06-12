from django.urls import path

from . import views

urlpatterns = [
    # path('', views.test, name='test'),
    path('postCumul', views.ConfirmedCumulview, name='postcumul'),
    path('postDaily', views.ConfirmedDailyview, name='postDaily'),
    path('postDeaths', views.DeathsCumulview, name='postDeaths'),
    path('postDeathsDaily', views.DeathsDailyview, name='postDeathsDaily'),
    path('postDeathsRates', views.DeathsRatesview, name='postDeathsRates'),
    path('postRecoveryRates', views.RecoveryRates, name='postRecoveryRates'),
    path('testMultiple', views.multipleChoiceview, name='testMultiple'),


]
