from datetime import timedelta

from django.conf import settings
from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from trips.models import Trip
from trips.forms import TripForm
from trips.encoders import LazyEncoder
from trips.settings import START_DATE, WAIT_PERIOD


@login_required
def overview(request):
    """
    Render an overview of all trips, along with stats
    """
    trips = Trip.objects.all()
    
    lost_days = 0
    
    for trip in trips:
        lost_days += trip.total_days
    
    end_date = START_DATE + WAIT_PERIOD + timedelta(days=lost_days)
    
    form = TripForm(auto_id="%s", prefix="TripForm")
    
    return render_to_response("trips/overview.html", {
        "trips": trips,
        "form": form,
        "start_date": START_DATE,
        "end_date": end_date,
        "lost_days": lost_days,
    }, context_instance=RequestContext(request))


@require_POST
@login_required
def create(request):
    """
    Create a new trip
    """
    form = TripForm(request.POST, auto_id="%s", prefix="TripForm")
    
    if form.is_valid():
        form.save()
    
    return render_to_response("trips/create.json", {
        "errors": simplejson.dumps(form.errors, cls=LazyEncoder),
    }, context_instance=RequestContext(request), mimetype="application/json")


@require_POST
@login_required
def delete(request):
    """
    Delete a trip
    """
    pass
