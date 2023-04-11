from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('butterfly/', views.butterfly_index, name='index'),
    path('butterfly/<int:butterfly_id>/', views.butterfly_detail, name='detail'),
    path('butterfly/create', views.ButterflyCreate.as_view(), name='butterflies_create'),

]
