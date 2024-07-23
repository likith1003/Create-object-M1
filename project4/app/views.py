from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    rollno = '2'
    name = 'Bill'
    pno ='+91 8869187688'
    email = 'Bill@gmail.com'
    cls = '12'
    st = Student(name=name, rollno=rollno, pno=pno, email=email, cls=cls)
    st.save()
    user = {'rollno': rollno, 'name':name, 'pno': pno, 'email': email, 'cls': cls}
    return render(request, 'home.html', user)