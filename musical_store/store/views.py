from django.http import HttpResponse, JsonResponse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from store.models import Instrument, Brand
from store.serializers import InstrumentSerializer, BrandSerializer


class SimpleView(View):
    def get(self, request):
        return HttpResponse('hello, world')


class InstrumentsView(ListAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['@instrument_type', '@brand', '@model_name']
    ordering_fields = ['production_year', 'brand']

    def get_queryset(self):
        return Instrument.objects.filter(instrument_type='guitar')


class AddInstrument(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

    def post(self, request, **kwargs):
        serializer = InstrumentSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            context = InstrumentSerializer(Instrument.objects.all(), many=True)
            return Response(context.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
