from django import forms
from django.utils.translation import ugettext_lazy as _

from trips.models import Trip


class TripForm(forms.ModelForm):
    """
    A form for creating a new trip
    """
    class Meta:
        model = Trip
    
    def clean(self):
        """
        Make sure that the end_date is later than start_date
        """
        end_date = self.cleaned_data.get("end_date")
        start_date = self.cleaned_data.get("start_date")
        
        if (end_date and start_date and (end_date - start_date).days < 0):
            raise forms.ValidationError(_("Trip's end date can't be before the start date"))
        
        return self.cleaned_data
