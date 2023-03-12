from django.forms.widgets import NumberInput

class ColorChannelRangeInput(NumberInput):
    """Defines a slider input.
    HTML5 natively supports sliders for ranges, so we just need to tweak the
    usual NumberInput to change the input_type.
    """
    input_type = "range"

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['min'] = 0
        context['widget']['attrs']['max'] = 255
        return context
