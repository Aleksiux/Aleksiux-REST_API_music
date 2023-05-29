from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add_band/', views.add_band),
    path('band/<int:pk>', views.get_specific_band),
    path('band_update/<int:pk>', views.update_specific_band),
    path('band_delete/<int:pk>', views.delete_band)
]