from django.urls import path
from core import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('delete/<int:pk>/', views.ContactDeleteView.as_view(), name='contact_delete'),
    path('update/<int:pk>/', views.ContactUpdateView.as_view(), name='contact_update'),
]
