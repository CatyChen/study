class person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"name:{self.name},age:{self.age},gender:{self.age} :我在吃")
    def drink(self):
        print(f"name:{self.name},age:{self.age},gender:{self.age} :我在喝")
    def run(self):
        print(f"name:{self.name},age:{self.age},gender:{self.age} :我在吃")

Lily = person("Lily",15,"女")
Tom =person("Tom",21,"男")
print(Lily.name)
Lily.eat()
Tom.run()
