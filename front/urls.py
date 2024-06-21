from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="core"),
    path('dep/', dep, name='dep'),
    path('dep/<int:pk>/', dep_view,),
    path('onas/', onas, name='onas'),
    path('nauka/', nauka, name='nauka'),
    path('doctors/', DoctorSView.as_view(), name='doctors'),
    path('<int:pk>', DoctorDetailView.as_view(), name='doctor'),
    path('begi/', begi, name='begi')
]
