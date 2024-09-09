def find_missing_numbers(numbers):
    # Input validation
    if not all(isinstance(num, int) for num in numbers):
        return "All elements must be integers."
    
    if len(numbers) == 0:
        return "The list cannot be empty."
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    
    # Find the full range
    full_range = set(range(sorted_numbers[0], sorted_numbers[-1] + 1))
    
    # Find missing numbers
    missing_numbers = full_range - set(sorted_numbers)
    
    return sorted(list(missing_numbers))

# Example usage
numbers = [2, 1, 5, 4, 6, 9, 7, 8, 10]  # The input list
missing_numbers = find_missing_numbers(numbers)
print(missing_numbers)
