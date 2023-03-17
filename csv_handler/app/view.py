from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from app.models import DataModel
from app.serializers import DataSerializer
from app.serializers import SortedDataSerializer
from app.utils import get_sorted_data

class DataUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, format=None):
        csv_file = request.FILES['file']
        data_models = []
        for row in csv_file:
            data_models.append(data_model)

        DataModel.objects.bulk_create(data_models)

        return Response(status=201)
    

class SortedDataView(APIView):
    def get(self, request, format=None):
        sort_by = request.query_params.get('sort_by', 'column1')
        order = request.query_params.get('order', 'asc')

        sorted_data = get_sorted_data(sort_by=sort_by, order=order, limit=50)
        serializer = SortedDataSerializer(sorted_data, many=True)
        return Response(serializer.data)
