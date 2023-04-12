import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    # Easy to calculate case: 5 numbers, clean percentages.
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])

    # Obscure and hard (by hand) to calculate frequencies
    input = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
             144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    actual = fd.ones_and_tens_digit_histogram(input)
    expected = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
                0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
                0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
                0.047619047619047616]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])


# write other test functions here
def test_mean_squared_error():
    numbers1 = [1, 4, 9]
    numbers2 = [6, 5, 4]
    result = fd.mean_squared_error(numbers1, numbers2)
    assert type(result) == float
    expected_output = 17
    if result != expected_output:
        print(f"Actual output: {result}")
        print(f"Expected output: {expected_output}")
    assert result == expected_output
    print("Test passed!")


def test_calculate_mse_with_uniform():
    votes = fd.extract_election_votes("election-iran-2009.csv", ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    histogram = fd.ones_and_tens_digit_histogram(votes)
    result = fd.calculate_mse_with_uniform(histogram)
    assert type(result) == float
    expected_output = 0.0007395833333333335
    if result != expected_output:
        print(f"Actual output: {result}")
        print(f"Expected output: {expected_output}")
    assert result == expected_output
    print("Test passed!")


def main():
    test_ones_and_tens_digit_histogram()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()


if __name__ == "__main__":
    main()
