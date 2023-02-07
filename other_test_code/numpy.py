import numpy as np

def similarity(v1, v2):
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)

    if n1 < 1e-6 or n2 < 1e-6:
        return 0.0
    else:
        return np.dot(v1, v2) / n1 / n2

def word_similarity(model, w1, w2):
    return similarity(model.get_word_vector(w1), model.get_word_vector(w2))

def sentence_similarity(model, t1, t2):
    return similarity(model.get_sentence_vector(t1), model.get_sentence_vector(t2))