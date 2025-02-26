my_int = 10
my_float = 3.14
my_complex = 2 + 3j
my_list = [1, 2, 3, "hello", 3.14]
my_tuple = (1, 2, 3, "hello", 3.14)
my_dict = {"name": "Alice", "age": 30}
my_set = {1, 2, 3, 4, 5}
my_bool = True

print("Type of my_int:", type(my_int))
print("Type of my_float:", type(my_float))
print("Type of my_complex:", type(my_complex))
print("Type of my_list:", type(my_list))
print("Type of my_tuple:", type(my_tuple))
print("Type of my_dict:", type(my_dict))
print("Type of my_set:", type(my_set))
print("Type of my_bool:", type(my_bool))

my_int_to_float = float(my_int)
my_float_to_int = int(my_float)  

print("\nConversion:")
print(f"{my_int} converted to float: {my_int_to_float} (Type: {type(my_int_to_float)})")
print(f"{my_float} converted to int: {my_float_to_int} (Type: {type(my_float_to_int)})")
