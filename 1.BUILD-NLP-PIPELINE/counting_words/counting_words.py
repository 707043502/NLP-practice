import re
import string
def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    text = text.lower()

    pattern = re.compile("<.*?>")
    text = pattern.sub('', text)

    pattern_punc = re.compile("["+string.punctuation+"]")
    text = pattern_punc.sub('', text)
    list_text = text.split()
    for word in list_text:
        counts[word] = counts.get(word, 0) + 1

    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))

        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()