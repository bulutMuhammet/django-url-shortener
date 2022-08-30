from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import ShortURL
from api.serializers import URLSerializer, ListURLSerializer


class ShortenURL(APIView):
    serializer_class = URLSerializer
    throttle_scope = 'shorten'

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_url_obj = serializer.save()

        short_url = f"{request.build_absolute_uri('/')}{short_url_obj.short_url}"
        original_url = short_url_obj.original_url

        return Response(status=status.HTTP_201_CREATED, data={
            "Original URL": original_url,
            "Short URL": short_url
        })


class RedirectURLView(APIView):

    def get(self, request, *args, **kwargs):
        short_code = kwargs['short_code']
        short_url_obj = get_object_or_404(ShortURL, short_url=short_code)
        short_url_obj.visit_count += 1
        short_url_obj.save()
        return HttpResponseRedirect(redirect_to=short_url_obj.original_url)


class ListShortURL(ListAPIView):
    serializer_class = ListURLSerializer
    queryset = ShortURL.objects.all()
    filterset_fields = ['original_url', 'short_url', 'visit_count', 'created_date']
