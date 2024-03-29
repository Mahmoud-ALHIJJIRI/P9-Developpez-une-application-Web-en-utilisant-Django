from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.contrib import messages
from . import forms

# Create your views here.


class LoginPageView(View):
    template_name = "authentication/login.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("flux")
        message = "Identifiants invalides."
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request,
                           "Il y a eu une erreur avec le formulaire. "
                           "Veuillez vérifier les informations que vous avez saisies."
                           )
            return redirect("signup")

    context = {
        "form": form,
    }
    return render(request, "authentication/signup.html", context)
