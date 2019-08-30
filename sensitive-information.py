class Patient:

  def __init__(self, ssn, birthdate, health_acct_num, firstname, lastname):
    self.__ssn = ssn
    self.__birth_date = birthdate
    self.__health_acct_number = health_acct_num
    self.__first_name = firstname
    self.__last_name = lastname

  def __str__(self):
    return f'{self.full_name} is a patient here and has a ssn of {self.__ssn}, an account number of {self.__health_acct_number} and lives at {self.__address}'

#The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.
  @property
  def ssn(self):
    try:
      return self.__ssn
    except AttributeError:
      return 0

  @property
  def birth_date(self):
    try:
      return self.__birth_date
    except AttributeError:
      return 0

  @property
  def health_acct_number(self):
    try:
      return self.__health_acct_number
    except AttributeError:
      return 0

  @property
  def full_name(self):
    try:
      return self.__first_name + " " + self.__last_name
    except AttributeError:
      return 0

  @property
  def address(self):
    try:
      return self.__address
    except AttributeError:
      return 0

  @address.setter # The setter
  def address(self, new_address):
    if type(new_address) is str:
      self.__address = new_address
    else: raise TypeError('Please provide a name for the firstname')

Matthew = Patient("083-76-1565", "03/21/1997", "08-455-43332-23", "Matthew", "McDevitt")


Matthew.address = "2350 12th Ave S"



print(Matthew)



