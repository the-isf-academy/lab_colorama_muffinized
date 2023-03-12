from django.forms import ModelForm
from color_app.widgets import ColorChannelRangeInput
from color_app.models import Color
from random import randint

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'red', 'green', 'blue']
        widgets = {
            'red': ColorChannelRangeInput(),
            'green': ColorChannelRangeInput(),
            'blue': ColorChannelRangeInput(),
        }
