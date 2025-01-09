from unittest.mock import NonCallableMock

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hvl_ccb.comm.telnet import TelnetError
from hvl_ccb.dev.fluke884x import MeasurementFunction

from charm.forms import FlukeForm, CharmForm, ConnectionCreateForm
from charm.models import Charm, Fluke, Muster
from charm.services import connection

from config import settings


class ConnectionCreateView(LoginRequiredMixin, CreateView):
    model = Muster
    form_class = ConnectionCreateForm
    template_name = 'charm/connection_form.html'
    success_url = reverse_lazy('charm:charm_list')

    def form_valid(self, form):
        muster = form.save(commit=False)
        fluke = muster.fluke
        try:
            dev = connection(str(fluke.IP))
            settings.CONNECT = dev
            settings.CONNECT.measurement_function = MeasurementFunction.VOLTAGE_DC
        except TelnetError:
            return redirect('charm:error_connection')
        return super().form_valid(form)


def error_connection(request):
    return render(request, 'charm/error.html')


def verification(request):
    if request.method == 'POST':
        if request.POST.get('next') is not None:
            if settings.CONNECT is None:
                return redirect('charm:error_connection')
            else:
                measurement = settings.CONNECT.measure()*1000
                print(measurement)
        elif request.POST.get('stop') is not None:
            settings.CONNECT.stop()
            settings.CONNECT = None
            return redirect('charm:charm_list')
    return render(request, 'charm/verification.html')


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
    form_class = CharmForm
    success_url = reverse_lazy('charm:charm_update')


class CharmDeleteView(DeleteView):
    model = Charm
    success_url = reverse_lazy('charm:charm_list')

