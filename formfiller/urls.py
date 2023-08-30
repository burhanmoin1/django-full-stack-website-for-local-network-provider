from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('internet/', views.internet_page, name='internet_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('feedback/', views.feedback_form_view, name='feedback_form'),
    path('submit_signup/', views.submit_signup, name='submit_signup'),
    path('thankyou/', views.thank_you, name='thank_you'),
    path('tv/', views.tv_page, name='tv_page'),
]
