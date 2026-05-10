import jellyfish


def jaro_winkler_score(word1: str, word2: str) -> float:
    """
    Compute Jaro-Winkler similarity score.

    Returns
    -------
    float
        Similarity percentage between 0 and 100
    """

    score = jellyfish.jaro_winkler_similarity(word1, word2)

    return round(score * 100, 2)


def levenshtein_score(word1: str, word2: str) -> float:
    """
    Compute normalized Levenshtein similarity score.

    Returns
    -------
    float
        Similarity percentage between 0 and 100
    """

    distance = jellyfish.levenshtein_distance(word1, word2)

    max_len = max(len(word1), len(word2))

    if max_len == 0:
        return 100.0

    similarity = (1 - distance / max_len) * 100

    return round(similarity, 2)
