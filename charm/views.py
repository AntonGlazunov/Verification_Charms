from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from charm.forms import FlukeForm, CharmForm
from charm.models import Charm, Fluke


class FlukeCreateView(CreateView):
    model = Fluke
    form_class = FlukeForm
    success_url = reverse_lazy('charm:fluke_list')


class FlukeListView(LoginRequiredMixin, ListView):
    model = Fluke


class FlukeUpdateView(UpdateView):
    model = Fluke
    form_class = FlukeForm
    success_url = reverse_lazy('charm:fluke_list')


class FlukeDeleteView(DeleteView):
    model = Fluke
    success_url = reverse_lazy('charm:fluke_list')


class CharmCreateView(CreateView):
    model = Charm
    form_class = CharmForm
    success_url = reverse_lazy('charm:charm_list')


class CharmListView(LoginRequiredMixin, ListView):
    model = Charm


class CharmDetailView(LoginRequiredMixin, DetailView):
    model = Charm


class CharmUpdateView(UpdateView):
    model = Charm


class CharmDeleteView(DeleteView):
    model = Charm

