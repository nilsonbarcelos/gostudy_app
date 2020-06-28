from ..models import Course


def add_course(course):
    Course.objects.create(name=course.name, description=course.description, start_date=course.start_date,
                          end_date=course.end_date, duration_time=course.duration_time, units=course.units,
                          units_done=course.units_done, type_course=course.type_course,
                          status_course=course.status_course,
                          user=course.user)


def course_list(user):
    return Course.objects.filter(user=user).all()


def course_list_id(id):
    return Course.objects.get(id=id)


def edit_course(db_course, new_course):
    db_course.name = new_course.name
    db_course.description = new_course.description
    db_course.start_date = new_course.start_date
    db_course.end_date = new_course.end_date
    db_course.duration_time = new_course.duration_time
    db_course.units = new_course.units
    db_course.units_done = new_course.units_done
    db_course.type_course = new_course.type_course
    db_course.status_course = new_course.status_course
    db_course.save(force_update=True)


def delete_course(db_course):
    db_course.delete()
