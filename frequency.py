"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string as s


def get_word_list(file_name):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    processed_lines = []
    table = str.maketrans(s.punctuation,32*" ")
    for line in lines:
        processed_line = line.translate(table).strip().lower()
        words = processed_line.split()
        processed_lines.extend(words)

    return processed_lines


def get_top_n_words(word_list, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequently occurring
    """
    word_counts = dict()
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1

    ordered_by_frequency = sorted(word_counts.items(), key=lambda item:item[1], reverse=True)

    most_common_words = []
    for word, freq in ordered_by_frequency[:n]:
        most_common_words.append(word)

    return most_common_words


if __name__ == "__main__":
    word_list = get_word_list('AliceInWonderland.txt')
    top_hundred = get_top_n_words(word_list, 100)
    print(top_hundred)
