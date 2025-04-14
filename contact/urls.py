from contact import views as contact_views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', contact_views.contact, name='contact'),
    path('', contact_views.index, name='index'),

]
