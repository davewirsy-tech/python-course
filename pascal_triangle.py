# Function to print Pascal's Triangle
def print_pascals_triangle(n):
   for i in range(n):
       # Print spaces for alignment
       print(" " * (n - i), end="")
       value = 1 # First value in every row is 1
       for j in range(i + 1):
           print(value, end=" ")
           # Update value using the formula: C(line, i) = C(line, i-1) * (line - i + 1) / i
           value = value * (i - j) // (j + 1)
       print() # Move to the next line
# Number of rows
rows = 7890096
print_pascals_triangle(rows)