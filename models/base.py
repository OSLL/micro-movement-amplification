from typing import Any

import torch.nn as nn
from torch import Tensor
import torch.nn.functional as F


class BasicConv2d(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, **kwargs: Any) -> None:
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, bias=False, **kwargs)
        self.bn = nn.BatchNorm2d(out_channels, eps=0.001)

    def forward(self, x: Tensor) -> Tensor:
        x = self.conv(x)
        x = self.bn(x)
        # https://arxiv.org/pdf/1606.08415.pdf
        return F.gelu(x, approximate='tanh')

