import numpy as np
from scipy.linalg import solve_toeplitz
from scipy.signal import lfilter

from vpd.features import lpc as L


def test_autocorr_small():
    np.testing.assert_allclose(L.autocorr(np.array([1.0, 2.0, 3.0]), 2), [14.0, 8.0, 3.0])


def test_levinson_matches_toeplitz_solve():
    x = np.random.default_rng(0).standard_normal(400)
    p = 10
    r = np.array([x[: len(x) - k] @ x[k:] for k in range(p + 1)])
    a, err = L.levinson_durbin(r, p)
    ref = solve_toeplitz(r[:p], r[1:p + 1])
    np.testing.assert_allclose(a, ref, rtol=1e-8, atol=1e-10)
    np.testing.assert_allclose(err, r[0] - ref @ r[1:p + 1], rtol=1e-8)


def test_lpc_recovers_ar2_and_residual():
    a_true = np.array([1.3, -0.6])          # stable AR(2): s[n] = e[n] + 1.3 s[n-1] - 0.6 s[n-2]
    e = np.random.default_rng(1).standard_normal(20000)
    s = lfilter([1.0], [1.0, -a_true[0], -a_true[1]], e)
    a, _ = L.lpc(s, 2)
    np.testing.assert_allclose(a, a_true, atol=0.05)
    np.testing.assert_allclose(L.lpc_residual(s, a_true), e, atol=1e-9)


def test_formants_from_known_poles():
    fs = 16000
    targets = [(500.0, 80.0), (1500.0, 120.0), (2500.0, 160.0)]
    poles = []
    for F, B in targets:
        r, th = np.exp(-np.pi * B / fs), 2 * np.pi * F / fs
        poles += [r * np.exp(1j * th), r * np.exp(-1j * th)]
    A = np.real(np.poly(poles))             # [1, -a_1, ..., -a_p]
    F, B = L.formants(-A[1:], fs, n=3)
    np.testing.assert_allclose(F, [t[0] for t in targets], atol=1.0)
    np.testing.assert_allclose(B, [t[1] for t in targets], atol=1.0)
