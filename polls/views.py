from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from .models import Student

fake = Faker()


def index(request):
    return render(request, "index.html")


def generate_student(request):
    if request.method == "GET":
        student = Student.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=fake.random_int(min=18, max=25),
        )
        context = {
            "student_id": student.id,
            "student_first_name": student.first_name,
            "student_last_name": student.last_name,
            "student_age": student.age,
        }
        return render(request, "index.html", context)
    else:
        return HttpResponse("Invalid request method. Please, use GET method")


def generate_students(request):
    try:
        if request.method == "GET":
            count = request.GET.get("count", 0)

            try:
                count = int(count)
                if 1 > count or count > 100:
                    raise ValueError(
                        "Invalid count value! Please, input students count as integer between 1 and 100"
                    )
            except ValueError as error:
                return HttpResponse(f"Invalid count parameter: {str(error)}")

            for i in range(count):
                student = Student.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=fake.random_int(min=18, max=50),
                )

            return HttpResponse(
                f"{count} students created! There are {student.id} students in the db."
            )
        else:
            return HttpResponse(
                "Invalid request method! Please, try again using GET method."
            )
    except (Exception,):
        return HttpResponse(
            "Invalid request method! Please, try again using GET method. "
            "Input '?count=YOUR_NUMBER' in the link"
        )
