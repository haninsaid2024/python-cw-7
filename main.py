class person:
    name = 'haneen'
    age = 15

    def is_adult(person):
        if person.age >18:
           print('you have too much responsibilit')
        elif person.age < 18:
            print('lucky')
first_person = person()
print(person.name)
print(person.age)
first_person.is_adult()
    
class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age 
    def __str__(self):
        return f'my name is {self.name}and i am{self.age}'

first_person = person("haneen" , 15)  
print(first_person) 