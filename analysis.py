"""
* Name: Jaelon Mendoza
* Date: 02/14/2023
* CSE 160, Winter 2023
* Homework 4
* Description:
* Collaboration:
"""

from kmeans import get_closest_centroid
from utils import load_centroids, read_data, assert_equals


# ----------------------------------------------------------
# PROBLEMS FOR STUDENTS


def update_assignment(list_of_points, labels, centroids_dict):
    """Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "labels".

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            labels = [2, 1, 3]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                              "centroid2": [2, 2, 2, 2]}
            print(update_assignment(list_of_points, labels, centroids_dict))
        Output:
            {'centroid1': [2, 3], 'centroid2': [1]}
    """

    new_dictionary = {}
    for x in range(0, len(list_of_points)):
        lop_list = list_of_points[x]
        labels_list = labels[x]
        nearest_centroid = get_closest_centroid(lop_list, centroids_dict)
        if nearest_centroid not in new_dictionary:
            new_dictionary[nearest_centroid] = []
        new_dictionary[nearest_centroid].append(labels_list)
    return new_dictionary


def majority_count(labels):
    """Return the count of the majority labels in the label list

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list

    Example:
        Code:
            labels = [0, 3, 3, 2, 2, 3, 4, 5, 5, 5, 4, 3, 2, 2, 2, 2]
            print(majority_count(labels))
        Output:
            6
    """
    maj_count = 0
    for x in range(len(labels)):
        label_current = labels[x]
        maj_current = labels.count(label_current)
        if (maj_current >= maj_count):
            maj_count = maj_current
        else:
            maj_count = maj_count
    return maj_count


def accuracy(list_of_points, labels, centroids_dict):
    """Calculate the accuracy of the algorithm. You should use
    update_assignment and majority_count (that you previously implemented)

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a float representing the accuracy of the algorithm

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            labels = [2, 1, 3]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                              "centroid2": [2, 2, 2, 2]}
            print(accuracy(list_of_points, labels, centroids_dict))
        Output:
            0.6666666666666666
    """
    new_dictionary = update_assignment(list_of_points, labels, centroids_dict)
    max_seen = 0
    things = 0
    accuracy = 0.0
    for x in new_dictionary.values():
        max_seen += majority_count(x)
        things += len(x)
    accuracy = float((max_seen)/(things))
    return accuracy


# ----------------------------------------------------------
# HELPER FUNCTIONS
def setup_for_tests():
    """Creates are returns data for testing analysis methods.

    Returns: data, a list of data points
             labels, numeric labels for each data point
             centroids_dict1, three 4D centroids
             centroids_dict2, three non-random 4D centroids
                with poor starting values
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    list_of_points = [
            [-1.01714716,  0.95954521,  1.20493919,  0.34804443],
            [-1.36639346, -0.38664658, -1.02232584, -1.05902604],
            [1.13659605, -2.47109085, -0.83996912, -0.24579457],
            [-1.48090019, -1.47491857, -0.6221167,  1.79055006],
            [-0.31237952,  0.73762417,  0.39042814, -1.1308523],
            [-0.83095884, -1.73002213, -0.01361636, -0.32652741],
            [-0.78645408,  1.98342914,  0.31944446, -0.41656898],
            [-1.06190687,  0.34481172, -0.70359847, -0.27828666],
            [-2.01157677,  2.93965872,  0.32334723, -0.1659333],
            [-0.56669023, -0.06943413,  1.46053764,  0.01723844]
        ]
    labels = [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    centroids_dict1 = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [-0.71767545, 1.2309971, -1.00348728, -0.38204247],
            "centroid3": [-1.71767545, 0.29971, 0.00328728, -0.38204247],
        }
    centroids_dict2 = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [10, 10, 10, 10],
            "centroid3": [-10, 1, -10, 10],
        }
    return list_of_points, labels, centroids_dict1, centroids_dict2


# ----------------------------------------------------------
# TESTS
def test_update_assignment():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    (list_of_points, labels,
     centroids_dict1, centroids_dict2) = setup_for_tests()

    # test with centroids_dict1
    answer = {'centroid3': [0, 1, 2, 1, 2, 2, 0], 'centroid1': [0],
              'centroid2': [1, 0]}

    assert_equals(answer,
                  update_assignment(list_of_points, labels, centroids_dict1))

    # test with centroids_dict2
    answer = {'centroid1': [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]}
    assert_equals(answer,
                  update_assignment(list_of_points, labels, centroids_dict2))

    # test to make sure parameters remains unchanged
    # If you're failing this test,
    # make sure your code doesn't modify the parameters passed in
    (list_of_points_copy, labels_copy,
     centroids_dict1_copy, centroids_dict2_copy) = setup_for_tests()
    assert_equals(list_of_points_copy, list_of_points)
    assert_equals(labels_copy, labels)
    assert_equals(centroids_dict1_copy, centroids_dict1)
    assert_equals(centroids_dict2_copy, centroids_dict2)

    print("test_update_assignment passed")


def test_majority_count():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # single
    assert_equals(6, majority_count([0, 0, 0, 0, 0, 0]))
    assert_equals(5, majority_count([1, 0, 0, 0, 0, 0]))
    assert_equals(5, majority_count([0, 1, 1, 1, 1, 1]))

    # mixed
    assert_equals(4, majority_count([0, 0, 1, 1, 0, 0]))
    assert_equals(4, majority_count([0, 2, 2, 2, 3, 3, 0, 1, 1, 0, 0]))

    # tied max count
    assert_equals(4, majority_count([0, 2, 2, 2, 0, 2, 0, 0]))

    # test with labels outside of 1-10
    assert_equals(6,
                  majority_count(["cat", "cat", "cat", "cat", "cat", "cat"]))

    print("test_majority_count passed")


def test_accuracy():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    (list_of_points, labels,
     centroids_dict1, centroids_dict2) = setup_for_tests()

    # test with centroids_dict1
    expected = 0.5
    received = accuracy(list_of_points, labels, centroids_dict1)
    assert_equals(expected, received)

    # test with centroids_dict2
    expected = 0.4
    received = accuracy(list_of_points, labels, centroids_dict2)
    assert_equals(expected, received)

    # test to make sure parameters remains unchanged
    # If you're failing this test,
    # make sure your code doesn't modify the parameters passed in
    (list_of_points_copy, labels_copy,
     centroids_dict1_copy, centroids_dict2_copy) = setup_for_tests()
    assert_equals(list_of_points_copy, list_of_points)
    assert_equals(labels_copy, labels)
    assert_equals(centroids_dict1_copy, centroids_dict1)
    assert_equals(centroids_dict2_copy, centroids_dict2)

    print("test_accuracy passed")


def main_test():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    test_update_assignment()
    test_majority_count()
    test_accuracy()
    print("all tests passed.")


if __name__ == "__main__":
    centroids = load_centroids("mnist_final_centroids.csv")
    # Consider exploring the centroids data here

    # Uncomment the line below for Part 2 Step 2, 3, and 4:
    main_test()

    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))

# 1. What happened to the centroids? Why are there fewer than 10?
# Answer: maybe because they are not updated?
#
# 2. What's the accuracy of the algorithm on MNIST? By looking at the
# centroids, which digits are easier to be distinguished by the algorithm,
# and which are harder?
# Answer: the centroids and the numbers don't allign and they are very blurry.
