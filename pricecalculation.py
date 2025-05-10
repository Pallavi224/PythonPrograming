import numpy as np
prices =np.array([100, 200, 300, 400, 500])
# Calculate the mean price
mean_price = np.mean(prices)
# Calculate the median price
median_price = np.median(prices)
# Calculate the standard deviation of prices
std_dev_price = np.std(prices)

# Print the results

print(f"Mean Price: {mean_price}")

print(f"Median Price: {median_price}")
print(f"Standard Deviation of Prices: {std_dev_price}")
# Calculate the maximum price
max_price = np.max(prices)
# Calculate the minimum price

min_price = np.min(prices)
# Print the results
print(f"Maximum Price: {max_price}")
print(f"Minimum Price: {min_price}")
# Calculate the range of prices
price_range = max_price - min_price
# Print the result
print(f"Range of Prices: {price_range}")
# Calculate the variance of prices
variance_price = np.var(prices)
# Print the result
print(f"Variance of Prices: {variance_price}")
# Calculate the coefficient of variation
coefficient_of_variation = (std_dev_price / mean_price) * 100
# Print the result
print(f"Coefficient of Variation: {coefficient_of_variation:.2f}%")
# Calculate the 25th and 75th percentiles
percentile_25 = np.percentile(prices, 25)
percentile_75 = np.percentile(prices, 75)
# Print the results

print(f"25th Percentile: {percentile_25}")
print(f"75th Percentile: {percentile_75}")
# MATRIX OPERATIONS
# Create two matrices
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
matrix_b = np.array([[7, 8, 9], [10, 11, 12]])
# Perform matrix addition
matrix_sum = np.add(matrix_a, matrix_b)
# Perform matrix subtraction
matrix_diff = np.subtract(matrix_a, matrix_b)
# Perform matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b.T)  # Transpose matrix_b for correct multiplication
# Perform matrix division (element-wise)
matrix_division = np.divide(matrix_a, matrix_b)
# Perform matrix
# Perform matrix
# Perform matrix exponentiation
matrix_exponentiation = np.power(matrix_a, 2)
# Print the results
print("Matrix A:")
print(matrix_a)
print("Matrix B:")
print(matrix_b)
print("Matrix Sum:")
print(matrix_sum)
print("Matrix Difference:")
print(matrix_diff)
print("Matrix Product:")
print(matrix_product)