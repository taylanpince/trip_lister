from datetime import timedelta

from django.conf import settings
from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize, get_serializer

from trips.models import Trip
from trips.forms import TripForm
from trips.settings import START_DATE, WAIT_PERIOD
from trips.encoders import LazyEncoder, convert_queryset_to_json


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
    
    if request.is_ajax():
        template_format = "json"
        mimetype = "application/json"
        trips = convert_queryset_to_json(trips, ["title", "start_date", "end_date", "total_days"])
    else:
        template_format = "html"
        mimetype = "text/html; charset=utf-8"
    
    return render_to_response("trips/overview.%s" % template_format, {
        "trips": trips,
        "form": form,
        "start_date": START_DATE,
        "end_date": end_date,
        "lost_days": lost_days,
    }, context_instance=RequestContext(request), mimetype=mimetype)


@require_POST
@login_required
def create(request):
    """
    Create a new trip
    """
    form = TripForm(request.POST, auto_id="%s", prefix="TripForm")
    
    if form.is_valid():
        form.save()
    
    if request.is_ajax():
        template_format = "json"
        mimetype = "application/json"
        
        if form.errors:
            errors = simplejson.dumps(form.errors, cls=LazyEncoder, ensure_ascii=False)
        else:
            errors = None
    else:
        template_format = "html"
        mimetype = "text/html; charset=utf-8"
        errors = form.errors
    
    return render_to_response("trips/create.%s" % template_format, {
        "errors": errors,
    }, context_instance=RequestContext(request), mimetype=mimetype)


@require_POST
@login_required
def delete(request):
    """
    Delete a trip
    """
    pass
