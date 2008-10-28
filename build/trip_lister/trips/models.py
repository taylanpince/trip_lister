from django.db import models
from django.utils.translation import ugettext_lazy as _


class Trip(models.Model):
    """
    A trip with start and end dates
    """
    title = models.CharField(_("Title"), max_length=100)
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    
    class Meta:
        verbose_name = _("Trip")
        verbose_name_plural = _("Trips")
    
    def __unicode__(self):
        return u"%s (%s - %s)" % (self.title, self.start_date, self.end_date)
