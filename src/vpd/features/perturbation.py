"""Source features: F0 by autocorrelation, jitter and shimmer (lecture L8).

NumPy only. Check with:  pytest tests/test_perturbation.py
"""
import numpy as np


def f0_autocorr(frame: np.ndarray, fs: int, fmin: float = 60.0, fmax: float = 400.0,
                voicing_threshold: float = 0.3) -> float:
    """F0 (Hz) of one frame, or 0.0 if the frame is judged unvoiced.

    1. Normalized biased autocorrelation rho[k] = r[k] / r[0], with r[k] = sum_n x[n] x[n+k]
       (no windowing).
    2. Search lags k from ceil(fs / fmax) to floor(fs / fmin) (inclusive) and take the
       lag k* with the largest rho.
    3. If rho[k*] < voicing_threshold return 0.0, else return fs / k*.
    """
    # TODO: Adımları sırayla uygula. (Sessiz çerçevede r[0] = 0 olabilir; o durumda 0.0 döndür.)
    raise NotImplementedError


def jitter_local(periods: np.ndarray) -> float:
    """Local jitter: mean |T_i - T_{i+1}| divided by mean T (dimensionless)."""
    # TODO
    raise NotImplementedError


def shimmer_local(amplitudes: np.ndarray) -> float:
    """Local shimmer: mean |A_i - A_{i+1}| divided by mean A (dimensionless)."""
    # TODO
    raise NotImplementedError


def glottal_cycles(x: np.ndarray, fs: int, f0: float) -> tuple[np.ndarray, np.ndarray]:
    """Period lengths T_i (s) and peak amplitudes A_i of consecutive glottal cycles.

    Week-2 task (no test yet): find one peak per cycle, searching for the next peak
    roughly 1/f0 seconds after the previous one. Periods are the differences of
    consecutive peak times; amplitudes are the peak values.
    """
    # TODO (Hafta 2): Önce ders notundaki yöntemi oku; sonra bir test yazıp bu fonksiyonu doldur.
    raise NotImplementedError
