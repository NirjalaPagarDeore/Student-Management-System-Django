from .forms import StudentForm
from .forms import CourseForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .models import Course
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# ==========================================
# CREATE USING MODEL FORM
# ==========================================
@login_required
def add_student(request):

    if request.method == "POST":

        # Create a form object with submitted data
        form = StudentForm(request.POST, request.FILES)

        # Check if the submitted data is valid
        if form.is_valid():

            # Save the data into the database
            form.save()

            return redirect("/list/?success=1")

    else:

        # Create an empty form object
        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form
        }
    )



#-----
#--- Add course
@login_required
def add_course(request):

    if request.method == "POST":

        # Create a form object with submitted data
        form = CourseForm(request.POST)

        # Check if the submitted data is valid
        if form.is_valid():

            # Save the data into the database
            form.save()

            return redirect("/course_list/?success=1")

    else:

        # Create an empty form object
        form = CourseForm()

    return render(
        request,
        "students/add_course.html",
        {
            "form": form
        }
    )



# ==========================================
# READ + SEARCH STUDENT
# ==========================================

# Display student list with Search + Pagination
@login_required
def student_list(request):

    # Get search text from URL
    search = request.GET.get("search", "").strip()

    if search:

        # ORM Filter
        students = Student.objects.filter(
            name__icontains=search
        )

    else:

        # ORM: Get all students
        students = Student.objects.all()

    # Pagination
    paginator = Paginator(students, 5)

    # Get current page number
    page_number = request.GET.get("page")

    # Get records of current page
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "students/student_list.html",
        {
            "page_obj": page_obj,
            "search": search
        }
    )


#==============
#==Dashboard
#===============
@login_required
def dashboard(request):

    total_students = Student.objects.count()
    total_courses = Course.objects.count()
   

    return render(
        request,
        "students/dashboard.html",
        {
            # pass both counts here
             "total_students": total_students,
             "total_courses": total_courses,
        }
    )
#======================
#  Course List
#=====================


@login_required
def course_list(request):

    # ORM: Get all courses
    courses = Course.objects.all()
    # print(list(courses.values()))
    # Pagination
    paginator = Paginator(courses, 5)

    # Get current page number
    page_number = request.GET.get("page")

    # Get records of current page
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "students/course_list.html",
        {
            "page_obj": page_obj
        }
    )



# ==========================================
# UPDATE STUDENT USING MODELFORM
# ==========================================
@login_required
def edit_student(request, id):

    # Get the student record
    student = Student.objects.get(id=id)

    if request.method == "POST":

        # Create form with submitted data
        # instance=student tells Django to UPDATE this record
        form = StudentForm( request.POST, request.FILES, instance=student )

        # Validate form data
        if form.is_valid():

            # Save updated data
            form.save()

            return redirect("/list/?updated=1")

    else:

        # Display existing data in the form
        form = StudentForm(instance=student)

    return render(
        request,
        "students/edit_student.html",
        {
            "form": form
        }
    )


#++++++++++++++++++
#  Edit Course
#++++++++++++++++++++++++
@login_required
def edit_course(request, id):

    # Get the student record
    courses = Course.objects.get(id=id)

    if request.method == "POST":

        # Create form with submitted data
        # instance=student tells Django to UPDATE this record
        form = CourseForm( request.POST, instance=courses )

        # Validate form data
        if form.is_valid():

            # Save updated data
            form.save()

            return redirect("/course_list/?updated=1")

    else:

        # Display existing data in the form
        form = CourseForm(instance=courses)

    return render(
        request,
        "students/edit_course.html",
        {
            "form": form
        }
    )

# ==========================
# DELETE OPERATION
# ==========================
@login_required
def delete_student(request, id):

    # ORM: Fetch one student using its ID
    student = Student.objects.get(id=id)

    # deleted = request.GET.get("deleted")

    # ORM: Delete the student
    student.delete()

    return redirect("/list/?deleted=1")

#===============================
# Delete Course
#================================
@login_required
def delete_course(request, id):

    # ORM: Fetch one student using its ID
    courses = Course.objects.get(id=id)

    # deleted = request.GET.get("deleted")

    # ORM: Delete the student
    courses.delete()

    return redirect("/course_list/?deleted=1")

# ==========================================
# VIEW SINGLE STUDENT
# ==========================================
@login_required
def view_student(request, id):

      # Get the student or return a 404 page if not found
    student = get_object_or_404(Student, id=id)

    return render(
        request,
        "students/view_student.html",
        {
            "student": student
        }
    )


# User Login
def user_login(request):

    if request.user.is_authenticated:
      return redirect("student_list")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check username and password
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # Login the user
            login(request, user)

            # Redirect to Student List
            return redirect("dashboard")

        else:

            return render(
                request,
                "students/login.html",
                {
                    "error": "Invalid Username or Password"
                }
            )

    return render(
        request,
        "students/login.html"
    )


# User Logout
def user_logout(request):

    logout(request)

    return redirect("login")