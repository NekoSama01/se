from django.urls import path, include
from . import views
from jobinfo.views import info

urlpatterns = [
    path('info/<int:job_id>/', info, name='job_info'),
    path('',views.detail, name='detail'),
]