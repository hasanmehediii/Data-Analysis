import numpy as np

random_numbers = np.random.default_rng()

print(random_numbers.integers(1, 10))  # Random integers between 1 and 10
print(random_numbers.random(5))         # Array of 5 random floats between 0 and 1
print(random_numbers.normal(0, 1, 5))   # Array of 5 random numbers from a normal distribution with mean 0 and std 1
print(random_numbers.choice(['apple', 'banana', 'cherry'], size=3))  # Randomly choose 3 fruits from the list
print(random_numbers.permutation(10))   # Random permutation of numbers from 0 to 9
print(random_numbers.shuffle([1, 2, 3, 4, 5]))  # Shuffle the list in place
print(random_numbers.binomial(10, 0.5, 5))  # Array of 5 random numbers from a binomial distribution
print(random_numbers.uniform(1, 10, 5))  # Array of 5 random floats between 1 and 10
print(random_numbers.beta(2, 5, 5))  # Array of 5 random numbers from a beta distribution
print(random_numbers.exponential(1.0, 5))  # Array of 5 random numbers from an exponential distribution
print(random_numbers.gamma(2.0, 2.0, 5))  # Array of 5 random numbers from a gamma distribution
print(random_numbers.poisson(5, 5))  # Array of 5 random numbers from a Poisson distribution with lambda=5
print(random_numbers.multinomial(10, [0.2, 0.5, 0.3], size=3))  # Array of 3 samples from a multinomial distribution

print(random_numbers.integers(low=1, high=100, size=(3, 4)))  # 3x4 array of random integers between 1 and 100
print(random_numbers.random((2, 3)))  # 2x3 array of random floats between 0 and 1
print(random_numbers.normal(loc=0.0, scale=1.0, size=(2, 2)))  # 2x2 array of random numbers from a normal distribution
print(random_numbers.choice(['red', 'green', 'blue'], size=(2, 2)))  # 2x2 array of randomly chosen colors
print(random_numbers.permutation(np.arange(12)).reshape(3, 4))  # 3x4 array of a random permutation of numbers from 0 to 11
print(random_numbers.binomial(n=20, p=0.5, size=(2, 3)))  # 2x3 array of random numbers from a binomial distribution
print(random_numbers.uniform(low=5.0, high=15.0, size=(3, 2)))  # 3x2 array of random floats between 5 and 15

print(random_numbers.beta(a=2.0, b=5.0, size=(2, 2)))  # 2x2 array of random numbers from a beta distribution
print(random_numbers.exponential(scale=1.0, size=(3, 3)))  # 3x3 array of random numbers from an exponential distribution
print(random_numbers.gamma(shape=2.0, scale=2.0, size=(2, 4)))  # 2x4 array of random numbers from a gamma distribution
print(random_numbers.poisson(lam=5.0, size=(4, 2)))  # 4x2 array of random numbers from a Poisson distribution with lambda=5
print(random_numbers.multinomial(n=10, pvals=[0.3, 0.4, 0.3], size=(2, 2)))  # 2x2 array of samples from a multinomial distribution