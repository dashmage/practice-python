"""
Compare the element lookup times between lists and sets.

Accessing an element in a set is significantly faster as it's implemented through
hash tables allowing for O(1) complexity for lookups.
"""

import random
import time

num_elements = 10000000

print("generating random values")
elements = [random.randint(1, num_elements) for _ in range(num_elements)]
print("finished generation")

random_list = elements
random_set = set(elements)

random_element = random.choice(elements)

start_time = time.time()
check_element_in_list = random_element in random_list
end_time = time.time()
list_access_time = end_time - start_time

start_time = time.time()
check_element_in_set = random_element in random_set
end_time = time.time()
set_access_time = end_time - start_time

print(f"Time taken to check if element is in the list: {list_access_time} seconds")
print(f"Time taken to check if an element is in the set: {set_access_time} seconds")
