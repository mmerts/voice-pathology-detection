import numpy as np

from vpd.data.splits import speaker_folds


def test_speaker_folds_are_speaker_independent():
    rng = np.random.default_rng(0)
    speakers = rng.integers(0, 40, size=200)
    y = (speakers % 3 == 0).astype(int)        # label is a speaker property
    folds = speaker_folds(y, speakers, n_splits=5, seed=0)
    assert len(folds) == 5
    tested = []
    for tr, te in folds:
        assert set(speakers[tr]).isdisjoint(speakers[te])
        assert len(set(y[te])) == 2             # both classes in every test fold
        tested.extend(te.tolist())
    assert sorted(tested) == list(range(len(y)))  # every recording tested exactly once
