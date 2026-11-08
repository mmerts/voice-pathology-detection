"""Baseline: one diagonal-covariance GMM per class on frame-level MFCC + delta (lecture L11)."""
import numpy as np


class GMMBaseline:
    """Two GMMs (healthy, pathological). Score = sum over frames of
    log p(x_t | pathological) - log p(x_t | healthy)."""

    def __init__(self, n_components: int = 16, seed: int = 0):
        self.n_components = n_components
        self.seed = seed

    def fit(self, frames_per_recording: list[np.ndarray], labels: np.ndarray) -> "GMMBaseline":
        # TODO (Hafta 3): Her sınıfın kayıtlarındaki çerçeveleri birleştir ve
        #   sklearn.mixture.GaussianMixture(covariance_type='diag') ile ayrı ayrı eğit.
        raise NotImplementedError

    def score(self, frames: np.ndarray) -> float:
        """Log-likelihood ratio of one recording (> 0 means 'pathological' is more likely)."""
        # TODO: GaussianMixture.score_samples çerçeve başına log-olabilirlik verir.
        raise NotImplementedError
