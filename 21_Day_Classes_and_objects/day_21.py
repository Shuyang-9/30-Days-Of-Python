class Person:
    pass
print(Person)  # <class '__main__.Person'>

p = Person()
print(p)  # <__main__.Person object at 0x0000020CB0AB8A10>

class Person:
      def __init__ (self, name):
        # self允许将参数附加到类
          self.name = name

p = Person('Asabeneh')
print(p.name)
print(p)

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())


class Person:
      def __init__(self, firstname = 'Asabeneh', lastname = 'Yetayeh', age = 250, country = 'Finland', city = 'Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
p1 = Person()
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman City')
print(p1.person_info())
print(p2.person_info())


class Person:
      def __init__(self, firstname = 'Asabeneh', lastname = 'Yetayeh', age = 250, country = 'Finland', city = 'Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skills(self, skill):
          self.skills.append(skill)
p1 = Person()
p1.add_skills('HTML')
p1.add_skills('CSS')
p1.add_skills('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman City')
print(p1.person_info())
print(p1.firstname)
print(p1.skills)
print(p2.person_info())
print(p2.firstname)
print(p2.skills)


class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        if self.gender == 'male':
            gender = 'He'
        else:
            gender = 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'
# p1 = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
p1 = Person()
p2 = Student('Tom', 'Y', 25, 'US', 'Detroit', 'male')
p3 = Student('Lily', 'H', 30, 'China', 'SH', 'female')
p1.add_skills('HTML')
p1.add_skills('CSS')
p2.add_skills('read')
p2.add_skills('write')
p3.add_skills('run')
p3.add_skills('walk')
print(p1.person_info())
print(p2.person_info())
print(p3.person_info())
print(p1.skills)
print(p2.skills)
print(p3.skills)









# Exercises: Day 21
# Exercises: Level 1
print('\nExercises: Level 1')
print('\n# 1')








# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')







