from django.urls import path

from .views import (
    upload_resume,
    resume_history,
    analytics
)

urlpatterns = [

    path(
        'upload/',
        upload_resume
    ),

    path(
        'history/',
        resume_history
    ),

    path(
       'analytics/',
        analytics
   ),

   
]
