import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]


def linear_search(unordered_nbrs, searched_nbr):
    """
    searches numbers in sequence and counts their frequency

    :param unordered_nbrs: (list) list of unordered numbers to search searched number in
    :param searched_nbr: (int) searched number
    :return output: (dict) dictionary with indexes of searched number as key and frequency as value
    """

    positions = []
    count = 0

    for i, nbr in enumerate(unordered_nbrs):
        if nbr == searched_nbr:
            positions.append(i)
            count += 1

    output = dict()
    output["positions"] = positions
    output["count"] = count
    # output = {"positions" : positions, "count" : count}
    return output


def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    print(linear_search(sequence, 9))

if __name__ == '__main__':
    main()