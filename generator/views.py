import base64
import io
from io import BytesIO

import qrcode
from django.http import HttpResponse
from django.shortcuts import render

from generator.forms import MainForm


def index(request):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            img = qrcode.make(text)
            img = img.get_image()

            buff = io.BytesIO()
            img.save(buff, format="PNG")
            contents = base64.encodebytes(buff.getvalue()).decode("utf-8")
            return render(request, "generator/index.html", {"form": form, "contents": contents})
    else:
        form = MainForm()
        return render(request, "generator/index.html", {"form": form})

