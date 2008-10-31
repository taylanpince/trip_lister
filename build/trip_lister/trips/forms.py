from django.forms import ModelForm

from trips.models import Trip


class TripForm(ModelForm):
    """
    A form for creating a new trip
    """
    class Meta:
        model = Trip
