"""Mel filterbank, log-mel spectrogram, MFCC and delta features (lectures L6, L9).

NumPy only. Check your work with:  pytest tests/test_mfcc.py
"""
import numpy as np

from .stft import pre_emphasis, stft, power_spectrum


def hz_to_mel(f):
    """HTK mel scale: m = 2595 * log10(1 + f / 700). Works on scalars and arrays."""
    # TODO
    raise NotImplementedError


def mel_to_hz(m):
    """Inverse of hz_to_mel."""
    # TODO: hz_to_mel formülünü f için çöz.
    raise NotImplementedError


def mel_filterbank(n_mels: int, n_fft: int, fs: int, fmin: float = 0.0,
                   fmax: float | None = None) -> np.ndarray:
    """Triangular mel filterbank, shape (n_mels, n_fft // 2 + 1).

    Construction (same as librosa.filters.mel(..., htk=True, norm=None)):
      * bin frequencies: f_k = linspace(0, fs/2, n_fft//2 + 1)
      * n_mels + 2 edge frequencies, equally spaced on the MEL scale between fmin and fmax
        (fmax defaults to fs/2), converted back to Hz: e_0 < e_1 < ... < e_{n_mels+1}
      * filter i rises linearly from 0 at e_i to 1 at e_{i+1} and falls back to 0 at e_{i+2}:
            w_i(f) = max(0, min((f - e_i) / (e_{i+1} - e_i), (e_{i+2} - f) / (e_{i+2} - e_{i+1})))
        evaluated at every bin frequency f_k (no rounding of edges to bins).
    """
    # TODO: 1) Bin frekanslarını oluştur.
    # TODO: 2) Mel ekseninde eşit aralıklı n_mels+2 nokta -> Hz'e çevir.
    # TODO: 3) Her filtre için yükselen ve inen kenarı hesapla, minimumunu al, 0'ın altını kes.
    raise NotImplementedError


def log_mel_spectrogram(P: np.ndarray, fb: np.ndarray, eps: float = 1e-10) -> np.ndarray:
    """Natural log of the mel energies: log(P @ fb.T + eps), shape (n_frames, n_mels).

    P is a power spectrum of shape (n_frames, n_fft//2 + 1).
    """
    # TODO
    raise NotImplementedError


def dct_ii(X: np.ndarray, n_out: int) -> np.ndarray:
    """Orthonormal DCT-II along the last axis, keeping the first n_out coefficients.

    For an input row x[0..N-1]:
        c[k] = s_k * sum_n x[n] * cos(pi * k * (2n + 1) / (2N)),
        s_0 = sqrt(1/N), s_k = sqrt(2/N) for k >= 1.
    (Equals scipy.fft.dct(X, type=2, norm='ortho')[..., :n_out]; do NOT call scipy here.)
    """
    # TODO: (n_out, N) boyutlu bir kosinüs matrisi kur, ölçek katsayılarıyla çarp, X ile çarp.
    raise NotImplementedError


def mfcc(x: np.ndarray, fs: int, n_mfcc: int = 13, n_mels: int = 40, frame_ms: float = 25.0,
         hop_ms: float = 10.0, n_fft: int = 512, alpha: float = 0.97) -> np.ndarray:
    """MFCCs of a signal, shape (n_frames, n_mfcc).

    Pipeline: pre_emphasis(alpha) -> stft -> power_spectrum -> mel_filterbank(n_mels, fmin=0,
    fmax=fs/2) -> log_mel_spectrogram (eps=1e-10) -> dct_ii, keep n_mfcc coefficients.
    """
    # TODO: Yukarıdaki fonksiyonları sırayla birleştir.
    raise NotImplementedError


def deltas(C: np.ndarray, N: int = 2) -> np.ndarray:
    """Delta (time-derivative) features of C, shape (n_frames, n_coeffs).

    Regression formula over frames t-N .. t+N:
        d_t = sum_{n=1..N} n * (c_{t+n} - c_{t-n}) / (2 * sum_{n=1..N} n^2)
    At the edges, missing frames are replaced by repeating the first / last frame.
    """
    # TODO: 1) C'yi zaman ekseninde başa ve sona N kez ilk/son çerçeveyi tekrarlayarak doldur (np.pad, mode='edge').
    # TODO: 2) Formülü uygula.
    raise NotImplementedError
