import random

# Parameters for the Gaussian distribution
mu = 0      # Mean
sigma = 5   # Standard deviation

# Generate a random number from the Gaussian distribution
random_value = random.gauss(mu, sigma)

print("Random value from Gaussian distribution:", random_value)
