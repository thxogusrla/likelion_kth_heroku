from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

# Create your views here.
# class MainpageView(TemplateView):
#     template_name= 'main.html'

    
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    detatils = get_object_or_404(Blog, pk=blog_id)  #몇번째 객체를 가져올건지. 인자가 두개인데, 어떤 클래스로부터 객체를 얻을지, 몇번 객체 인지
    return render(request, 'detail.html', {'details':detatils})

def create(request): # 입력받은 내용을 데이터베이스에 저장해주는 함수.
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    # return redirect('/blogapp/'+str(blog.id)) #redirect(url)
    return redirect('detail', blog.id)

def blogform(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})