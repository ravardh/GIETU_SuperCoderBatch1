def create_list_with_array(array_input):
    # Creating a list with an array as input
    list_with_array = [array_input]

    # Creating a list inside the list_with_array to store values
    values_list = []
    list_with_array.append(values_list)

    # Adding values to the inner list as tuples
    values_list.append((10,))
    values_list.append((20,))
    values_list.append((30,))

    return list_with_array

# Example usage:
array_input = [1, 2, 3, 4, 5]
result_list = create_list_with_array(array_input)
print(result_list)  # Output: [[1, 2, 3, 4, 5], [(10,), (20,), (30,)]]
