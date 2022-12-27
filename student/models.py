from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=20)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=20)
    period = models.IntegerField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mentor}-{self.student}-{self.period}'