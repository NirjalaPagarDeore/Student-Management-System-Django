from .forms import StudentForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# ==========================================
# CREATE USING MODEL FORM
# ==========================================

def add_student(request):

    if request.method == "POST":

        # Create a form object with submitted data
        form = StudentForm(request.POST)

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

# ==========================================
# READ + SEARCH STUDENT
# ==========================================

def student_list(request):

    # Get search text from URL
    search = request.GET.get("search")

    if search:

        # ORM Filter
        students = Student.objects.filter(
            name__icontains=search
        )

    else:

        students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {
            "students": students,
            "search": search
        }
    )

# ==========================================
# UPDATE STUDENT USING MODELFORM
# ==========================================

def edit_student(request, id):

    # Get the student record
    student = Student.objects.get(id=id)

    if request.method == "POST":

        # Create form with submitted data
        # instance=student tells Django to UPDATE this record
        form = StudentForm(request.POST, instance=student)

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


# ==========================
# DELETE OPERATION
# ==========================
def delete_student(request, id):

    # ORM: Fetch one student using its ID
    student = Student.objects.get(id=id)

    # deleted = request.GET.get("deleted")

    # ORM: Delete the student
    student.delete()

    return redirect("/list/?deleted=1")

# ==========================================
# VIEW SINGLE STUDENT
# ==========================================

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