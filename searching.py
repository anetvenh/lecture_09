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


def pattern_search(sequence, pattern):
    """
    Searches pattern in sequence.

    :param sequence: (str) sequence to search pattern in
    :param pattern: (str) pattern to search
    :return output: (set) set of positions of first letter of pattern in sequence
    """
    positions = set()

    for i in range(len(sequence)-len(pattern)+1):
        subsequence = sequence[i:(i+len(pattern))]
        match = True

        for lttr_subseq, lttr_patt in zip(subsequence, pattern):
            if lttr_subseq != lttr_patt:
                match = False
                break
        if match:
            positions.add(i)


    return positions


def main():
    sequence = read_data("sequential.json", "dna_sequence")
    print(pattern_search(sequence, "ATA"))

if __name__ == '__main__':
    main()