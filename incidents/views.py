from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from incidents.models import Incident
from incidents.serializers import IncidentSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def incident_list(request):
    user = request.user
    incidents = Incident.objects.filter(reporter=user)
    serializer = IncidentSerializer(incidents, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_incident(request):
    serializer = IncidentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.validated_data["reporter"] = request.user
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def edit_incident(request, pk):
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return Response({"error": "Incident not found."}, status=404)

    # Check if the incident is closed
    if incident.status == "Closed":
        return Response({"error": "Cannot edit a closed incident."}, status=400)

    # Check if the authenticated user is the reporter of the incident
    if incident.reporter != request.user:
        return Response(
            {"error": "You are not authorized to edit this incident."}, status=403
        )

    serializer = IncidentSerializer(incident, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def search_incident(request, incident_id):
    incident = get_object_or_404(
        Incident, incident_id=incident_id, reporter=request.user
    )
    serializer = IncidentSerializer(incident)
    return Response(serializer.data)
