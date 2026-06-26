from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('candidate_register', views.candidate_register, name="candidate_register"),
    path('candidate_login', views.candidate_login, name="candidate_login"),
    path('logout', views.logout, name='logout'),
    path('candidate', views.candidate, name='candidate'),
    path('recruiter', views.recruiter, name='recruiter'),
    path('company_login', views.company_login, name="company_login"),
    path('company_register', views.company_register, name='company_register')
]