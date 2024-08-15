from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

def health_check(request):
    data = {
        'message': 'Hello, world!',
        'status': 'success'
    }
    return JsonResponse(data, status=200)

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    path('health/', health_check),
    path('admin/', admin.site.urls),

    path('', include('apps.books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
