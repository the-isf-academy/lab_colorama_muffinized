from django.db import models
from django.urls import reverse
from colorsys import rgb_to_hsv, hsv_to_rgb
from color_app.validators import color_channel_validator

class Color(models.Model):
    name = models.CharField(max_length=50)
    red = models.IntegerField(validators=[color_channel_validator])
    green = models.IntegerField(validators=[color_channel_validator])
    blue = models.IntegerField(validators=[color_channel_validator])

    def hex_code(self):
        """Returns a hex representation of the color like #00ff00 (green) suitable for CSS.
        """
        return '#' + ''.join([self.int2hex(self.red), self.int2hex(self.green), self.int2hex(self.blue)])

    def int2hex(self, int_value):
        "Converts an integer value like 15 to a two-digit hex string like 0b"
        return hex(int_value)[2:].zfill(2)

    def inverted(self, name=None):
        """Returns a new color which is the 'opposite' of this one. 
        A color is defined by red, green, and blue values, each ranging from
        0-255. If a color's red, green, and blue values are (x, y, z), the 
        opposite color's values are (255-x, 255-y, 255-z). For example, white is 
        (255, 255, 255), so its opposite, black, is (0, 0, 0). 
        """
        if name is None:
            name = self.name + ' inverted'
        return Color(name=name, red=255-self.red, green=255-self.green, blue=255-self.blue)

    def to_hsv(self):
        "Returns the color as hue, saturation, value instead of in rgb"
        return rgb_to_hsv(self.red/255, self.green/255, self.blue/255)

    def adjust_hue(self, delta, name=''):
        "Adjust the hue of the color by `delta`."
        h, s, v  = self.to_hsv()
        r, g, b = hsv_to_rgb(h + delta % 1, s, v)
        return Color(name=name, red=int(r*255), green=int(g*255), blue=int(b*255))

    def adjust_saturation(self, delta, name=''):
        "Adjust the saturation of the color by `delta`."
        h, s, v  = self.to_hsv()
        r, g, b = hsv_to_rgb(h, clamp(s + delta, 0, 1), v)
        return Color(name=name, red=int(r*255), green=int(g*255), blue=int(b*255))

    def adjust_value(self, delta, name=''):
        "Adjust the value of the color by `delta`."
        h, s, v  = self.to_hsv()
        r, g, b = hsv_to_rgb(h, s, clamp(v + delta, 0, 1))
        return Color(name=name, red=int(r*255), green=int(g*255), blue=int(b*255))

    def get_absolute_url(self):
        "Returns a url to this model"
        return reverse("colors_app:color_detail", args=[self.id])

    def __str__(self):
        "Defines how a Color will be represented as a string"
        return "<Color {} ({}, {}, {})>".format(self.name, self.red, self.green, self.blue)

    def __repr__(self):
        "Defines how a Color will be represented in code"
        return str(self)

def clamp(value, low, high):
    "Ensures that the value is between low and high"
    return min(max(low, value), high)
