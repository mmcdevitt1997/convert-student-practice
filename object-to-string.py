
# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.

class Student:

  def __init__(self, first_name,last_name, age, cohort_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cohort_number = cohort_number
        # self.full_name = (f"{first_name} {last_name}")
#   def output (self):
#       print(f"{self.first_name} {self.last_name} is {self.age} years old and is in cohort {self.cohort_number}")

  def __str__(self):
        return f"{self.full_name}"

  @property
  def first_name(self):
      try:
          return self.__first_name
      except AttributeError:
          return ""

  @first_name.setter
  def first_name(self, first_name):
      if isinstance (first_name, str):
          self.__first_name = first_name
      else:
          print("first name has to be a string")

  @property
  def last_name(self):
      try:
          return self.__last_name
      except AttributeError:
          return ""

  @last_name.setter
  def last_name(self, last_name):
      if isinstance (last_name, str):
          self.__last_name = last_name
      else:
          print("last name has to be a string")

  @property
  def age(self):
      try:
          return self.__age
      except AttributeError:
          return 0

  @age.setter
  def age(self, age):
      if isinstance (age, int):
          self.__age = age
      else:
          print("age must be a number")

  @property
  def cohort_number(self):
      try:
          return self.__age
      except AttributeError:
          return 0

  @cohort_number.setter
  def cohort_number(self, cohort_number):
      if isinstance (cohort_number, int):
          self.__cohort_number = cohort_number
      else:
          print("cohort must be a number must be a number")

  @property
  def cohort_number(self):
      try:
          return self.__cohort_number
      except AttributeError:
          return 0

  @cohort_number.setter
  def cohort_number(self, cohort_number):
      if isinstance (cohort_number, int):
          self.__cohort_number = cohort_number
      else:
          print("cohort must be a number must be a number")
  @property
  def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0

Matthew = Student("Matthew","McDevitt", 22, 33)

# Matthew.output()
print(Matthew)
