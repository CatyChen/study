# result =0
# for i in range(101):
#     result=result+i
#     print(result)

class person():
    name="test class"
    sex="F"

    def get_person(self):
        return self.name

print(person.name)
print(person.sex)

p=person()
print(p.name)
print(p.sex)
print(p.get_person())


person.name="Caty"
p.name="Lily"
print(p.name)

p1=person()
print(p1.name)


