from django.shortcuts import render
from .models import Posts
from .forms import PostsForm
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

@require_http_methods(["GET", "POST"])  
def index(request):
    if request.method == "GET":
        form = PostsForm()
        context = {"form": form}
        return render(request, "form.html", context)

    elif request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.cleaned_data['caption']
            comment = form.cleaned_data['comment']
            image = form.cleaned_data['image']
            ts_schedule = form.cleaned_data['ts_schedule']

            try:
                post = Posts(caption=caption, comment=comment, image=image, ts_schedule=ts_schedule)
                post.save()
                return HttpResponse("Succes")
            except Exception as e:
                return HttpResponse(e)
