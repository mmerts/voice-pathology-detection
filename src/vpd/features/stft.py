"""Short-time analysis: pre-emphasis, framing, windowing and STFT (lecture L6).

Implement every function with NumPy only (no librosa, no scipy.signal.stft).
Check your work with:  pytest tests/test_stft.py
"""
import numpy as np


def pre_emphasis(x: np.ndarray, alpha: float = 0.97) -> np.ndarray:
    """Return y[n] = x[n] - alpha * x[n-1] for n >= 1, and y[0] = x[0]."""
    # TODO: İpucu — döngü (for) gerekmez; NumPy dilimleme (slicing) ile x[1:] ve x[:-1] kullan.
    raise NotImplementedError


def hamming(N: int) -> np.ndarray:
    """Symmetric Hamming window: w[n] = 0.54 - 0.46 cos(2*pi*n / (N-1)), n = 0..N-1."""
    # TODO: n = 0..N-1 dizisini oluştur ve formülü uygula. (np.hamming'i KULLANMA; test onunla karşılaştırıyor.)
    raise NotImplementedError


def frame_signal(x: np.ndarray, frame_len: int, hop: int) -> np.ndarray:
    """Split x into overlapping frames, shape (n_frames, frame_len).

    n_frames = 1 + (len(x) - frame_len) // hop  (no padding; leftover samples are dropped).
    Frame i starts at sample i * hop.
    """
    # TODO: 1) n_frames'i hesapla.
    # TODO: 2) Her çerçevenin başlangıç indeksini bul (i * hop).
    # TODO: 3) Çerçeveleri (n_frames, frame_len) boyutlu bir diziye koy.
    #          (Önce for döngüsüyle yaz; çalışınca istersen indeks matrisiyle vektörleştir.)
    raise NotImplementedError


def stft(x: np.ndarray, fs: int, frame_ms: float = 25.0, hop_ms: float = 10.0,
         n_fft: int = 512) -> np.ndarray:
    """Complex STFT, shape (n_frames, n_fft // 2 + 1).

    frame_len = round(frame_ms * fs / 1000), hop = round(hop_ms * fs / 1000).
    Each frame is multiplied by hamming(frame_len), zero-padded to n_fft samples and
    transformed with the FFT; only the non-negative frequencies (bins 0..n_fft/2) are kept.
    """
    # TODO: 1) ms -> örnek sayısı (frame_len, hop).
    # TODO: 2) frame_signal ile çerçevele, hamming ile pencerele.
    # TODO: 3) Her çerçevenin FFT'si: np.fft.rfft(..., n=n_fft) sıfır doldurmayı (zero-padding) kendisi yapar.
    raise NotImplementedError


def power_spectrum(X: np.ndarray, n_fft: int) -> np.ndarray:
    """Periodogram |X|^2 / n_fft (same shape as X, real-valued)."""
    # TODO
    raise NotImplementedError
