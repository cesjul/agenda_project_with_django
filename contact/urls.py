from contact import views as contact_views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('', contact_views.index, name='index'),
]
