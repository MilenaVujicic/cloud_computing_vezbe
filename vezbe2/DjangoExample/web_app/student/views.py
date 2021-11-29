from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
# Create your views here.


def students_json(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)


def student_json(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)
    return JsonResponse(serializer.data, safe=False, status=200)


def student_html(request, id):
    ret = "<html><body><p>"

    student = Student.objects.get(id=id)
    ret += "Name: "
    ret += student.name
    ret += " Surname: "
    ret += student.surname
    ret += " Grade: "
    ret += str(student.avg_grade)
    ret += "</p></body></html>"

    return HttpResponse(content=ret, status=200)