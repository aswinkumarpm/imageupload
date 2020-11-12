from django import forms
from .models import FileUpload


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ('photo',
                  )

SIZE_CHOICES= [
    ('800*800', '800*800'),
    ('102*60', '102*60'),
    ('100*100', '100*100'),
    ('750*500', '750*500'),
    ]


class SizeSelectForm(forms.Form):
    size= forms.CharField(label='Select Your Size', widget=forms.Select(choices=SIZE_CHOICES))
