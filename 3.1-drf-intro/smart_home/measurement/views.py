# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, \
    SensorDetailSerializer, SensorListSerializer


class CreateAPIView(ListAPIView):
    """ Создаем датчик. Ввести название и описание датчика. """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})


class ListView(ListAPIView):
    """ Получаем список датчиков. Список с краткой информацией по датчикам:
    ID, название и описание. """
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class RetrieveUpdateAPIView(RetrieveAPIView):
    """ Получаем информацию по конкретному датчику:
    ID, название, описание и список всех измерений температуры с указанием времени. """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        """ Меняем датчик. Можно ввести название и/или описание. """
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class ListCreateAPIView(ListAPIView):
    """ Добавляем измерение. Указываем ID датчика и температуру """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response({'status': 'OK'})
