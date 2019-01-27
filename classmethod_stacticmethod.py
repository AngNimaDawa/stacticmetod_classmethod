#stactic


# from datetime import date
# class agecalculator:
# 	def __inint__(self, year, month, day)
# 	self.year = year
# 	self.month = month
# 	self.day = day

#     def get_age(self):
#     	today = date,today()
#     	dob = date(self.year, self.month, self.day)


# isinstance method can be only accesss by instance 
# classmethod and stacticmethod can accesss by only classmethod and instancemethod

# classmethod is actual factorymethod



import math

class circle:
	"""

	"""
	counter = 0


	def __init__(self, radius):
		self.radius = radius
		self.increase_counter()



    @classmethod
    def increase_counter(cls)
     	cls.counter += 1


	@property

	def area(self):
		return math.pi * self.radius**2


	@property

	def perimeter(self):
		return 2 * math.pi * self.radius

	@staticmethod
	def get_diameter(radius):
		return 2*radius


	@classmethod
	def unit_circle(cls):
		return cls(1)


c = circle(5)
m = circle.unit_circle()
print(isinstance(m, circle))
# a = c.unit_circle()
# print(isinstance(a, circle))
a = c.unit_circle()
print(isinstance(a, circle))
d = circle(6)
print(circle.get_diameter(8))
print(d.get_diameter(d.radius))
print(c.area)
print(c.perimeter)
print(d.area)
print(d.perimeter)
print(self.increase_counter)
