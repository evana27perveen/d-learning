from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from blog.models import PostModel
from profile_app.models import ProfileAddOnModel
from .forms import ProfileAddOnForm, ProfileEditOnForm
from django.views.generic import UpdateView
from PIL import Image


@login_required
def profile(request):
    this_user = ProfileAddOnModel.objects.filter(owner=request.user).last()
    if this_user is None:
        default_demo = ProfileAddOnModel(my_bio='!!!nothing yet!!!')
        default_demo.owner = request.user
        default_demo.save()
    context = {
        'posts': PostModel.objects.filter(author=request.user),
        'user_profiles': ProfileAddOnModel.objects.filter(owner=request.user).order_by('-id')[0],
    }
    return render(request, 'profile/profile.html', context)


@login_required
def add_my_profile(request):
    form = ProfileAddOnForm()
    if request.method == 'POST':
        form = ProfileAddOnForm(request.POST, request.FILES)
        if form.is_valid():
            profile_form = form.save(commit=False)
            profile_form.owner = request.user
            profile_form.save()
            return HttpResponseRedirect(reverse('profile_page'))

    return render(request, 'profile/add_profile.html', context={'form': form})


class UpdateProfile(UpdateView):
    model = ProfileAddOnModel
    form_class = ProfileEditOnForm
    template_name = 'profile/edit_profile.html'

