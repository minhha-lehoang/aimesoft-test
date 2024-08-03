# Minimum Edit Distance

This folder implements the Minimum Edit Distance (Levenshtein Distance) algorithm and includes unit tests to verify its correctness.

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