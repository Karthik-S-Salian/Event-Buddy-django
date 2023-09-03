from django import forms
from .models import Event,Comment

INPUT_CLASSES = 'w-full py-4 px-6 border border-gray-400 my-2'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude=("created_at","created_by")
        localized_fields = ["timings"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'poster': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                'id':"image-input"
            }),
            'location_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'registration_link': forms.URLInput(attrs={
                'class': INPUT_CLASSES
            }),
            'publish': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'timings':forms.DateTimeInput(attrs={
                'class': INPUT_CLASSES,
                'type': 'datetime-local'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'longitude': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            })
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=("body",)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': "w-full h-20 border px-2 py-2",
                'placeholder':"leave a comment"
            })
        }
