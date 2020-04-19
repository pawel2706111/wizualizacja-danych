# zadanie 4
# Korzystając z powyższego kodu stwórz kilka instancji klasy Point
# i spróbuj odwołać się do zmiennej counter z poziomu różnych instancji,
# porównując jej wartość dla każdej z nich oraz spróbuj zmienić jej wartość.
class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point()
p2 = Point(1,1)
p3 = Point(-202, 1223)
print('p1.counter:', p1.counter)
print('p2.counter:', p2.counter)
print('p3.counter:', p3.counter)
p1.update('p1')
p2.update('p2')
p3.update('p3')
p1.update('p1_2')
print('p1.counter:', p1.counter)
print('p2.counter:', p2.counter)
print('p3.counter:', p3.counter)
p1.counter.append('dodałem element XD')
print('p1.counter:', p1.counter)
print('p2.counter:', p2.counter)
print('p3.counter:', p3.counter)