from django.urls import path
from . import views

urlpatterns = [
    path('customer_dashboard', views.customer_dashboard, name='customer_dashboard'),
    path('support_agent/dashboard/', views.support_agent_dashboard, name='support_agent_dashboard'),
    path('customer/create_ticket/', views.create_ticket, name='create_ticket'),
    path('ticket/view/<int:ticket_id>/', views.view_ticket, name='view_ticket'),
    path('customer/ticket/<int:ticket_id>/reply/', views.reply_to_ticket, name='reply_to_ticket'),
    path('customer/register/', views.customer_register, name='customer_register'),
    path('support_agent/register/', views.support_agent_register, name='support_agent_register'),
    path('', views.home, name='home2'),

]

