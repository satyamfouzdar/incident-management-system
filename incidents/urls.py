from django.urls import path

from incidents.views import (
    incident_list,
    create_incident,
    edit_incident,
    search_incident,
)


urlpatterns = [
    path("", incident_list, name="incident-list"),
    path("create/", create_incident, name="incident-create"),
    path("edit/<str:pk>/", edit_incident, name="incident-edit"),
    path("search/<str:incident_id>/", search_incident, name="search_incident"),
]
