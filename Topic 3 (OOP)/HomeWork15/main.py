class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def work(self):
		return "I come to the pffice."

	def __str__(self):
		return f"Должность: {self.name}"

	def check_salary(self, days=1):
		return self.salary*days

class Recruiter(Employee):
	def work(self):
		return "I come to the office and start to hiring."

class Develop(Employee):
	tech_stack = ["Manager", "Programmer", "UI Designer"]

	def work(self):
		return "I come to the office and start to coding."

r = Recruiter("Alex", 10)
d = Develop("Steve", 15)

pass