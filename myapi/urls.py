from django.urls import include, path
from rest_framework import routers
from . import views

#create your paths here
router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

#wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
