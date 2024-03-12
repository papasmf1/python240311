class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name
    
    def printInfo(self):
        print("ID:", self.id)
        print("Name:", self.name)


class Manager(Person):
    def __init__(self, person_id, name, title):
        super().__init__(person_id, name)
        self.title = title
    
    def printInfo(self):
        super().printInfo()
        print("Title:", self.title)


class Employee(Person):
    def __init__(self, person_id, name, skill):
        super().__init__(person_id, name)
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()
        print("Skill:", self.skill)


if __name__ == "__main__":
    # Person 클래스 테스트
    print("Person 클래스 테스트:")
    person1 = Person(1, "John")
    person1.printInfo()
    print()

    # Manager 클래스 테스트
    print("Manager 클래스 테스트:")
    manager1 = Manager(2, "Alice", "Senior Manager")
    manager1.printInfo()
    print()

    # Employee 클래스 테스트
    print("Employee 클래스 테스트:")
    employee1 = Employee(3, "Bob", "Python")
    employee1.printInfo()
    print()

    # 추가적인 테스트 코드
    print("추가적인 테스트 코드:")

    # Manager 클래스의 title 테스트
    print("Manager 클래스의 title 테스트:")
    manager2 = Manager(4, "Carol", "Junior Manager")
    manager2.printInfo()
    print()

    # Employee 클래스의 skill 테스트
    print("Employee 클래스의 skill 테스트:")
    employee2 = Employee(5, "Dave", "Java")
    employee2.printInfo()
    print()

    # Person 클래스의 id와 name 테스트
    print("Person 클래스의 id와 name 테스트:")
    person2 = Person(6, "Emma")
    person2.printInfo()
    print()

    # Manager 클래스와 Employee 클래스의 printInfo() 메서드 테스트
    print("Manager 클래스와 Employee 클래스의 printInfo() 메서드 테스트:")
    person3 = Manager(7, "Frank", "Team Lead")
    person3.printInfo()
    person4 = Employee(8, "Grace", "C++")
    person4.printInfo()
    print()

    # Manager 클래스와 Employee 클래스의 상속 테스트
    print("Manager 클래스와 Employee 클래스의 상속 테스트:")
    print(isinstance(manager1, Person))  # Manager는 Person의 하위 클래스여야 함
    print(isinstance(employee1, Person))  # Employee는 Person의 하위 클래스여야 함
    print()

    # Manager 클래스와 Employee 클래스의 속성 테스트
    print("Manager 클래스와 Employee 클래스의 속성 테스트:")
    print(hasattr(manager1, 'title'))  # Manager 클래스에는 title 속성이 있어야 함
    print(hasattr(employee1, 'skill'))  # Employee 클래스에는 skill 속성이 있어야 함
    print()

    # 다형성(polymorphism) 테스트
    print("다형성(polymorphism) 테스트:")
    for person in [manager1, employee1, person1]:
        person.printInfo()
        print()
