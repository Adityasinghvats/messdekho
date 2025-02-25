from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm, TweetSearchForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

# we will handle 3 situation
# 1. get request to show the form
# 2 .post req to save the form
# 3. get req to show form with data
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list') 
    else:
        form = TweetForm()

    return render(request, 'tweet_form.html', {'form': form})

# last parameter is user = request.user , which means the req is created by logged in user
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

def tweet_search(request):
    search_result = []
    if request.method == 'POST':
        form = TweetSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['tweet']
            search_result = Tweet.objects.filter(text__icontains=search_query)
    else:
        form = TweetSearchForm()
    
    return render(request, 'tweet_search.html', {
        'form': form,
        'search_result': search_result
    })