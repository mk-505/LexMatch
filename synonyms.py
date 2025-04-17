import math
import re


def cosine_similarity(vec1, vec2):
    # find common words in both vectors
    common_words = set(vec1.keys()) & set(vec2.keys())

    dot_product = 0

    # sum up the product of common words' values
    for key in common_words:
        dot_product += vec1[key] * vec2[key]

    def norm(vec):
        sum_of_squares = 0.0
        for x in vec:
            sum_of_squares += vec[x] * vec[x]
        return math.sqrt(sum_of_squares)

    # calculate the product of norms as denominator
    denominator = norm(vec1) * norm(vec2)

    # cosine similarity -> without division by zero
    return dot_product / denominator if denominator != 0 else 0


def build_semantic_descriptors(sentences):
    d = {}

    # go through each sentence
    for sentence in sentences:
        processed_words = set()
        unique_words_in_sentence = set(sentence)

        # process each word in the sentence
        for word in sentence:
            if word not in d:
                d[word] = {}

            # avoid processing the same word more than once
            if word not in processed_words:
                for other_word in unique_words_in_sentence:
                    if word != other_word:
                        d[word][other_word] = d[word].get(other_word, 0) + 1
                processed_words.add(word)
    return d


def build_semantic_descriptors_from_files(filenames):
    all_sentences = []

    # read and process each file
    for filename in filenames:
        with open(filename, "r", encoding="latin1") as file:
            text = file.read()

            # clean up text
            text = re.sub(r'[\-—:;]', ' ', text)
            text = re.sub(r'[!?]', '.', text)
            sentences = text.split(".")

            # split sentences into words
            for sentence in sentences:
                words = re.sub(r'[,]', '', sentence).lower().split()
                if words:
                    all_sentences.append(words)

    return build_semantic_descriptors(all_sentences)

# handle errors in similarity calculation


def similarity_fn(vec1, vec2):
    try:
        similarity = cosine_similarity(vec1, vec2)
        return similarity
    except Exception:  # errors
        return -1


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_similarity = -1  # start with the lowest similarity
    most_similar = None  # no similar word yet

    # descriptor for the main word
    word_descriptor = semantic_descriptors.get(word, {})

    # compare with each choice
    for choice in choices:
        choice_descriptor = semantic_descriptors.get(choice, {})
        similarity = similarity_fn(word_descriptor, choice_descriptor)

        # is a better match found?
        if similarity > max_similarity or most_similar is None:
            max_similarity = similarity
            most_similar = choice

    return most_similar

# similarity test based on a file


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct_guesses = 0
    total_questions = 0

    with open(filename, "r", encoding="latin1") as file:
        for line in file:
            words = line.strip().split()
            if len(words) < 2:  # skip if invalid
                continue

            target_word, correct_answer, *choices = words
            guess = most_similar_word(
                target_word, choices, semantic_descriptors, similarity_fn)

            # count correct guesses
            if guess == correct_answer:
                correct_guesses += 1

            total_questions += 1

    # calculate and return the accuracy percentage
    if total_questions > 0:
        return (correct_guesses / total_questions) * 100
    else:
        return 0.0  # return 0 if no valid questions are found


if __name__ == "__main__":
    sem_descriptors = build_semantic_descriptors_from_files(
        ["wp.txt", "sw.txt"])
    res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
    print(res, "of the guesses were correct")
