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
    def email():
        return config.get("common info", "email")

    @staticmethod
    def currentaddress():
        return config.get("common info", "currentaddress")

    @staticmethod
    def password():
        return config.get("common info", "password")