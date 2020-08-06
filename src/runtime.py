# # linear O(n) time
# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
# def print_animals(animal_list):
#     for i in range(len(animal_list)):
#         print(animal_list[i])
# # ??? runtime
# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
# def print_animals(animals):
#     for i in range(len(animals)):
#         print(animal_list[i])
#         my_number = 0
#         for _ in range(100000):
#             my_number += 1
# # polynomial O(n^2) time
# # Print a list of all possible animal pairs
# def print_animal_pairs():
#     for animal_1 in animals:
#         for animal_2 in animals:
#             print (f"{animal_1} - {animal_2}")
# # ??? runtime
# def print_animal_triples():
#     # O(?)
#     for animal in animals:
#         print(animal)
#     # O(?)
#     for animal_1 in animals:
#         for animal_2 in animals:
#             for animal_3 in animals:
#                 print (f"{animal_1} - {animal_2} - {animal_3}")
# # logarithmic O(logn) time
# # free all the animals, half at a time
# # (remove them from the array)
# def free_animals(animals):
#     while len(animals) > 0:
#         animals = animals[0: len(animals) // 2]