from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('upload/', views.upload_record, name='upload_record'),
    path('export/', views.export_records, name='export_records'),
    path('export_fil/', views.export_records_fil, name='export_records_fil'),
    path('export_time/', views.export_records_time, name='export_records_time'),
]
