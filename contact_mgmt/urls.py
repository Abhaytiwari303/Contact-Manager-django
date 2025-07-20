from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include contacts app URLs
    path('api/', include('contacts.urls')),

    # Root message
    path('', lambda request: JsonResponse({'message': 'Welcome to the Contact Management API'})),
]
