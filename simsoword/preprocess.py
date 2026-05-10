import re


def normalize_text(text: str) -> str:
    """
    Normalize input text.

    Operations:
    - Convert to lowercase
    - Remove non a-z characters
    - Reject spaces

    Parameters
    ----------
    text : str
        Input word

    Returns
    -------
    str
        Normalized word
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if len(text)>151:
        raise ValueError("Input length should be less than or equal 150")

    if " " in text:
        raise ValueError("Spaces are not allowed in words")

    text = text.lower()

    # Keep only a-z
    text = re.sub(r"[^a-z]", "", text)

    return text