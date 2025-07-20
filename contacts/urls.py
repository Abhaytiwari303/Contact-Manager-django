from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, RegisterView, LogoutView, MyTokenObtainPairView, ContactList, ContactDetail
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = [
    # JWT Token Auth
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration & Logout
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Contacts API
    path('', include(router.urls)),                      # /api/contacts/
    path('all/', ContactList.as_view(), name='contact-list'),      # /api/all/
    path('<int:pk>/', ContactDetail.as_view(), name='contact-detail'),  # /api/<id>/
]
