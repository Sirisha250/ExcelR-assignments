def calculate_sum_of_evens(n):
    even_sum = 0
    for number in range(1, n + 1):
        if number % 2 == 0: 
            even_sum += number
    return even_sum

try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a number greater than 0.")
    else:
        result = calculate_sum_of_evens(n)
        print(f"The sum of all even numbers between 1 and {n} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
