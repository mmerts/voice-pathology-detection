import numpy as np

from vpd.features import perturbation as P

FS = 16000


def test_f0_of_sine():
    t = np.arange(int(0.04 * FS)) / FS
    assert abs(P.f0_autocorr(np.sin(2 * np.pi * 150.0 * t), FS) - 150.0) < 2.0


def test_f0_unvoiced_noise_and_silence():
    assert P.f0_autocorr(np.random.default_rng(1).standard_normal(640), FS) == 0.0
    assert P.f0_autocorr(np.zeros(640), FS) == 0.0


def test_jitter_and_shimmer():
    T = np.array([0.010, 0.011, 0.010, 0.011])
    np.testing.assert_allclose(P.jitter_local(T), 0.001 / 0.0105)
    np.testing.assert_allclose(P.jitter_local(np.full(5, 0.008)), 0.0)
    A = np.array([1.0, 0.8, 1.0, 0.8])
    np.testing.assert_allclose(P.shimmer_local(A), 0.2 / 0.9)
