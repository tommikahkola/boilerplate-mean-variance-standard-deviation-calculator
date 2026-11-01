import numpy as np


def calculate(numbers):
    # The function only works with exactly nine numbers
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Turn the list into a 3 x 3 matrix
    matrix = np.array(numbers).reshape(3, 3)

    # Each statistic gets three results:
    #   axis=0  -> one value per column
    #   axis=1  -> one value per row
    #   no axis -> one value for all nine numbers
    # .tolist() turns NumPy values into normal Python lists and numbers
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations
