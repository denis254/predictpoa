from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('twitter/', views.twitter, name = "twitter"),
    path('facebook/', views.facebook, name = "facebook"),
    path('history/', views.results, name = "history"),
    path('payment/', views.payment, name = "payment"),
    path('viptips/', views.viptips, name = "viptips"),
    path('signup/', views.signup, name = "signup"),
    path('viptipsgames/', views.viptipsgames, name = "viptips"),
    path('punterpick/', views.punterpick, name = "punterpick"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('comment/', views.comment, name = "comment"),
]
