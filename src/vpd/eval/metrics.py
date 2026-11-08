"""Binary classification metrics (1 = pathological = positive class).

Check with:  pytest tests/test_metrics.py
"""
import numpy as np


def confusion(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[int, int, int, int]:
    """Return (TP, FN, FP, TN)."""
    # TODO
    raise NotImplementedError


def sensitivity(y_true, y_pred) -> float:
    """Recall of the pathological class: TP / (TP + FN)."""
    # TODO
    raise NotImplementedError


def specificity(y_true, y_pred) -> float:
    """Recall of the healthy class: TN / (TN + FP)."""
    # TODO
    raise NotImplementedError


def uar(y_true, y_pred) -> float:
    """Unweighted average recall: mean of sensitivity and specificity (primary metric)."""
    # TODO
    raise NotImplementedError


def f1(y_true, y_pred) -> float:
    """F1 score of the pathological class: 2TP / (2TP + FP + FN)."""
    # TODO
    raise NotImplementedError
