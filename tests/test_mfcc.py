import numpy as np
import pytest
from scipy.fft import dct

from vpd.features import mfcc as M
from vpd.features.stft import pre_emphasis, stft, power_spectrum

FS = 16000


def test_mel_scale():
    f = np.array([0.0, 700.0, 1000.0, 4000.0])
    np.testing.assert_allclose(M.mel_to_hz(M.hz_to_mel(f)), f, rtol=1e-10, atol=1e-9)
    assert abs(M.hz_to_mel(1000.0) - 1000.0) < 0.5


def test_mel_filterbank_properties():
    fb = M.mel_filterbank(n_mels=40, n_fft=512, fs=FS)
    assert fb.shape == (40, 257)
    assert (fb >= 0).all() and fb.max() <= 1 + 1e-9
    assert (fb.sum(axis=1) > 0).all()            # no empty filter
    assert np.all(np.diff(fb.argmax(axis=1)) >= 0)  # centres move up in frequency


def test_mel_filterbank_matches_librosa():
    librosa = pytest.importorskip("librosa")
    ref = librosa.filters.mel(sr=FS, n_fft=512, n_mels=40, htk=True, norm=None)
    np.testing.assert_allclose(M.mel_filterbank(40, 512, FS), ref, atol=1e-6)


def test_dct_ii_matches_scipy():
    X = np.random.default_rng(0).standard_normal((7, 40))
    np.testing.assert_allclose(M.dct_ii(X, 13), dct(X, type=2, norm="ortho", axis=-1)[:, :13],
                               atol=1e-10)


def test_mfcc_pipeline():
    x = np.random.default_rng(1).standard_normal(FS)
    C = M.mfcc(x, FS, n_mfcc=13, n_mels=40)
    P = power_spectrum(stft(pre_emphasis(x, 0.97), FS, 25, 10, 512), 512)
    ref = dct(np.log(P @ M.mel_filterbank(40, 512, FS).T + 1e-10), type=2, norm="ortho", axis=1)
    assert C.shape == (P.shape[0], 13)
    np.testing.assert_allclose(C, ref[:, :13], atol=1e-8)


def test_deltas_of_ramp_and_constant():
    T = 20
    ramp = np.tile(np.arange(T, dtype=float)[:, None], (1, 3))   # c_t = t
    d = M.deltas(ramp, N=2)
    assert d.shape == ramp.shape
    np.testing.assert_allclose(d[2:T - 2], 1.0)                  # slope 1 inside
    np.testing.assert_allclose(M.deltas(np.ones((T, 3)), N=2), 0.0)


def test_deltas_match_librosa_inside():
    librosa = pytest.importorskip("librosa")
    C = np.random.default_rng(2).standard_normal((30, 13))
    ref = librosa.feature.delta(C.T, width=5, order=1).T
    np.testing.assert_allclose(M.deltas(C, N=2)[2:-2], ref[2:-2], atol=1e-8)
