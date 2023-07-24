from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views


#def trigger_error(request):
#    division_by_zero = 1 / 0

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    #path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] 
