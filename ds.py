
ex = '16.1 Given a sorted array of positive integers with an empty spot (zero) at the end, insert an element in sorted order.'
print(ex)

s_array = [0, 1, 2, 3, 4, 5, ]
x = 0.5
print(s_array)
for i, v in enumerate(s_array):
    if x <= v:
        s_array[i+1:] = s_array[i:]
        s_array[i] = x
        break
print("including new element")
print(s_array)

ex = '16.1 Given a sorted array of positive integers with an empty spot (zero) at the end, insert an element in sorted order.'
print(ex)

sorted_array = [0, 1, 2, 3, 4, 5, 6]

def reverse(s_array):
    l = len(s_array)
    mid = int(l / 2)
    for i in range(mid):
        cur, inv = i, l - 1 -i
        c_val, inv_val = s_array[cur], s_array[inv]
        s_array[cur] = inv_val
        s_array[inv] = c_val
    return s_array

print("reversed")
print(reverse(sorted_array))


ex = '16.3 Given two lists (A and B) of unique strings, write a program to determine if A is a subset of B. That is, check if all the elements from A are contained in B.'
print(ex)

big = ['a', 'b', 'c', 'd', 'e']
small = ['d', 'e']

def is_subset(b, s):
    l_dict = {}
    for x in b: l_dict[x] = True
    for x in s: 
        if x not in l_dict: 
            return False
    return True

print(is_subset(big, small))

ex = '16.4 You are given a two-dimensional array of sales data where the first column is a product ID and the second column is the quantity. Write a function to take this list of data and return a new two-dimensional array with the total sales for each product ID.'

a1 =  [[211,4],  [262,3],  [211,5],  [216,6]]

def sum_total(a):
    sum_dict = {}
    for x, y in a:
        if x in sum_dict: sum_dict[x] = sum_dict[x] + y
        else: sum_dict[x] = y
    return sum_dict

print(sum_total(a1))

ex = '16.5 Insert an element into a binary search tree (in order). You may assume that the binary search tree contains integers.'
print(ex)
class Tree:
    def __init__(
        self, cargo: int, 
        left=None, 
        right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def insert_node(self, node: Tree):
        if node is None: return False
        if node.cargo < self.cargo:
            if self.left is None:
                self.left = node
                return
            else: self.left.insert_node(node)
        elif node.cargo > self.cargo:
            if self.right is None:
                self.right = node
                return
            else: self.right.insert_node(node)

    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        if self.right is not None:
            self.right.traverse()
        return print(str(self))
    
    def sum(self):
        if self.left is not None:
            return self.cargo + self.left.sum()
        if self.right is not None:
            return self.cargo + self.right.sum()
        return self.cargo + self.cargo + self.cargo

t = Tree(10)
t.insert_node(Tree(5))
t.insert_node(Tree(15))
t.insert_node(Tree(2))
t.traverse()

ex = '16.6 Given a binary search tree which contains integers as values, calculate the sum of all the numbers. jump'

t.sum()














