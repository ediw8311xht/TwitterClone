from django.shortcuts import redirect, render
from tweet_app.models import Tweet

def home(request):
    tweets = Tweet.objects.all()
    return render(request, "home.html", {"tweets": tweets})

def tweet(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            Tweet.objects.create(author=request.user, text=request.POST["new_tweet"])
            return redirect("/")
        else:
            return render(request, "tweet.html")
    else:
        return redirect("/login/")
