# Import necessary libraries
import random
import math

# Define the function to calculate Pi using the Monte Carlo method
def calculate_pi(n_trials, tolerance=1e-6):
    # n_trials: maximum number of iterations to perform
    # tolerance: the convergence criteria to determine when to stop
    
    # Counter for points inside the circle
    points_inside_circle = 0
    
    # List to store estimates of Pi
    pi_estimates = []
    
    for i in range(1, n_trials + 1):
        # Generate random (x, y) point between 0 and 1
        x = random.random()
        y = random.random()

        # Check if the point lies inside the unit circle
        if x ** 2 + y ** 2 <= 1:
            points_inside_circle += 1

        # Estimate the value of Pi
        pi_estimate = 4 * points_inside_circle / i
        pi_estimates.append(pi_estimate)

        # Print the current estimate of Pi
        print(f"Iteration {i}: Estimate of Pi = {pi_estimate}")

        # Check for convergence if we have at least 2 values
        if i > 1:
            # Calculate the difference between consecutive estimates
            diff = abs(pi_estimates[-1] - pi_estimates[-2])

            # Check if the difference is within the specified tolerance
            if diff < tolerance:
                print(f"Converged after {i} iterations with Pi = {pi_estimate}")
                return pi_estimate

    # If it did not converge within the specified iterations, return the last estimate
    print(f"Did not converge within {n_trials} iterations. Final Estimate of Pi = {pi_estimate}")
    return pi_estimate

# Example usage of the function
n = 1000000  # Maximum number of trials to perform
tolerance = 1e-6  # Convergence tolerance
calculate_pi(n, tolerance)  # Run the calculation

# Run the script and observe the printed output to see convergence
