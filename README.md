# Decision Tree Implementation with Information Gain

This repository contains Python code for building a decision tree using information gain as the splitting criterion. The implementation leverages the pandas library for data manipulation and numpy for mathematical operations.

## Features

- **Entropy Calculation**: Function to compute entropy based on input data.
- **Information Gain Calculation**: Function to determine information gain for each feature.
- **Recursive Decision Tree Construction**: Recursive function for constructing a decision tree.

## Usage

1. **Importing Required Libraries**:

    ```python
    import pandas as pd
    import numpy as np
    ```

2. **Feature Ranking**:

    Use the provided functions to rank features based on information gain. The code demonstrates how to rank features using the included dataset and display the ranked features along with their respective information gain values.

3. **Decision Tree Construction**:

    The `recurisve_decision_tree` function constructs a decision tree by recursively splitting based on information gain. It displays each split node and its corresponding information gain, as well as the resulting child nodes.

## Dataset

The provided dataset is extracted from lecture slides and includes attributes such as `Outlook`, `Temperature`, `Humidity`, `Wind`, and the target variable `Class`.

## Requirements

- Python 3.x
- pandas
- numpy
