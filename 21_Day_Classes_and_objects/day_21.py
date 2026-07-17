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
class Statistics:
    def __init__(self, data):
        self.data = data
    def count(self):
        return len(self.data)
    def sum(self):
        total = 0
        for i in self.data:
            total += i
        return total
    def min(self):
        minimum = self.data[0]
        for i in self.data:
            if i < minimum:
                minimum = i
        return minimum
    def max(self):
        maximum = self.data[0]
        for i in self.data:
            if i > maximum:
                maximum = i
        return maximum
    def range(self):
        return self.max() - self.min()
    def mean(self):
        return self.sum() / self.count()
    def median(self):
        sorted_data = sorted(self.data)
        if self.count() % 2 == 1:
            return sorted_data[self.count() // 2]
        else:
            median1 = sorted_data[self.count() / 2 - 1]
            median2 = sorted_data[self.count() / 2]
            return (median1 + median2) / 2
    def mode(self):
        frequency = {}
        for i in self.data:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        # mode = max(frequency, key=frequency.get)  # 找 value 最大的 key
        # 更容易理解的写法
        max_count = 0
        mode = None
        for num in frequency:
            if frequency[num] > max_count:
                max_count = frequency[num]
                mode = num
        # 或者
        # for num, count in frequency.items():
        #     if count > max_count:
        #         max_count = count
        #         mode = num
        return (mode, max_count)
    def var(self):
        mean = self.mean()
        squared_diff = 0
        for i in self.data:
            squared_diff += (i - mean) ** 2
        variance = squared_diff / self.count()
        return variance
    def std(self):
        return round(self.var() ** 0.5, 1)
    def freq_dist(self):
        frequency = {}
        for i in self.data:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        result = []
        for key, value in frequency.items():
            percentage = value / self.count() * 100
            result.append((percentage, key))
        return sorted(result, reverse=True)

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# Exercises: Level 2
print('\nExercises: Level 2')
print('\n# 1')
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})
    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})
    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income['amount']
        return total
    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense['amount']
        return total
    def account_balance(self):
        return self.total_income() - self.total_expense()
    def account_info(self):
        return f"""
        Name = {self.firstname} {self.lastname}
        Total Income = {self.total_income()}
        Total Expense = {self.total_expense()}
        Balance = {self.account_balance()}
        """
person = PersonAccount('John', 'Smith')
person.add_income = (7000, 'salary')
person.add_income = (2000, 'freelance')
person.add_expense = (3000, 'rent')
person.add_expense = (3000, 'food')
print(person.account_info())