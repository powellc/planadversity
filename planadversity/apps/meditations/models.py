from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import ShortUUIDField
from django.contrib.auth import get_user_model

User = get_user_model()

class Meditation(TimeStampedModel):
    text = models.TextField(_('Meditation Text'))
    slug = models.IntegerField(_('Day of the Year'))
    date = models.DateField(_('Date'), blank=True, null=True)


    def __unicode__(self):
        return u'{0} - {1}'.format(self.day, self.title)

    @permalink
    def get_absolute_url(self):
        return ('meditation-detail', None, {'slug': self.slug})

    def save(self, *args, **kwargs):
        super(Meditation, self).save(*args, **kwargs)


class Response(TimeStampedModel):
    slug = models.ShortUUIDField(_('slug'))
    user = models.ForeignKey(User)
    meditation = models.ForeignKey(Meditation)
    initial_response = models.CharField(_('Initial Response'), max_length=255,
                                        blank=True, null=True)
    desired_response = models.CharField(_('Desired Response'), max_length=255,
                                        blank=True, null=True)
    notes = models.TextField(_('Notes'))


    def __unicode__(self):
        return u'{0} response by {1}'.format(self.meditation, self.user)

    @permalink
    def get_absolute_url(self):
        return ('response-detail', None, {'slug': self.slug})
