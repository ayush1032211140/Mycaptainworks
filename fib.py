# Get the number of Fibonacci numbers to generate from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Initialize a list to store the Fibonacci sequence
fibonacci_sequence = []

# Generate the Fibonacci sequence
for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b

# Display the generated Fibonacci sequence
print(f"The first {n} Fibonacci numbers are: {fibonacci_sequence}")
