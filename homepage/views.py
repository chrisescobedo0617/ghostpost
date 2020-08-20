from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.forms import AddPost
from homepage.models import Post

# Create your views here.
def index(request):
    all_posts = Post.objects.all().order_by("-id")
    return render(request, "index.html", {"all_posts": all_posts})

def boast_view(request):
    boast_posts = Post.objects.filter(post_type=True).order_by("-id")
    return render(request, "boasts.html", {"boast_posts": boast_posts})
    
def roast_view(request):
    roast_posts = Post.objects.filter(post_type=False).order_by("-id")
    return render(request, "roasts.html", {"roast_posts": roast_posts})

def votes_view(request):
    #refered to https://stackoverflow.com/questions/981375/using-a-django-custom-model-method-property-in-order-by
    votes = sorted(Post.objects.all(), key=lambda votes: votes.count_votes)[::-1]
    return render(request, "votes.html", {"votes": votes})

def add_post(request):
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
              content = data.get('content'),
              post_type = data.get('post_type')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddPost()
    return render(request, "generic_form.html", {"form": form})

#did the upvote and downvote referencing https://stackoverflow.com/questions/51668709/add-value-on-integerfield-with-a-buttondjango-1-11
def upvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def downvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))