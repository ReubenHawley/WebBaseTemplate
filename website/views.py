from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {"title": "Home"}
        return render(request, "website/Home.html", context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = {"title": "About"}
        return render(request, "website/About.html", context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {"title": "About"}
        return render(request, "website/About.html", context)

    def post(self, request, *args, **kwargs):
        context = {"title": "About"}
        return render(request, "website/About.html", context)
