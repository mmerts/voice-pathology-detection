import numpy as np

from vpd.features import stft as S


def test_pre_emphasis():
    x = np.array([1.0, 2.0, 3.0, 4.0])
    np.testing.assert_allclose(S.pre_emphasis(x, 0.5), [1.0, 1.5, 2.0, 2.5])


def test_hamming_matches_numpy():
    for N in (5, 400, 401):
        np.testing.assert_allclose(S.hamming(N), np.hamming(N), atol=1e-12)


def test_frame_signal_shape_and_content():
    x = np.arange(10.0)
    F = S.frame_signal(x, frame_len=4, hop=3)
    assert F.shape == (3, 4)
    np.testing.assert_array_equal(F[0], [0, 1, 2, 3])
    np.testing.assert_array_equal(F[2], [6, 7, 8, 9])


def test_stft_matches_numpy_rfft():
    rng = np.random.default_rng(0)
    fs = 16000
    x = rng.standard_normal(fs // 2)
    X = S.stft(x, fs, frame_ms=25, hop_ms=10, n_fft=512)
    L, H = 400, 160
    assert X.shape == (1 + (len(x) - L) // H, 257)
    ref = np.fft.rfft(x[3 * H: 3 * H + L] * np.hamming(L), 512)
    np.testing.assert_allclose(X[3], ref, rtol=1e-9, atol=1e-9)


def test_stft_sine_peak_bin():
    fs, f = 16000, 1000.0
    t = np.arange(fs) / fs
    X = S.stft(np.sin(2 * np.pi * f * t), fs, n_fft=512)
    assert np.argmax(np.abs(X).mean(axis=0)) == round(f * 512 / fs)


def test_power_spectrum():
    X = np.array([[3 + 4j, 0j]])
    np.testing.assert_allclose(S.power_spectrum(X, 5), [[5.0, 0.0]])
