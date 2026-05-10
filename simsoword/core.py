
from simsoword.preprocess import normalize_text
from simsoword.metrics import (
    jaro_winkler_score,
    levenshtein_score
)


VALID_BOUNDARIES = ("easy", "hard")


def get_score(
    word1: str,
    word2: str,
    boundary: str = "easy",
    normalize: bool = True
) -> float:
    """
    Compute similarity score between two words.

    Parameters
    ----------
    word1 : str
    word2 : str
    boundary : str
        'easy' -> Jaro-Winkler
        'hard' -> Levenshtein
    normalize : bool
        Apply preprocessing or not

    Returns
    -------
    float
        Similarity score between 0 and 100
    """

    if boundary not in VALID_BOUNDARIES:
        raise ValueError(
            "boundary must be either 'easy' or 'hard'"
        )

    if normalize:
        word1 = normalize_text(word1)
        word2 = normalize_text(word2)

    if boundary == "easy":
        return jaro_winkler_score(word1, word2)

    return levenshtein_score(word1, word2)


def is_similar(
    word1: str,
    word2: str,
    threshold: float = 80.0,
    boundary: str = "easy",
    normalize: bool = True
) -> bool:
    """
    Check whether two words are similar.

    Returns
    -------
    bool
    """

    score = get_score(
        word1=word1,
        word2=word2,
        boundary=boundary,
        normalize=normalize
    )

    return score >= threshold