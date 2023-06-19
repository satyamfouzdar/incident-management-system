from django.urls import path

from pages.views import test_project


urlpatterns = [
    path('', test_project, name='tests')
]
