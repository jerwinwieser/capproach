from django.urls import path
from core import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='contact_list'),
    path('statistics/', views.StatisticsListView.as_view(), name='statistics_list'),
    path('create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('delete/<int:pk>/', views.ContactDeleteView.as_view(), name='contact_delete'),
    path('update/<int:pk>/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('read/<int:pk>', views.ContacReadView.as_view(), name='contact_read'),
    path('info/', views.modelFieldsInfo.as_view(), name='model_fields_info'),
    path('createtest/', views.TestCreateView.as_view(), name='test_create'),
]
