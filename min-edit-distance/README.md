# Minimum Edit Distance

This folder implements the Minimum Edit Distance (Levenshtein Distance) algorithm and includes unit tests to verify its correctness.

**Complexity**:
- Time Complexity: `O(m*n)`
- Space Complexity: `O(m*n)`
where `m` and `n` are the lengths of the source and target strings, respectively.

**Some applications**:
- Natural language processing: spell checking, OCR, plagiarism detection, etc.
- Computational biology: DNA/RNA sequence alignment, protein sequence alignment, etc.
- Machine translation: aligning source and target sentences.
- Speech recognition: aligning spoken words with text.

## Structure
```
min-edit-distance 
├── med.py # Contains the implementation of the min_edit_distance function 
├── test_med.py # Contains unit tests for the min_edit_distance function 
└── stanford-med.pdf # Lecture slides from Stanford about Minimum Edit Distance
└── README.md # Documentation
```

## Usage
To use the `min_edit_distance function`, you can import it from the `med.py` file:
    
```python
from med import min_edit_distance

source = "kitten"
target = "sitting"
distance = min_edit_distance(source, target)
print(f"The minimum edit distance between '{source}' and '{target}' is {distance}.")
```

Or you can run the `med.py` file directly from the command line:
```bash
python med.py kitten sitting
```

## Running Tests
To run the unit tests, you can use the following command:
```bash
python -m unittest test_med.py
```