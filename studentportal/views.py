from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


def home(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('read')

    else:

        form = StudentForm()

    return render(
        request,
        'home.html',
        {'form': form}
    )


def read(request):

    search = request.GET.get('search')

    if search:

        students = Student.objects.filter(
            name__icontains=search
        )

    else:

        students = Student.objects.all()

    total_students = Student.objects.count()

    return render(
        request,
        'read.html',
        {
            'students': students,
            'total_students': total_students
        }
    )
    
def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect('read')

    else:

        form = StudentForm(instance=student)

    return render(
        request,
        'home.html',
        {'form': form}
    )  
    
def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('read')      