from contact import views as contact_views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('search/', contact_views.search, name='search'),
    path('', contact_views.index, name='index'),
    #CRUD
    path('contact/<int:contact_id>/details/', contact_views.contact, name='contact'),
    path('contact/create/', contact_views.create, name='create'),
   
]
