# скрипт для обучения
import os
import time
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torch.utils.tensorboard import SummaryWriter

from config import Config
from model import make_net
from models.magnet import MagNet
from data import get_gen_ABC
from callbacks import save_model, gen_state_dict

config = Config()
# cudnn.benchmark = True

net = make_net()
device = "cuda" if torch.cuda.is_available() else "cpu"
writer = SummaryWriter()
writer.add_graph(net)

if config.pretrained_weights:
    net.load_state_dict(gen_state_dict(config.pretrained_weights))

criterion = nn.L1Loss().to(device)

optimizer = optim.Adam(net.parameters(), lr=config.lr, betas=config.betas)
