from django.shortcuts import render, redirect


def profile_page(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect("/")
