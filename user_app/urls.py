from django.urls import include, path
from rest_framework import routers
from user_app import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'episodes', views.EpisodeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('user_app/', views.user_app, name='user_app'),
#     path('user_app/details/<int:id>', views.details, name='details'),
# ]