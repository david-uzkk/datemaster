from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('alta/', views.alta, name='dashboard-alta'),
    path('media/', views.media, name='dashboard-media'),
    path('baixa/', views.baixa, name='dashboard-baixa'),
]
