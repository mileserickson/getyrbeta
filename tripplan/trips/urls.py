from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'trips'

urlpatterns = [
    url(r'^$', views.TripList.as_view(), name='trip_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.TripView.as_view(), name='trip_detail'),
    # url(r'^edit/(?P<pk>[0-9]+)/$', views.TripEditView.as_view(), name='trip_edit'),
    url(r'^create/$',
        views.TripCreateView.as_view(), name='trip_create'),
    url(r'^create/(?P<trip_id>[0-9]+)/trailhead/$',
        views.TrailheadCreateView.as_view(), name='trailhead_create'),
    url(r'^create/(?P<trip_id>[0-9]+)/objective/$',
        views.ObjectiveCreateView.as_view(), name='objective_create'),
    url(r'^create/(?P<trip_id>[0-9]+)/camp/$',
        views.CampCreateView.as_view(), name='camp_create'),
    url(r'^notifications/$', views.notifications, name='notifications'),
]


    # url(r'^create/(?P<trip_id>[0-9]+)/(?P<location_type>[\w])/$',
    #     views.TrailheadCreateView.as_view(), name='trailhead_create'),

            # <a href="{% url 'trips:trailhead_create' trip_id=trip.id location_type='trailhead' %}">Add new location</a>
