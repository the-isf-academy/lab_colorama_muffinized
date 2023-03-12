from django.core.exceptions import ValidationError

def color_channel_validator(value):
    "Checks that a value for a color channel (red, green, or blue) is within 0-255"
    if value < 0:
        raise ValidationError("{} is lower than 0".format(value))
    if value > 255:
        raise ValidationError("{} is higher than 255".format(value))

