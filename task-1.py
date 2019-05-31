"""
Дан массив целых чисел. Написать функцию, которая определяет, содержит
ли массив какие-либо дубликаты. Возвращает True если содержит дубликаты,
и возвращает False, если не содержит.
"""

# Если
#   contains_duplicates = [1, 2, 3, 1]
# то
#   contains_duplicates(example_list) = True

# Если
#   contains_duplicates = [1, 23, 213, 125152]
# то
#   contains_duplicates(example_list) = False

# Если
#   contains_duplicates = []
# то
#   contains_duplicates(example_list) = False

def contains_duplicates(example_list):
    return len(set(example_list)) != len(example_list)

example_list = [1, 23, 213, 125152]

print(contains_duplicates(example_list))   
