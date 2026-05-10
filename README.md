# simsoword

`simsoword` is a lightweight Python package for comparing words using phonetic-aware and edit-distance-based similarity metrics.

The package is designed to determine whether two words are similar based on configurable similarity boundaries and threshold scores.

It provides:

- Jaro-Winkler similarity scoring
- Levenshtein similarity scoring
- configurable threshold matching
- optional text normalization
- simple and intuitive APIs

---

# Motivation

Different similarity algorithms behave differently depending on the use case.

For example:

- `"nite"` and `"night"` sound similar phonetically
- `"color"` and `"colour"` are spelling variants
- `"book"` and `"back"` are structurally different

A single similarity metric is often insufficient.

`simsoword` provides two comparison boundaries:

| Boundary | Algorithm    | Behavior                             |
| -------- | ------------ | ------------------------------------ |
| `easy`   | Jaro-Winkler | More liberal and pronunciation-aware |
| `hard`   | Levenshtein  | More strict and spelling-sensitive   |

This allows users to choose the type of similarity comparison required for their application.

---

# Features

- Lightweight and fast
- Simple API design
- Optional preprocessing pipeline
- Percentage-based similarity scoring
- Threshold-based boolean matching
- Jaro-Winkler similarity
- Levenshtein similarity
- PyPI-ready architecture
- Easy integration into NLP and phonetic applications

---

# Installation

## Install from PyPI

```bash
pip install simsoword
```

---

## Local Development Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/simsoword.git
```

Move into the project directory:

```bash
cd simsoword
```

Install in editable mode:

```bash
pip install -e .
```

---

# Dependencies

`simsoword` currently depends on:

- `jellyfish`

Install manually if needed:

```bash
pip install jellyfish
```

---

# Package Structure

```text
simsoword/
│
├── simsoword/
│   ├── __init__.py
│   ├── core.py
│   ├── metrics.py
│   ├── preprocess.py
│   ├── exceptions.py
│   └── utils.py
│
├── tests/
│   ├── test_preprocess.py
│   ├── test_score.py
│   └── test_match.py
│
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

# Supported Similarity Algorithms

## 1. Jaro-Winkler Similarity

Used when:

```python
boundary="easy"
```

Characteristics:

- More liberal
- Better for realistic pronunciation matching
- Good for fuzzy matching
- Useful for phonetic similarity

Example:

```python
"nite" vs "night"
```

May produce a relatively high similarity score.

---

## 2. Levenshtein Similarity

Used when:

```python
boundary="hard"
```

Characteristics:

- More strict
- Based on edit distance
- Sensitive to spelling changes
- Better for exact structural similarity

---

# Text Normalization

By default:

```python
normalize=True
```

Normalization performs:

- lowercase conversion
- removal of non `a-z` characters
- validation against spaces

---

## Example

### Input

```python
"HeLLo123!!"
```

### Output

```python
"hello"
```

---

# Public APIs

The package currently exposes two primary functions:

```python
get_score()
is_similar()
```

---

# Function Documentation

---

## 1. `get_score()`

Computes similarity score between two words.

---

### Syntax

```python
get_score(
    word1: str,
    word2: str,
    boundary: str = "easy",
    normalize: bool = True
) -> float
```

---

### Parameters

| Parameter   | Type   | Description                |
| ----------- | ------ | -------------------------- |
| `word1`     | `str`  | First input word           |
| `word2`     | `str`  | Second input word          |
| `boundary`  | `str`  | `"easy"` or `"hard"`       |
| `normalize` | `bool` | Apply preprocessing or not |

---

### Returns

```python
float
```

Similarity score between `0` and `100`.

---

### Example

```python
from simsoword import get_score

score = get_score(
    "nite",
    "night"
)

print(score)
```

---

### Example Output

```python
84.72
```

---

# 2. `is_similar()`

Checks whether similarity score exceeds threshold.

---

## Syntax

```python
is_similar(
    word1: str,
    word2: str,
    threshold: float = 80.0,
    boundary: str = "easy",
    normalize: bool = True
) -> bool
```

---

## Parameters

| Parameter   | Type    | Description                |
| ----------- | ------- | -------------------------- |
| `word1`     | `str`   | First input word           |
| `word2`     | `str`   | Second input word          |
| `threshold` | `float` | Matching threshold         |
| `boundary`  | `str`   | `"easy"` or `"hard"`       |
| `normalize` | `bool`  | Apply preprocessing or not |

---

## Returns

```python
bool
```

---

## Example

```python
from simsoword import is_similar

result = is_similar(
    "nite",
    "night",
    threshold=75
)

print(result)
```

---

## Example Output

```python
True
```

---

# Boundary Modes

## Easy Boundary

```python
boundary="easy"
```

Uses:

- Jaro-Winkler similarity

Recommended for:

- phonetic similarity
- fuzzy matching
- pronunciation-aware comparisons

---

## Hard Boundary

```python
boundary="hard"
```

Uses:

- Levenshtein similarity

Recommended for:

- strict spelling comparison
- typo-sensitive matching
- exact textual similarity

---

# Examples

---

## Example 1: Default Comparison

```python
from simsoword import get_score

score = get_score(
    "nite",
    "night"
)

print(score)
```

---

## Example 2: Strict Comparison

```python
from simsoword import get_score

score = get_score(
    "nite",
    "night",
    boundary="hard"
)

print(score)
```

---

## Example 3: Disable Normalization

```python
from simsoword import get_score

score = get_score(
    "Hello!!",
    "hello",
    normalize=False
)
```

---

## Example 4: Boolean Similarity Check

```python
from simsoword import is_similar

result = is_similar(
    "colour",
    "color",
    threshold=70
)

print(result)
```

---

## Invalid Input Types

```python
TypeError:
Input must be a string
```

---

# Version

Current version:

```python
0.1.0
```

---

# Future Roadmap

Planned future features include:

- Soundex support
- Metaphone support
- Double Metaphone support
- multilingual normalization
- configurable preprocessing pipelines
- sentence-level similarity
- CLI support
- custom scoring strategies

---

# Contributing

Contributions are welcome.

Possible contribution areas:

- additional phonetic algorithms
- optimization
- multilingual support
- benchmark datasets
- documentation improvements
- testing improvements

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# Author

Developed by Manish Prajapati.

# Contact

For suggestions, improvements, bug reports, or collaboration opportunities, feel free to reach out.

- Email: mmprajapaty3@gmail.com
- LinkedIn: [Manish Prajapati](https://www.linkedin.com/in/manish-prajapati-3126a31aa/?utm_source=chatgpt.com)

---

# Acknowledgements

This package uses:

- `jellyfish` for similarity algorithms

---

# Keywords

phonetics, fuzzy matching, jaro winkler, levenshtein distance, string similarity, NLP, speech processing, text similarity, pronunciation matching
