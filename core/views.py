from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Profile, Notification
from django.core.paginator import Paginator


# Auto create profile
def get_or_create_profile(user):
    profile, created = Profile.objects.get_or_create(user=user)
    return profile

def feed(request):
    if request.user.is_authenticated:
        following_profiles = Profile.objects.filter(followers=request.user)
        following_users = User.objects.filter(profile__in=following_profiles)
        all_posts = Post.objects.filter(user__in=following_users) | Post.objects.filter(user=request.user)
        all_posts = all_posts.distinct().order_by('-created_at')
    else:
        all_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'feed.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        get_or_create_profile(user)
        login(request, user)
        messages.success(request, f'Welcome to SocialApp, {username}!')
        return redirect('feed')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('feed')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('feed')


@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if content:
            Post.objects.create(
                user=request.user,
                content=content,
                image=image
            )
            messages.success(request, 'Post created successfully!')
        else:
            messages.error(request, 'Post content cannot be empty!')

    return redirect('feed')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        # Remove notification
        Notification.objects.filter(
            sender=request.user,
            recipient=post.user,
            notification_type='like',
            post=post
        ).delete()
    else:
        post.likes.add(request.user)
        # Create notification
        if request.user != post.user:
            Notification.objects.get_or_create(
                sender=request.user,
                recipient=post.user,
                notification_type='like',
                post=post
            )

    return redirect('feed')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                post=post,
                user=request.user,
                content=content
            )
            # Create notification
            if request.user != post.user:
                Notification.objects.create(
                    sender=request.user,
                    recipient=post.user,
                    notification_type='comment',
                    post=post
                )

    return redirect('feed')


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_or_create_profile(user)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    return render(request, 'profile.html', {'profile': profile, 'posts': posts})


@login_required
def edit_profile(request):
    profile = get_or_create_profile(request.user)

    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile', username=request.user.username)

    return render(request, 'edit_profile.html', {'profile': profile})


@login_required
def follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    profile = get_or_create_profile(user_to_follow)

    if request.user in profile.followers.all():
        profile.followers.remove(request.user)
        # Remove notification
        Notification.objects.filter(
            sender=request.user,
            recipient=user_to_follow,
            notification_type='follow'
        ).delete()
        messages.success(request, f'Unfollowed {username}!')
    else:
        profile.followers.add(request.user)
        # Create notification
        Notification.objects.get_or_create(
            sender=request.user,
            recipient=user_to_follow,
            notification_type='follow'
        )
        messages.success(request, f'Now following {username}!')

    return redirect('profile', username=username)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.user:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    else:
        messages.error(request, 'You can only delete your own posts!')
    return redirect('feed')


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        messages.error(request, 'You can only edit your own posts!')
        return redirect('feed')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            post.content = content
            if 'image' in request.FILES:
                post.image = request.FILES['image']
            post.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('feed')
        else:
            messages.error(request, 'Post content cannot be empty!')

    return render(request, 'edit_post.html', {'post': post})

# Search the usename
def search(request):
    query = request.GET.get('q', '')
    users = []
    posts = []

    if query:
        users = User.objects.filter(username__icontains=query)
        posts = Post.objects.filter(content__icontains=query)

    return render(request, 'search.html', {
        'query': query,
        'users': users,
        'posts': posts
    })

@login_required
def notifications(request):
    notifs = Notification.objects.filter(recipient=request.user)
    # Mark all as read
    notifs.update(is_read=True)
    return render(request, 'notifications.html', {'notifications': notifs})

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)