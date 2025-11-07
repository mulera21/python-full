# list
empty_list = []  # or list()
my_list = [1, 2, 3, 'four', 'five']

print("List:", my_list)

#get single item
first_item = my_list[2]
print("single item", first_item)
# counting start from 0 in programming and -1 from the other end
first_item = my_list[-1]
#this will give last item which is five
print("single item from list", first_item)

#slicing of a list
sub_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(sub_list[2:3])
print(sub_list[1:5])
print(sub_list[:4])
print(sub_list[3:])

#categories of list methods
fruits = ['apple', 'banana', 'cherry']
header = fruits[0]
data = fruits[1:]
print("header:", header)
print("data:", data)

#adding item to a list
fruits.append("mango")   #add single item
print(fruits)
fruits.extend(['orange', 'grape'])  #add multiple items
print(fruits)

#nested list
points = [[2,4],[5,6],[6,7,8]]  #a list inside a list

#looping through a list
for point in points:
    print(point)


# tuple
data = (10, 20, 30, 'forty', 'fifty')  # tuple is immutable
data_pts = ((1,2), (3,4), (5,6))  # nested tuple
print("Tuple:", data)