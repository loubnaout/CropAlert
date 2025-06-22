from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Alert
from .serializers import AlertSerializer
from .permissions import IsAgronome
from django.shortcuts import render



def alerts_page(request):
    return render(request, 'alerts.html')

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated, IsAgronome]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'agriculture_type']

    def get_queryset(self):
        qs = super().get_queryset()
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        radius = self.request.query_params.get('radius', 10) 

        if lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                radius = float(radius)
            except ValueError:
                return qs

            lat_min = lat - 0.1 * radius
            lat_max = lat + 0.1 * radius
            lon_min = lon - 0.1 * radius
            lon_max = lon + 0.1 * radius

            qs = qs.filter(
                latitude__gte=lat_min,
                latitude__lte=lat_max,
                longitude__gte=lon_min,
                longitude__lte=lon_max,
            )
        return qs

