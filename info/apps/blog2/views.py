from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.list import ListView
from .models import Post


def home(request):
    return render(request, 'blog2/home.html')

def posts(request):
    return render(request, 'blog2/posts.html')

def comentarios(request):
    return render(request, 'blog2/comentarios.html')

def contacto(request):
    return render(request, 'blog2/contacto.html')
    





# class ListarPosts(ListView):
#     model=Post
#     template_name = "postsList.html"
#     context_object_name = "noticias"
#     def get_queryset(self):
#         noticias = Post.objects.all().order_by('-fecha_creacion')
#         return noticias


'''class PostDetailView(HitCountDetailView):
    model = Post
    template_name = "blog/post.html"
    slug_field = "slug"
    count_hit = True
    form = ComentarioForm
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post", kwargs={
                'slug': post.slug
            }))
    def get_context_data(self, **kwargs):
        post_comments_count = Comentario.objects.all().filter(post=self.object.id).count()
        post_comments = ComComentarioment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context'''