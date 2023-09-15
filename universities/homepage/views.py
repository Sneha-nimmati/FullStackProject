from django.shortcuts import render
from .models import *
from django.core.mail import send_mail


# Create your views here.
def home_view(request):
    universities = Universitieslist.objects.all()
    university_filter =[]
    id= {}
    for university in universities:
        id[university.StateId] = university.StateName
    if request.method == 'POST':
        selcted_id = request.POST['state-select']
        university_filter = Universitieslist.objects.filter(StateId=selcted_id)
    context = {'list': university_filter, 'states': id}
    return render(request, 'home.html', context)


def course_details_view(request, university_id):
    courses = CourseNames.objects.filter(UniversityId=university_id)
    majors = Subjects.objects.filter(UniversityId=university_id)
    allmajors = {}
    for major in majors:
        if major.CourseId not in allmajors:
            allmajors[major.CourseId] = []
        allmajors[major.CourseId].append(major.MajorName)
    context = {'courses': courses, 'subjects': allmajors, 'uid': university_id}
    return render(request, 'course_details.html', context)


def email_view(request,university_id):
    context ={'UUID': university_id}
    return render(request, 'send_email.html', context)

def send_email_view(request, university_id):

    courses = CourseNames.objects.filter(UniversityId=university_id)

    email_body = ""
    for course in courses:
        email_body += course.CourseName + ", "

    name=""
    if request.method == "POST":
        name = request.POST.get('name')
    send_mail(university_id,
              email_body,
              'nimmathisneha13@gmail.com',
              [name],
              fail_silently=False)
    return render(request, 'send_email.html')

from django.shortcuts import render

# Create your views here.
