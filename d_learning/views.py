from django.shortcuts import render, HttpResponseRedirect, reverse
from blog.models import PostModel
from django.contrib.auth.decorators import login_required
from profile_app.models import ProfileAddOnModel


@login_required()
def home(request):
    this_user = ProfileAddOnModel.objects.filter(owner=request.user).last()
    if this_user is not None:
        pp = ProfileAddOnModel.objects.filter(owner=request.user).order_by('-id')[0]
        context = {
            'posts': PostModel.objects.all(),
            'user_profiles': pp,
        }
    else:
        context = {
            'posts': PostModel.objects.all(),
        }
    return render(request, 'd_learning/home.html', context)


def about(request):
    return render(request, 'd_learning/about.html')
