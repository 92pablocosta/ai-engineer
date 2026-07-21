class Student:
    """Represents a student."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def introduce(self):
        print(f'Olá! Meu nome é {self.name} e tenho {self.age} anos de idade.')
    

    def have_birthday(self):
        self.age += 1

    
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

aluno1 = Student("Maria", 20)
aluno2 = Student("João", 21)

print(aluno1)
print(aluno2)
aluno1.introduce()
aluno2.introduce()
aluno1.have_birthday()
print(aluno1.__dict__)
