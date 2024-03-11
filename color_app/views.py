from django.shortcuts import render
from color_app.models import Color
from random import randint
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from color_app.models import Color
from color_app.forms import ColorForm

#######################
# Function Based Views
#######################


def home_view(request):
    "A view function which renders the homepage"

    skyblue = Color(name="skyblue", red=135, green=206, blue=250)

    params = {
        "name": "mufinized",
        "color": skyblue,
    }
    
    response = render(request, 'color_app/index.html', params)
    return response

def random_color_view(request):
    "A view function which renders a random color"

    random_color = Color(
        name="random color", 
        red=randint(0, 256), 
        green=randint(0, 256),
        blue=randint(0, 256)
    )

    params = {"color": random_color, "name": "mufinized"}

    return render(request, 'color_app/index.html', params)


def color_list(request):
    "A view function which renders a random color"



    return render(request, 'color_app/color_list.html', {})


#######################
# Class Based Views
#######################

class ColorListView(ListView):
    model = Color
    template_name = "color_app/color_list.html"
    queryset = Color.objects.order_by(*["red", "blue", "green"]).reverse()

class NewColorView(CreateView):
    model = Color
    form_class = ColorForm
    template_name = "color_app/color_form.html"
    success_url = reverse_lazy("color_app:color_list")