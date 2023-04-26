from django.shortcuts import render

from generator.forms import MainForm


def index(request):
    # if request.method == "POST":
    #
    # else:
    #
    form = MainForm()
    return render(request, "generator/index.html", {"form": form})

