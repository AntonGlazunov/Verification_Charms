from django.urls import path
from django.views.decorators.cache import cache_page

from charm.apps import CharmConfig
from charm.views import FlukeCreateView, CharmCreateView, CharmListView, CharmDetailView, CharmUpdateView, \
    CharmDeleteView, FlukeListView, FlukeUpdateView, FlukeDeleteView, error_connection, ConnectionCreateView, \
    verification

app_name = CharmConfig.name

urlpatterns = [
    path('fluke_create/', FlukeCreateView.as_view(), name='fluke_create'),
    path('fluke_list/', FlukeListView.as_view(), name='fluke_list'),
    path('fluke_update/<int:pk>', FlukeUpdateView.as_view(), name='fluke_update'),
    path('fluke_delete/<int:pk>', FlukeDeleteView.as_view(), name='fluke_delete'),
    path('', CharmListView.as_view(), name='charm_list'),
    path('charm_create/', CharmCreateView.as_view(), name='charm_create'),
    path('charm_detail/<int:pk>', CharmDetailView.as_view(), name='charm_detail'),
    path('charm_update/<int:pk>', CharmUpdateView.as_view(), name='charm_update'),
    path('charm_delete/<int:pk>', CharmDeleteView.as_view(), name='charm_delete'),
    path('connection_create/', ConnectionCreateView.as_view(), name='connection_create'),
    path('error_connection/', error_connection, name='error_connection'),
        path('verification/', verification, name='verification'),
]
