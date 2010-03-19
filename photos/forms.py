from django.forms import ModelForm
from clayto_2.photos.models import Photo

class PhotoForm( ModelForm ):

    class Meta:
        model = Photo

    def save(self, force_insert=False, force_update=False, commit=True):

        m = super(PhotoForm, self).save(commit=False)

        # do custom stuff
        print("CUSTOM STUFF")

        if commit:
            m.save()

        return m
