import datetime

class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email
        save_email(email)

    def work(self):
        return "I come to the pffice."

    def __str__(self):
        return f"Должность: {self.name}"

    def check_salary(self, days=1):
        return self.salary*days

    def save_email(self, email):
        with open("emails.txt", "a") as file:
            file.write(f"{email}")

    def validate(self):
        pass

class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

class Develop(Employee):
    tech_stack = ["Manager", "Programmer", "UI Designer"]

    def work(self):
        return "I come to the office and start to coding."

r = Recruiter("Alex", 10, "email@gmail.com")
d = Develop("Steve", 15, "email@gmail.com")

if __name__ == "__main__":
    try:
        pass
    except Exception as error:
        with open("logs.txt", "a") as file:
            file.write(f"{datetime.now()} | {error}")