from django.urls import path
from .views import (
    contact_list,
    add_contact,
    update_contact,
    delete_contact
)

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('add/', add_contact, name='add_contact'),
    path('update/<int:id>/', update_contact, name='edit_contact'),
    path('delete/<int:id>/', delete_contact, name='delete_contact'),
]