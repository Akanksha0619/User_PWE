from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import SearchForm
from django.db.models import Q


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})



def post_list(request):
    form = SearchForm(request.GET or None)
    posts = Post.objects.all().order_by('-created_at')

    if form.is_valid():
        query = form.cleaned_data.get('query')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')

        if query:
            posts = posts.filter(Q(title__icontains=query) | Q(user__username__icontains=query))
        if start_date:
            posts = posts.filter(created_at__gte=start_date)
        if end_date:
            posts = posts.filter(created_at__lte=end_date)

    return render(request, 'post_list.html', {'posts': posts, 'form': form})


@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})

