class Utility:
    app_version = "1.0"

    @classmethod
    def get_version(cls):
        print(f"App Version: {cls.app_version}")

    @staticmethod
    def greet():
        print("Hello!,Welcome the app.") 

Utility.get_version()
Utility.greet()