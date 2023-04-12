import utils  # noqa: F401, do not remove if using a Mac
# add your imports BELOW this line
import csv
import matplotlib.pyplot as plt
import random


def ones_and_tens_digit_histogram(numbers):
    '''
    Input:
        a list of numbers.
    Returns:
        a list where the value at index i is the frequency in which digit i
        appeared in the ones place OR the tens place in the input list. This
        returned list will always have 10 numbers (representing the frequency
        of digits 0 - 9).

    For example, given the input list
        [127, 426, 28, 9, 90]
    This function will return
        [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]

    That is, the digit 0 occurred in 20% of the one and tens places; 2 in 30%
    of them; 6, 7, and 8 each in 10% of the ones and tens, and 9 occurred in
    20% of the ones and tens.

    See fraud_detection_tests.py for additional cases.
    '''
    histogram = [0] * 10

    # first fill histogram with counts
    for i in numbers:
        # 1's place
        histogram[i % 10] += 1

        # 10's place
        histogram[i // 10 % 10] += 1

    # normalize over total counts
    for i in range(len(histogram)):
        histogram[i] /= len(numbers) * 2

    return histogram


# Your Set of Functions for this assignment goes in here
def extract_election_votes(filename, column_names):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        votes = []
        for x in reader:
            for y in column_names:
                votes.append(int(x[y].replace(',', '')))
    return votes


def plot_iran_least_digits_histogram(histogram):
    least = [i % 10 for i in range(10)]
    frequen = [histogram[i] for i in least]
    plt.plot(least, frequen, linestyle='-', color='orange', label='iran')
    plt.plot([0, 9], [0.1, 0.1], linestyle='-', color='blue', label='ideal')
    plt.title("Distribution of the last two digits in Iranian dataset")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.legend(loc='upper left')
    plt.xlim(-1, 10)
    plt.xticks(range(10))
    plt.savefig("iran-digits.png")
    plt.show()


def plot_dist_by_sample_size():
    sample_sizes = [10, 50, 100, 1000, 10000]
    random = []
    for x in sample_sizes:
        random.append([random.randint(0, 99) for sample in range(x)])
    histograms = [ones_and_tens_digit_histogram(numbers) for numbers in random]
    plt.plot(range(10), [0.1] * 10, label='ideal')
    for i in range(len(histograms)):
        plt.plot(range(10), histograms[i], label=f"{sample_sizes[i]}randnumbs")
    plt.legend()
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Distribution of last two digits in randomly generated dataset")
    plt.savefig("random-digits.png")


def mean_squared_error(numbers1, numbers2):
    squar_diff = [(n1 - n2) ** 2 for n1, n2 in zip(numbers1, numbers2)]
    return sum(squar_diff) / len(numbers1)


def calculate_mse_with_uniform(histogram):
    n = len(histogram)
    uniform_hist = [1/n]*n
    return mean_squared_error(histogram, uniform_hist)


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    num_samples = 10000
    sample_size = number_of_iran_datapoints
    mse_list = []
    for x in range(num_samples):
        sample = [random.randint(0, 99) for y in range(sample_size)]
        mse = calculate_mse_with_uniform(ones_and_tens_digit_histogram(sample))
        mse_list.append(mse)
    large = sum(1 for mse in mse_list if mse >= iran_mse)
    smal = sum(1 for mse in mse_list if mse < iran_mse)
    p_value = large / num_samples
    print("2009 Iranian election MSE:", iran_mse)
    print("Q of MSEs larger than or equal to the 2009 Iranian election MSE:"
          , large)
    print("Quantity of MSEs smaller than the 2009 Iranian election MSE:", smal)
    print("2009 Iranian election null hypothesis rejection level p:", p_value)


# The code in this function is executed when this
# file is run as a Python program
def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.

    votes = extract_election_votes("election-iran-2009.csv", ["Ahmadinejad", "Rezai" , "Karrubi", "Mousavi"])
    histogram = ones_and_tens_digit_histogram(votes)
    plot_iran_least_digits_histogram(histogram)
    plot_dist_by_sample_size()
    calculate_mse_with_uniform(histogram)
    compare_iran_mse_to_samples(0.000739583333333, 120)


if __name__ == "__main__":
    main()
