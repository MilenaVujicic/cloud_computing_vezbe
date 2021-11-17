Django
------

Kreiranje projekta: ``django-admin startproject ime_projekta``
Kreiranje modula u projektu ``django-admin startapp ime_modula`` **da bi prethodna komanda radila potrebno je biti u pozicioniran folderu ime_projekta**


- Primer povezivanja sa postgresql bazom podataka (settings.py)::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'baza_podataka',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Dokumentacija za podešavanje baze podataka: https://docs.djangoproject.com/en/3.2/ref/databases/

- Primer modela (student/models.py)::

    class Student(models.Model):
        name = models.CharField(null=False, max_length=512)
        surname = models.CharField(null=False, max_length=512)
        avg_grade = models.DecimalField(null=False, max_digits=4, decimal_places=2)

Dokumentacija koja sadrži tipove polja modela: https://docs.djangoproject.com/en/3.2/topics/db/mod

- Primer json serializacije (student/serializers.py)::

    class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Student
            fields = ['id', 'name', 'surname', 'avg_grade']

Dokumentacija za pravljenje seriajlizatora: https://www.django-rest-framework.org/api-guide/serializers/



- Primer rest endpoint-ova (student/views.py)::

    def students_json(request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
        
    def student_json(request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, safe=False, status=200)


