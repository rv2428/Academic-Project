from django.urls import path

from . import views

urlpatterns = [ 
        path('sightings/',views.sightings),
        path('map/',views.coordinates),
        path('<str:Unique_Squirrel_Id>/edit',views.edit_squirrel),
]
