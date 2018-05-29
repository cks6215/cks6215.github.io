from django import forms
from lotto.models import GuessNumber


class PostForm(forms.ModelForm):
    class Meta:
        model = GuessNumber
        fields = ('name', 'text', 'num_lotto')