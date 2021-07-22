from project.cat import Cat


class Tomcat(Cat):
    TOMCAT_GENDER = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.TOMCAT_GENDER)
        self.sound = "Hiss"
