# examples for use of ZIP method
names = ["Damian", "Patryk", "Wojtek", "Adam"]
age = [20, 30, 25, 22]
colors = ["Green", "Blue", "Black", "White", "Pink"]

x = list(zip(names, age, colors))
print(x)

x1 = dict(zip(names, age))
print(x1)

for names, age, colors in zip(names, age, colors):
    if age < 30:
        print(names)