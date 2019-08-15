from django.conf.urls import url, include
from django.contrib import admin
from api.resources import EventResource

event_resource = EventResource()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(event_resource.urls)),
]