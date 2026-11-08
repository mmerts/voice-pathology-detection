"""Linear prediction: autocorrelation method, Levinson-Durbin, residual, formants (lecture L7).

Convention used everywhere in this project (the same as in the proposal):
    prediction        s_hat[n] = sum_{k=1..p} a_k * s[n-k]
    residual          e[n]     = s[n] - sum_{k=1..p} a_k * s[n-k]
    inverse filter    A(z)     = 1 - sum_{k=1..p} a_k * z^{-k}

NumPy only (scipy.signal.lfilter is allowed for the residual). Check with:  pytest tests/test_lpc.py
"""
import numpy as np

from .stft import hamming


def autocorr(x: np.ndarray, p: int) -> np.ndarray:
    """Biased autocorrelation r[k] = sum_n x[n] * x[n+k], for k = 0..p (length p+1)."""
    # TODO: Her k için üst üste binen kısımların iç çarpımı (dot product). (np.correlate KULLANMA.)
    raise NotImplementedError


def levinson_durbin(r: np.ndarray, p: int) -> tuple[np.ndarray, float]:
    """Solve the normal equations sum_k a_k r[|i-k|] = r[i] (i = 1..p) with Levinson-Durbin.

    Returns (a, err): a = [a_1, ..., a_p] and the final prediction error
    err = r[0] - sum_k a_k r[k].
    """
    # TODO: Ders notundaki (L7) özyinelemeyi uygula:
    #   E_0 = r[0]
    #   her i = 1..p için: yansıma katsayısı k_i'yi hesapla,
    #   a^{(i)} katsayılarını önceki a^{(i-1)} ile güncelle,
    #   E_i = (1 - k_i^2) * E_{i-1}
    raise NotImplementedError


def lpc(frame: np.ndarray, p: int) -> tuple[np.ndarray, float]:
    """LPC of one frame with the autocorrelation method: window with hamming(len(frame)),
    compute autocorr up to lag p, then levinson_durbin."""
    # TODO
    raise NotImplementedError


def lpc_residual(x: np.ndarray, a: np.ndarray) -> np.ndarray:
    """Inverse-filter x with A(z): e[n] = x[n] - sum_k a_k x[n-k] (zero initial conditions)."""
    # TODO: A(z) katsayı dizisi [1, -a_1, ..., -a_p]; scipy.signal.lfilter(b=..., a=[1.0], x) ile FIR filtre.
    raise NotImplementedError


def formants(a: np.ndarray, fs: int, n: int = 3, fmin: float = 90.0,
             bmax: float = 400.0) -> tuple[np.ndarray, np.ndarray]:
    """Formant frequencies and bandwidths (Hz) from the roots of A(z).

    For each root z with Im(z) > 0:   F = angle(z) * fs / (2*pi),   B = -(fs/pi) * ln|z|.
    Keep roots with F > fmin and B < bmax, sort by F, return the first n.
    If fewer than n remain, pad with np.nan. Returns (F, B), each of length n.
    """
    # TODO: 1) A(z) polinom katsayıları -> np.roots
    # TODO: 2) Üst yarı düzlemdeki kökleri seç, F ve B'yi hesapla.
    # TODO: 3) Filtrele, sırala, n tanesini döndür (eksikse nan ile doldur).
    raise NotImplementedError
