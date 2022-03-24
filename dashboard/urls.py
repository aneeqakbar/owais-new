from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.IndexView.as_view(), name="IndexView"),
    path('view-client-data/<int:client_id>/<str:data_type>/', views.ViewClientData.as_view(), name="ViewClientData"),
    path('view-client-data/<int:client_id>/<str:data_type>/<str:field>/', views.ViewClientDataAnalytics.as_view(), name="ViewClientDataAnalytics"),
    path('view-data-chart/<int:data_id>/<str:data_type>/<str:field>/', views.ViewDataChartAnalytics.as_view(), name="ViewDataChartAnalytics"),
    path('add-client/', views.AddClientView.as_view(), name="AddClientView"),
    path('update-client/<int:client_id>/', views.UpdateClientView.as_view(), name="UpdateClientView"),
    path('manage-clients/', views.ManageClientView.as_view(), name="ManageClientView"),
]
