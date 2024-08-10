from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['street', 'user_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Если запись уже существует, добавляем поле is_completed
            self.fields['is_completed'] = forms.BooleanField(
                required=False,
                initial=self.instance.is_completed,
                label="Is completed"
            )
