# ============================================================
# Gradient Descent-Based Statistical Model
# ============================================================
# Author: Charan V
# Description:
# A Python implementation of gradient descent for a simple
# linear model y_pred = w * x using Mean Squared Error (MSE).
# The model iteratively updates the weight to minimize the error.
# ============================================================


# ------------------------------------------------------------
# Statistical Data
# ------------------------------------------------------------

w = 10.0

# Learning rate controls the size of each weight update.
learning_rate = 0.001

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = [
    8087,
    11549,
    12704,
    9858,
    19000,
    11393,
    13601,
    16055,
    15268,
    16207
]


# ------------------------------------------------------------
# Formula
# ------------------------------------------------------------

def formula(x, y, w):
    """
    Calculate the predicted value, squared error,
    and gradient for one observation.
    """

    # Predicted value
    y_pred = w * x

    # Difference between predicted and actual value
    error = y_pred - y

    # Squared error
    m = error ** 2

    # Gradient of squared error with respect to w
    grad = 2 * x * error

    return m, grad


# ------------------------------------------------------------
# Calculate One Iteration
# ------------------------------------------------------------

def calculate_iteration(x_values, y_values, w, learning_rate):
    """
    Calculate MSE and gradient for all observations
    and update the weight using gradient descent.
    """

    results = []

    # Calculate error and gradient for every data point
    for x_value, y_value in zip(x_values, y_values):

        result = formula(x_value, y_value, w)

        results.append(result)

    # Number of observations
    n = len(x_values)

    # Sum of squared errors
    sum_m = sum(result[0] for result in results)

    # Mean Squared Error
    mse = sum_m / n

    # Average gradient
    avg_grad = sum(result[1] for result in results) / n

    # Gradient descent weight update
    new_w = w - learning_rate * avg_grad

    return results, mse, avg_grad, new_w


# ------------------------------------------------------------
# Closed-Form Solution
# ------------------------------------------------------------

def closed_form_solution(x_values, y_values):
    """
    Calculate the least-squares solution for a linear model
    passing through the origin.

    w* = sum(x*y) / sum(x^2)
    """

    numerator = sum(
        xi * yi
        for xi, yi in zip(x_values, y_values)
    )

    denominator = sum(
        xi ** 2
        for xi in x_values
    )

    return numerator / denominator


# ============================================================
# Run Gradient Descent
# ============================================================

num_iterations = 1000

# Iterations whose results will be displayed
log_at = {1, 2, 3, 10, 100, 500, 1000}


print("=" * 70)
print("GRADIENT DESCENT - STATISTICAL MODEL")
print("=" * 70)

print(
    f"{'Iteration':>10} | "
    f"{'Weight':>12} | "
    f"{'MSE':>15} | "
    f"{'Gradient':>15}"
)

print("-" * 70)


# Perform gradient descent
for i in range(1, num_iterations + 1):

    results, mse, grad, w = calculate_iteration(
        x,
        y,
        w,
        learning_rate
    )

    # Display selected iterations
    if i in log_at:

        print(
            f"{i:>10} | "
            f"{w:>12.4f} | "
            f"{mse:>15.2f} | "
            f"{grad:>15.2f}"
        )


# ============================================================
# Compare with Closed-Form Solution
# ============================================================

w_star = closed_form_solution(x, y)


print("-" * 70)

print(
    f"\nFinal weight using Gradient Descent : {w:.4f}"
)

print(
    f"Optimal weight using Closed Form    : {w_star:.4f}"
)

print("=" * 70)