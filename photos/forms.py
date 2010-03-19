from django.forms import ModelForm
from django.models import Photo

class PhotoForm( ModelForm ):

    class Meta:
        model = Photo

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoForm, self).save(commit=False)

        # do custom stuff

        if commit:
            m.save()

        return m
