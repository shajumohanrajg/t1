from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistrationDetailsAPIView.as_view(), name='registration-list'),
    # path('get_token/', views.MyTokenObtainPairSerializer.as_view() , name='get_token'),
    path('<int:user_id>/', views.RegistrationGetIdAPIView.as_view(), name='registration-detail'),
    path('edit/', views.RegistrationEditAPIView.as_view(), name='registration-detail'),
    path('search/', views.RegistrationSearchAPIView.as_view(), name='registration-search'),

]
