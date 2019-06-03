"""
Дан массив целых чисел. Написать функцию, которая определяет, содержит
ли массив какие-либо дубликаты. Возвращает True если содержит дубликаты,
и возвращает False, если не содержит. В массиве могут быть данные False или True.
"""

# Если
#   contains_duplicates = [1, 2, 3, 1]
# то
#   contains_duplicates(example_list) = True

# Если
#   contains_duplicates = [1, 2, 3, 1, False, False]
# то
#   contains_duplicates(example_list) = True

# Если
#   contains_duplicates = [1, 23, 213, 125152, True]
# то
#   contains_duplicates(example_list) = False

# Если
#   contains_duplicates = []
# то
#   contains_duplicates(example_list) = False

def contains_duplicates(example_list: list) -> bool:
    id_list = [id(i) for i in example_list]
    return len(set(id_list)) != len(example_list)

example_list = [1, 2, 3, 1]

print(contains_duplicates(example_list))   

