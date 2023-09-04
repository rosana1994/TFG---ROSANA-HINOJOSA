# Define the number of tests (k) and the significance level (alpha)
k = 15
alpha = 0.01

# Calculate the expected coverage using the formula
expected_coverage = 1 - (1 - alpha)**k

print("Expected Coverage for 15 tests with alpha =", alpha, ":", expected_coverage)
