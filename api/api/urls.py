from django.contrib import admin
from django.urls import path
from candidate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #GETPOST link
    path('api/student/detailsgetpost/', views.StudentViewgetpost.as_view()),
    #UPDATEDELETE link
    path('api/student/detailsupdatedelete/<int:ab>', views.StudentViewupdatedelete.as_view()),
]
