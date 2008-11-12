import types

from decimal import *

from django.db import models
from django.utils import simplejson
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from django.core.serializers.json import DateTimeAwareJSONEncoder


class LazyEncoder(simplejson.JSONEncoder):
    """
    Convert lazy translations before being passed on to simplejson's encoder
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj


def convert_queryset_to_json(queryset, fields=[]):
    """
    Convert a QuerySet into a JSON dictionary by only including the specified
    fields - this allows us to include custom properties and get rid of 
    unnecessary data given by the default json encoder
    """
    output = []
    
    for item in queryset:
        data = {}
        
        if len(fields) > 0:
            for field in fields:
                data[field] = getattr(item, field)
        else:
            for field in item._meta.fields:
                data[field.attname] = getattr(item, field.attname)
        
        output.append(data)
    
    return simplejson.dumps(output, cls=DateTimeAwareJSONEncoder, ensure_ascii=False)
