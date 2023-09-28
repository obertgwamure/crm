from django.urls import path
from .views import lead_list, lead_detail

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='leads_list'),
    path('<pk>/', lead_detail, name='lead_detail'),
]