from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..services import course_service
from ..forms import CourseForm
from ..entity.course import Course


@login_required
def course_list(request):
    courses = course_service.course_list(request.user)
    return render(request, "course/course_list.html", {"courses": courses})


@login_required
def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            name = course_form.cleaned_data["name"]
            description = course_form.cleaned_data["description"]
            start_date = course_form.cleaned_data["start_date"]
            end_date = course_form.cleaned_data["end_date"]
            duration_time = course_form.cleaned_data["duration_time"]
            units = course_form.cleaned_data["units"]
            units_done = course_form.cleaned_data["units_done"]
            type_course = course_form.cleaned_data["type_course"]
            status_course = course_form.cleaned_data["status_course"]
            new_course = Course(name=name, description=description, start_date=start_date,
                                end_date=end_date, duration_time=duration_time, units=units,
                                units_done=units_done, type_course=type_course, status_course=status_course,
                                user=request.user)
            course_service.add_course(new_course)
            return redirect("course_list")
    else:
        course_form = CourseForm()
    return render(request, "course/course_form.html", {"course_form": course_form})


@login_required
def edit_course(request, id):
    db_course = course_service.course_list_id(id)
    if db_course.user != request.user:
        return HttpResponse("Access denied")
    course_form = CourseForm(request.POST or None, instance=db_course)
    if course_form.is_valid():
        name = course_form.cleaned_data["name"]
        description = course_form.cleaned_data["description"]
        start_date = course_form.cleaned_data["start_date"]
        end_date = course_form.cleaned_data["end_date"]
        duration_time = course_form.cleaned_data["duration_time"]
        units = course_form.cleaned_data["units"]
        units_done = course_form.cleaned_data["units_done"]
        type_course = course_form.cleaned_data["type_course"]
        status_course = course_form.cleaned_data["status_course"]
        new_course = Course(name=name, description=description, start_date=start_date,
                            end_date=end_date, duration_time=duration_time, units=units,
                            units_done=units_done, type_course=type_course, status_course=status_course,
                            user=request.user)
        course_service.edit_course(new_course)
        return redirect("course_list")
    return render(request, "course/course_form.html", {"course_form": course_form})


@login_required
def delete_course(request, id):
    db_course = course_service.course_list_id(id)
    if db_course.user != request.user:
        return HttpResponse("Access denied")
    if request.method == "POST":
        course_service.delete_course(db_course)
        return redirect("course_list")
    return render(request, "course/delete_confirmation.html", {"course": db_course})
