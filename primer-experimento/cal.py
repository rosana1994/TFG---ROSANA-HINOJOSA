import scipy.stats as stats

total_sequences = 100000
probability_of_failure = 0.002

# Calculate the expected number of sequences that fail at least one test
expected_failed_sequences = total_sequences * (1 - (1 - probability_of_failure) ** 15)

print(f"Expected number of sequences that fail at least one test: {expected_failed_sequences:.2f}")