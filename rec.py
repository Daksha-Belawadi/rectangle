import sys

# Check if two input values are provided
if len(sys.argv) == 3:
    length = float(sys.argv[1])
    breadth = float(sys.argv[2])
    print("Using user-provided values:")
else:
    print("No input values – using default values")
    length = 10
    breadth = 5

# Calculate area
area = length * breadth

print("---- Area of Rectangle ----")
print("Length:", length)
print("Breadth:", breadth)
print("Area:", area)
print("---------------------------")
