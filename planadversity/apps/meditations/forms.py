from django.core.urlresolvers import reverse
import floppyforms as forms

from .models import Response, Meditation


class ResponseForm(forms.ModelForm):
    meditation = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Response
        exclude = ['user']

    def clean(self):
        cleaned_data = super(ResponseForm, self).clean()
        try:
            cleaned_data['meditation'] = Meditation.objects.get(id=cleaned_data['meditation'])
        except:
            pass

