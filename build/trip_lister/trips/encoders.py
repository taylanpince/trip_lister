from django.utils import simplejson
from django.utils.functional import Promise
from django.utils.encoding import force_unicode


class LazyEncoder(simplejson.JSONEncoder):
    """
    Convert lazy translations before being passed on to simplejson's encoder
    """
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return obj
