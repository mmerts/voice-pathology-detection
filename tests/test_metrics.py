import numpy as np
from sklearn.metrics import balanced_accuracy_score, f1_score

from vpd.eval import metrics as E


def test_metrics_small_example():
    y = np.array([1, 1, 1, 1, 0, 0])
    p = np.array([1, 1, 1, 0, 0, 1])
    assert E.confusion(y, p) == (3, 1, 1, 1)
    assert E.sensitivity(y, p) == 0.75
    assert E.specificity(y, p) == 0.5
    assert E.uar(y, p) == 0.625


def test_metrics_match_sklearn():
    rng = np.random.default_rng(0)
    y, p = rng.integers(0, 2, 300), rng.integers(0, 2, 300)
    np.testing.assert_allclose(E.uar(y, p), balanced_accuracy_score(y, p))
    np.testing.assert_allclose(E.f1(y, p), f1_score(y, p))
