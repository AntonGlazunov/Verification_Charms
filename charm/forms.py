from django import forms

from charm.models import Charm, Fluke, Muster


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-basic'
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs['class'] = 'form-control datepicker'
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs['class'] = 'form-control flatpickr-time'
            elif isinstance(field.widget, forms.widgets.SelectMultiple):
                field.widget.attrs['class'] = 'form-control select2 select2-multiple'
            elif isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs['class'] = 'form-control select2'
            else:
                field.widget.attrs['class'] = 'form-control'


class FlukeForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Fluke
        fields = ('serial_number', 'IP')


class CharmForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Charm
        fields = ('serial_number',)


# class MusterCreateForm(StyleFormMixin, forms.ModelForm):
#     class Meta:
#         model = Muster
#         fields = ('charm', 'fluke')


# class MeasurementCreateForm(StyleFormMixin, forms.ModelForm):
#     class Meta:
#         model = Muster
#         fields = ('fluke', 'measurement')
#
#     def __init__(self, *args, **kwargs):
#         super(MeasurementCreateForm, self).__init__(*args, **kwargs)
#         instance = getattr(self, 'instance', None)
#         if instance and instance.pk:
#             self.fields['fluke'].widget.attrs['readonly'] = True


class ConnectionCreateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Muster
        fields = ('fluke',)
