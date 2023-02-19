class Tree:
  height = 5
  leafs = 21461
  age = 10
  colortrumps = "brown"
  colorleafs = "green"

  def __init__(self):
    print("")

  def get_older(self):
    self.age += 1

my_tree = Tree()

print(my_tree.age)

my_tree.get_older()

print(my_tree.age)

my_tree.get_older()

print(my_tree.age)

my_tree.get_older()

print(my_tree.age)

my_tree.get_older()

print(my_tree.age)

my_tree.get_older()

print(my_tree.age)