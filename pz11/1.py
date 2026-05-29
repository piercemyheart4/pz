
# Даны две последовательности. Найти элементы, общие для двух
# последовательностей и их количество.

sequence_a = [1, 5, 3, 8, 12, 5, 7, 9]
sequence_b = [5, 9, 14, 7, 2, 5, 12]

common_elements = [item for item in set(sequence_a) if item in set(sequence_b)]
count_common = len(common_elements)

print("Исходная последовательность A:", sequence_a)
print("Исходная последовательность B:", sequence_b)
print("---")
print("Общие элементы:", common_elements)
print("Количество общих элементов:", count_common)