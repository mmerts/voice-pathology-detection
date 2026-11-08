"""Default parameters. They follow Section IV of the proposal (docs/proposal)."""

FS = 16_000            # analysis sampling rate for P1 (Hz)
FS_CROSS = 8_000       # sampling rate for the cross-database experiment P2 (Hz)

PRE_EMPHASIS = 0.97
FRAME_MS = 25.0
HOP_MS = 10.0
N_FFT = 512

N_MELS = 40
N_MFCC = 13
DELTA_N = 2            # deltas use frames t-2 .. t+2

LPC_ORDER = 16         # at 16 kHz; a common rule of thumb is fs/1000 + 2..4
F0_MIN = 60.0          # Hz
F0_MAX = 400.0         # Hz

N_FOLDS = 5
SEED = 0
