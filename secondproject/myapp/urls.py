from myapp import views
from django.urls import path

urlpatterns = [
    path('Greet/',views.Greet),
    path('temp/',views.template)
]
