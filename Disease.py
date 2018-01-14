import datetime


class Disease:
    def __init__(self, title,type,cause,symptom,treatment,complication,specialist,created_by):
        self.__pubid = ''
        self.__title = title
        self.__type = type
        self.__cause = cause
        self.__symptom = symptom
        self.__treatment = treatment
        self.__complication = complication
        self.__specialist = specialist
        self.__created_by = created_by
        currentdatetime = datetime.datetime.now()
        create_date = str(currentdatetime.day) + "-" + str(currentdatetime.month) + "-" + str(
            currentdatetime.year)  # DD-MM-YYYY format
        self.__created_date = create_date



    def get_pubid(self):
        return self.__pubid

    def get_title(self):
        return self.__title

    def get_cause(self):
        return self.__cause

    def get_symptom(self):
        return self.__symptom

    def get_treatment(self):
        return self.__treatment

    def get_complication(self):
        return self.__complication

    def get_specialist(self):
        return self.__specialist

    def get_created_by(self):
        return self.__created_by

    def get_created_date(self):
        return self.__created_date

    def get_type(self):
        return self.__type

    def set_title(self, title):
        self.__title = title

    def set_cause(self, cause):
        self.__cause = cause

    def set_symptom(self, symptom):
        self.__symptom = symptom

    def set_treatment(self, treatment):
        self.__treatment = treatment

    def set_complication(self, complication):
        self.__complication = complication

    def set_specialist(self, specialist):
        self.__specialist = specialist

    def set_pubid(self, pubid):
        self.__pubid = pubid

    def set_created_by(self, created_by):
        self.__createdby = created_by

    def set_created_date(self, created_date):
        self.__created_date = created_date

    def set_type(self,type):
        self.__type = type
