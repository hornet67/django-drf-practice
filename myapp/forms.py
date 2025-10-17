from django import forms
from .models import Person, Division, District

class PersonForm(forms.ModelForm):
    division = forms.ModelChoiceField(
        queryset=Division.objects.all(),
        required=True,
        label='Division'
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.none(),
        required=True,
        label='District'
    )

    class Meta:
        model = Person
        fields = ['name', 'email', 'division', 'district']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Pre-populate district if editing an existing person
        if self.instance.pk and getattr(self.instance, 'division_id', None):
            self.fields['district'].queryset = District.objects.filter(
                division_id=self.instance.division_id
            )
