from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets

from .models import Mentor, Student, Course
from .serializers import MentorSerializer, StudentSerializer, CourseSerializer
from .my_generics import ListMixinAPI, CreateMixinAPI, MyAPIView, UpdateMixinAPI, RetrieveMixinAPI, DeleteMiximAPI

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroy(UpdateMixinAPI, RetrieveMixinAPI, DeleteMiximAPI, MyAPIView, viewsets.ModelViewSet):
    serializer_class = MentorSerializer
    model = Course

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MentorListCreateAPIView(ListMixinAPI, CreateMixinAPI, MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MentorRetrieveUpdateDestroyAPIView(UpdateMixinAPI, RetrieveMixinAPI, DeleteMiximAPI, MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)