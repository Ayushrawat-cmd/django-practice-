from django.urls import path

from . import views

urlpatterns = [
    # path('', views.ProductListCreateAPIView.as_view()),
    # path("<int:pk>/", views.ProductDetailAPIView.as_view()) # dynamic url 
    # path('/insert', views.api_insert)
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view())
]   