# Name: Jaelon Mendoza
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()

    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")
    practice_graph.add_edge("B", "D")
    practice_graph.add_edge("C", "D")
    practice_graph.add_edge("C", "F")
    practice_graph.add_edge("D", "E")
    practice_graph.add_edge("D", "F")

    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()

    rj.add_edge("Nurse", "Juliet")
    rj.add_edge("Juliet", "Tybalt")
    rj.add_edge("Juliet", "Capulet")
    rj.add_edge("Juliet", "Romeo")
    rj.add_edge("Juliet", "Friar Laurence")
    rj.add_edge("Tybalt", "Capulet")
    rj.add_edge("Capulet", "Escalus")
    rj.add_edge("Capulet", "Paris")
    rj.add_edge("Friar Laurence", "Romeo")
    rj.add_edge("Romeo", "Benvolio")
    rj.add_edge("Romeo", "Montague")
    rj.add_edge("Romeo", "Mercutio")
    rj.add_edge("Benvolio", "Montague")
    rj.add_edge("Montague", "Escalus")
    rj.add_edge("Escalus", "Mercutio")
    rj.add_edge("Escalus", "Paris")
    rj.add_edge("Mercutio", "Paris")
    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    fofset = set()

    for i in graph.neighbors(user):
        for j in graph.neighbors(i):
            if (j != user) and (j not in graph.neighbors(user)):
                fofset.add(j)
    return fofset


def common_friends(graph, user1, user2):
    """Finds and returns the set of friends user1 and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a string representing one user
        user2: a string representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """

    return set(graph.neighbors(user1)) & set(graph.neighbors(user2))


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """

    cf_dic = {}
    for i in graph.neighbors(user):
        for j in graph.neighbors(i):
            if j not in graph.neighbors(user) and (j != user):
                if j not in cf_dic.keys():
                    cf_dic[j] = 1
                else:
                    cf_dic[j] += 1
    return cf_dic


def number_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    keys = map_with_number_vals
    keys = sorted(keys.items(), key=itemgetter(0))
    keys = sorted(keys, key=itemgetter(1), reverse=True)
    keys = [i for i, j in keys]
    return keys


def rec_number_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a string

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """

    friendrec = number_of_common_friends_map(graph, user)
    orderdhomies = number_map_to_sorted_list(friendrec)
    return orderdhomies


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    influ_map = {i: None for i in friends_of_friends(graph, user)}

    for i in influ_map:
        sums = 0.0
        for j in common_friends(graph, user, i):
            sums = sums + 1.0/sum(1 for items in friends(graph, j))
            influ_map[i] = sums
    return influ_map


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    fr = influence_map(graph, user)
    current_rec = number_map_to_sorted_list(fr)
    return current_rec


###
#  Problem 5
###

def get_facebook_graph():
    """Builds and returns the facebook graph
    """

    # (Your Problem 5 code goes here.)
    facebook = nx.Graph()
    facebook_file = open("facebook-links-small.txt", "r")
    facebook_line = facebook_file.readlines()
    for line in facebook_line:
        data = line.split()
        facebook.add_edge(int(data[0]), int(data[1]))
    return facebook


def main():
    # practice_graph = get_practice_graph()
    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Comment out this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()
    diff_list = []
    same_list = []
    for user in rj.nodes():
        com_rec = (rec_number_common_friends(rj, user))
        influ_rec = (recommend_by_influence(rj, user))
        if com_rec == influ_rec:
            same_list.append(user)
        else:
            diff_list.append(user)
    print("Unchanged Recommendations:", sorted(same_list))
    print("Changed Recommendations:", sorted(diff_list))
    ###
    #  Problem 5
    ###

    facebook = get_facebook_graph()  # Calls the facebook graph

    # assert len(facebook.nodes()) == 63731
    # assert len(facebook.edges()) == 817090

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    fb = facebook.nodes()
    sorted_fb = sorted(fb, key=int)
    common_dict = {}
    for x in sorted_fb:
        if x % 1000 == 0:
            friend = rec_number_common_friends(facebook, x)
            print(str(x) + " (by num_common_friends): "
                  + str(friend[:10]))
            common_dict[x] = friend[:10]
    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    influence_dict = {}
    for x in sorted_fb:
        if x % 1000 == 0:
            friend = recommend_by_influence(facebook, x)
            print(str(x) + " (by influence): " + str(friend[:10]))
            influence_dict[x] = friend[:10]
    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    same = []
    different = []
    for key in common_dict:
        if common_dict[key] == influence_dict[key]:
            same.append(key)
        else:
            different.append(key)
    print("Same: " + str(len(same)))
    print("Different: " + str(len(different)))


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
