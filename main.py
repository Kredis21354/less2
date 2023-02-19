class Tree:
  height = 5
  leafs = 21461
  age = 10
  colortrumps = "brown"
  colorleafs = "green"

  def __init__(self, type):
    self.type = type

  def get_older(self):
    self.age += 1

  def leafs_left(self):
    self.leafs -= 1

my_tree = Tree("Maple")

print(my_tree.age)
my_tree.get_older()
print(my_tree.age)

print(my_tree.leafs)
my_tree.leafs_left()
print(my_tree.leafs)

print(my_tree.type)

