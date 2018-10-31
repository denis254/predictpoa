from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('history/', views.results, name = "history"),
    path('payment/', views.payment, name = "payment"),
    path('viptips/', views.viptips, name = "viptips"),
    path('signup/', views.signup, name = "signup"),
    path('viptips/', views.viptips, name = "viptips"),
    path('punterpick/', views.punterpick, name = "punterpick"),
    path('accounts/', include('django.contrib.auth.urls')),
]
