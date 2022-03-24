from django.urls import path
from . import views

app_name = "sheets"

urlpatterns = [
    path('', views.HomeView.as_view(), name="HomeView"),
    path('upload-data/<int:client_id>/', views.UploadClientData.as_view(), name="UploadClientData"),
]
