from django.forms import ModelForm
from .models import Feedback


class Feedform(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'memo', 'important']
