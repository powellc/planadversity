from django.core.urlresolvers import reverse
import floppyforms as forms

from .models import Response


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        exclude = ['user', 'meditation']

