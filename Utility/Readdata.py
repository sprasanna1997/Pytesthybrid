import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\chiya\PycharmProjects\HybridFramwork\Configuaration\config.ini")

class Readdata:
    @staticmethod
    def base_url():
        return config.get("common info", "baseUrl")

    @staticmethod
    def username():
        return config.get("common info", "username")

    @staticmethod
    def lastname():
        return config.get("common info", "lastname")

    @staticmethod
    def age():
        return config.get("common info", "age")

    @staticmethod
    def salary():
        return config.get("common info", "salary")

    @staticmethod
    def department():
        return config.get("common info", "department")

    @staticmethod
    def email():
        return config.get("common info", "email")

    @staticmethod
    def currentaddress():
        return config.get("common info", "currentaddress")

    @staticmethod
    def password():
        return config.get("common info", "password")

    @staticmethod
    def mobileno():
        return config.get("common info", "mobileno")

    @staticmethod
    def dob():
        return config.get("common info", "dob")

    @staticmethod
    def subject():
        return config.get("common info", "subject")
