from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import PostForm, PostEditForm
from django.views.generic import UpdateView
from .models import PostModel


@login_required
def blog(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_form = form.save(commit=False)
            blog_form.author = request.user
            blog_form.save()
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'blog/blog.html', context={'form': form})


class UpdatePost(UpdateView):
    model = PostModel
    form_class = PostEditForm
    template_name = 'blog/update_blog.html'

