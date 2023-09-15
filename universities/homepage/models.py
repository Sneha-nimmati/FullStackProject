from django.db import models


# Create your models here.
class Universitieslist(models.Model):
    UniversityId = models.IntegerField(primary_key=True)
    UniversityName = models.CharField(max_length=150)
    StateName = models.CharField(max_length=50)
    StateId = models.IntegerField()


class CourseNames(models.Model):
    UniversityId = models.IntegerField()
    CourseName = models.CharField(max_length=200)
    CourseId = models.CharField(max_length=10)


class Subjects(models.Model):
    UniversityId = models.ForeignKey(Universitieslist, default=None, on_delete=models.CASCADE)
    CourseId = models.CharField(max_length=10)
    MajorName = models.CharField(max_length=200)


