# Data

Audio and features are **not** committed (see `.gitignore`). Expected layout:

```
data/
  raw/svd/        # archives downloaded from Zenodo
  raw/voiced/     # files downloaded from PhysioNet
  interim/svd/    # .wav files converted from .nsp (normal-pitch /a/ only)
  features/       # cached .npy features
```

## Saarbrücken Voice Database (SVD)

- Zenodo record: https://zenodo.org/records/16874898 (DOI 10.5281/zenodo.16874898), CC BY 4.0.
- The full release is about 38 GB. Only the normal-pitch /a/ recordings are needed: start with
  `healthy.zip` and the per-diagnosis archives, and do not download `data.zip` (17.9 GB) until you
  know whether it is needed.
- Audio is in `.nsp` format; the Zenodo page links a converter:
  https://github.com/UMEssen/stimmdatenbank-converter
- TODO: after downloading, describe here the folder layout, the file-naming scheme, and where
  speaker ID, sex, age, and diagnosis are stored. `src/vpd/data/svd.py` depends on this.

Cite: M. Pützer and W. J. Barry, *Saarbrücken Voice Database* (v2), Zenodo, 2008.

## VOICED

- PhysioNet: https://physionet.org/content/voiced/1.0.0/ (Open Data Commons Attribution License v1.0).
- 208 recordings (150 pathological, 58 healthy), 5 s sustained /a/, 8 kHz.
- Used only as an external test set (protocol P2).

Cite: U. Cesari *et al.*, "A new database of healthy and pathological voices,"
*Computers & Electrical Engineering*, vol. 68, pp. 310–321, 2018.
