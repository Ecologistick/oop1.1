class Goose:
  eggs = 0
  voice = 'Гуси гогочут' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def eat(self, food):
    self.weight += food
    self.eggs += food // 2
  
  def colect(self):
    print('Собрано', self.eggs, 'яиц')
    self.eggs = 0

  def song(self):
    print(self.voice)

white = Goose('Белый', 3)
gray = Goose('Серый', 4)

class Cow:
  milk = 0
  voice = 'Коровы мычат' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self, food):
    self.weight += food
    self.milk += food // 2
  
  def colect(self):
    print('Собрано', self.milk, 'литров молока')
    self.milk = 0

  def song(self):
    print(self.voice)

manka = Cow('Манька', 400)

class Sheep:
  wool = 0
  voice = 'Овцы блеют' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self, food):
    self.weight += food
    self.wool += food // 2
  
  def colect(self):
    print('Собрано', self.wool, 'килограммов шерсти')
    self.wool = 0

  def song(self):
    print(self.voice)

lamb = Sheep('Барашек', 100)
curly = Sheep('Кудрявый', 90)

class Chicken:
  eggs = 0
  voice = 'Курица кудахчет' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self, food):
    self.weight += food
    self.eggs += food // 2
  
  def colect(self):
    print('Собрано', self.eggs, 'яиц')
    self.eggs = 0

  def song(self):
    print(self.voice)

coco = Chicken('Ко-ко', 2)
kuka = Chicken('Кукареку', 1)

class Goat:
  milk = 0
  voice = 'Козы блеют' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def eat(self, food):
    self.weight += food
    self.milk += food // 2
  
  def colect(self):
    print('Собрано', self.milk, 'литров молока')
    self.milk = 0

  def song(self):
    print(self.voice)
  
horns = Goat('Рога', 70)
hooves = Goat('Копыта', 90)

class Duck:
  eggs = 0
  voice = 'Утка крякает' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def eat(self, food):
    self.weight += food
    self.eggs += food // 2
  
  def colect(self):
    print('Собрано', self.eggs, 'яиц')
    self.eggs = 0

  def song(self):
    print(self.voice)

mallard = Duck('Кряква', 1)

animals =(white, gray, manka, lamb, curly, coco, kuka, horns, hooves, mallard)

max = 0
name_max = ''
for animal in animals:
  if animal.weight > max:
    max = animal.weight
    name_max = animal.name
print(name_max)

total_weight = 0
for animal in animals:
  total_weight += animal.weight
print('Общий вес всех животных', total_weight)