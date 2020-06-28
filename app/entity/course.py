class Course():
    def __init__(self, name, description, start_date,
                 end_date, duration_time, units, units_done, type_course, status_course, user):
        self.__name = name
        self.__description = description
        self.__start_date = start_date
        self.__end_date = end_date
        self.__duration_time = duration_time
        self.__units = units
        self.__units_done = units_done
        self.__type_course = type_course
        self.__status_course = status_course
        self.__user = user

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        self.__end_date = end_date

    @property
    def duration_time(self):
        return self.__duration_time

    @duration_time.setter
    def duration_time(self, duration_time):
        self.__duration_time = duration_time

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, units):
        self.__units = units

    @property
    def units_done(self):
        return self.__units_done

    @units_done.setter
    def units_done(self, units_done):
        self.__units_done = units_done

    @property
    def type_course(self):
        return self.__type_course

    @type_course.setter
    def type_course(self, type_course):
        self.__type_course = type_course

    @property
    def status_course(self):
        return self.__status_course

    @status_course.setter
    def status_course(self, status_course):
        self.__status_course = status_course

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

