"""Speaker-independent, stratified cross-validation folds (protocol P1)."""
import numpy as np


def speaker_folds(y: np.ndarray, speakers: np.ndarray, n_splits: int = 5,
                  seed: int = 0) -> list[tuple[np.ndarray, np.ndarray]]:
    """Return a list of (train_idx, test_idx) index arrays.

    Rules: every speaker's recordings fall into exactly one test fold (no speaker in both
    train and test), and each fold keeps roughly the overall healthy/pathological ratio.
    """
    # TODO: sklearn.model_selection.StratifiedGroupKFold(n_splits, shuffle=True, random_state=seed)
    #       kullan; groups=speakers ver. Dönen indeksleri listeye topla.
    raise NotImplementedError
