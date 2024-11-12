from django.urls import path
from django.views.decorators.cache import cache_page

from charm.apps import CharmConfig
from charm.views import FlukeCreateView

app_name = CharmConfig.name

urlpatterns = [
    path('fluke_create/', FlukeCreateView.as_view(), name='fluke_create'),
    path('fluke_list/', FlukeCreateView.as_view(), name='fluke_list'),
    path('fluke_update/<int:pk>', FlukeCreateView.as_view(), name='fluke_update'),
    path('fluke_delete/<int:pk>', FlukeCreateView.as_view(), name='fluke_delete'),
    path('', statistics, name='charm_list'),
    path('charm_create/', FlukeCreateView.as_view(), name='charm_create'),
    path('charm_detail/<int:pk>', FlukeCreateView.as_view(), name='charm_detail'),
    path('charm_update/<int:pk>', FlukeCreateView.as_view(), name='fluke_update'),
    path('charm_delete/<int:pk>', FlukeCreateView.as_view(), name='charm_update')
]
