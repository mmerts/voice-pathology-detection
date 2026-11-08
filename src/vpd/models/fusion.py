"""Proposed system: CNN on log-mel excerpts + MLP on handcrafted features, late fusion.

Week 4-5 task. Keep the networks small (the data set is small).
"""
import torch
from torch import nn


class SmallCNN(nn.Module):
    """3 x [Conv2d -> BatchNorm2d -> ReLU -> MaxPool2d], then global average pooling.
    Input: (batch, 1, n_mels, n_frames). Output: an embedding of size emb_dim."""

    def __init__(self, emb_dim: int = 64):
        super().__init__()
        # TODO (Hafta 4)
        raise NotImplementedError

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError


class FeatureMLP(nn.Module):
    """Two-layer MLP on the standardized handcrafted feature vector (MFCC stats, LPC, jitter...)."""

    def __init__(self, in_dim: int, emb_dim: int = 32):
        super().__init__()
        # TODO (Hafta 4)
        raise NotImplementedError

    def forward(self, f: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError


class FusionNet(nn.Module):
    """Concatenate the two embeddings -> Linear -> one logit (sigmoid applied in the loss)."""

    def __init__(self, cnn: SmallCNN, mlp: FeatureMLP):
        super().__init__()
        # TODO (Hafta 5)
        raise NotImplementedError

    def forward(self, spec: torch.Tensor, feats: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError
