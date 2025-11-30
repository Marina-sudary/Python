class User:  # в классе есть -
    age = 0  # -поле age

    def __init__(self, name):  # - конструктор
        print("создалось")
        self.username = name # -поле username (оно инициализируется, когда вызывают конструктор)

    def sayName(self):  # - метод : скажи имя - sayName
        print("имя ", self.username)

    def sayAge(self):  # - метод : скажи возраст - sayAge
        print(self.age)  

    def setAge(self, newAge):
        self.age = newAge      



user1 = User("Alex") # можно обозвать сразу переменную для лучшего понимания, кому она пренадлежит
mark = User("Mark")
anna = User("Anna")

user1.sayName()
user1.sayAge()
user1.setAge(33)
user1.sayAge()
mark.sayName()
anna.sayName()
