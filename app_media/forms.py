from django import forms
from app_media.models import File


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    file = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'file')


# class MultiFileForm(forms.Form):          # не работает
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))     # для загрузки одновременно много файлов

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class MultiFileForm(forms.Form):                     # для загрузки одновременно много файлов
    file_field = MultipleFileField()