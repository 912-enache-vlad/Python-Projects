class Ingredient:
    def __init__(self, id, name):
        self.id = id
        self.name = name


ingr = Ingredient(100, "Random ingredient")
flour = Ingredient(101, "Flour")

ingr.x = 123

print(ingr.id)
print(ingr.name)
print(ingr.x)

print("Yess")
for i in range(10):
    print(i)
