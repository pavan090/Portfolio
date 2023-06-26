from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm



# Create your views here.
def home(request):
    return render(request,"home.html")

def products(request):
    return render(request,"products.html")

def service(request):
    return render(request,"service.html")

def contactus(request):
    return render(request,"contactus.html")

def aboutus(request):
    return render(request,"aboutus.html")


from django.views.generic import CreateView , ListView , DetailView , UpdateView , DeleteView

from AIDS.models import Student

class StuRg(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'sturg.html'
    success_url = '/'


class StuDt(DetailView):
    model = Student
    template_name = 'studt.html'

class StuUp(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'stuup.html'
    success_url = '/'

class StuDe(DeleteView):
    model = Student
    template_name = 'stude.html'
    success_url = '/'

class StuLi(ListView):
    model = Student
    template_name = 'stuli.html'





def student(request):
    stu = Student.objects.all()
    context = {'stu': stu}
    return render(request, 'student.html', context)


def detail(request, id):
	data = Student.objects.get(id = id)	
	context = {'data':data}
	return render(request,'detail.html', context)


def update(request, id):
	obj = get_object_or_404(Student, id =id)
	form = StudentForm(request.POST or None, instance = obj)
	data = Student.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('student')

	context = {'form':form, 'data':data}
	return render(request,'update.html', context )


def delete(request, id):
	data = Student.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('form')
	return render(request,'delete.html', context )


def form(request):
    stu = Student.objects.all() 

    form = StudentForm
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')  

    context = {'stu': stu, 'form': form}
    return render(request, 'form.html', context)


def rit(request):
	return render(request,'rit.html')

def get1(request):
	a = int(request.GET['num1'])
	b = int(request.GET['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'get.html',context)

def post1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'post.html',context)


# new views


def index(request):
      return render(request, 'AIDS/index.html')

def about(request):
      return render(request, 'AIDS/about.html')

def blog(request):
      return render(request, 'AIDS/blog.html')

def contact(request):
      return render(request, 'AIDS/contact.html')

def portfolio(request):
      return render(request, 'AIDS/portfolio.html')

def blog_single(request):
      return render(request, 'AIDS/blog-single.html')



