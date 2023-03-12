from django.shortcuts import render
import logging
from color_app.models import Color
from random import randint

log = logging.getLogger(__name__)

def home_view(request):
    "A view function which renders the homepage"
    log.info("In color_app.views.home. Rendering the homepage.")
    skyblue = Color(name="skyblue", red=135, green=206, blue=250)
    params = {
        "name": "stranger",
        "color": skyblue,
    }
    response = render(request, 'color_app/index.html', params)
    return response

def random_color_view(request):
    "A view function which renders a random color"
    log.info("In color_app.views.home. Rendering a random color page.")
    random_color = Color(
        name="random color", 
        red=randint(0, 256), 
        green=randint(0, 256),
        blue=randint(0, 256)
    )
    params = {"color": random_color}
    return render(request, 'color_app/random_color.html', params)

