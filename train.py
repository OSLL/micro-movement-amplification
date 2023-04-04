# скрипт для обучения
import os
import time
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.backends.cudnn as cudnn
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter

from config import Config
from model import make_net
from models.magnet import MagNet
from data import get_gen_ABC
from callbacks import save_model, gen_state_dict

config = Config()
device = "cuda" if torch.cuda.is_available() else "cpu"
# cudnn.benchmark = True

net = make_net(config)
device = "cuda" if torch.cuda.is_available() else "cpu"
writer = SummaryWriter()
print(net)
#writer.add_graph(net)

if config.pretrained_weights:
    net.load_state_dict(gen_state_dict(config.pretrained_weights))

criterion = nn.L1Loss().to(device)

optimizer = optim.Adam(net.parameters(), lr=config.lr, betas=config.betas)

if not os.path.exists(config.save_dir):
    os.makedirs(config.save_dir)
print('Save_dir:', config.save_dir)

data_loader = get_gen_ABC(config, mode='train')
print('Number of training image couples:', data_loader.data_len)

for epoch in range(1, config.epochs + 1):
    losses, losses_y, losses_texture_AC, losses_texture_BM, losses_motion_BC = [], [], [], [], []

    for idx_load in tqdm(range(0, data_loader.data_len, data_loader.batch_size)):
        # Data Loading
        batch_A, batch_B, batch_C, batch_M, batch_amp = data_loader.gen()

        # G Train
        optimizer.zero_grad()

        y_hat, texture_AC, texture_BM, motion_BC = net(batch_A, batch_B, batch_C, batch_M, batch_amp, mode='train')
        loss_y, loss_texture_AC, loss_texture_BM, loss_motion_BC = criterion(y_hat, batch_M, texture_AC, texture_BM,
                                                                             motion_BC, criterion)

        loss = loss_y + (loss_texture_AC + loss_texture_BM + loss_motion_BC) * 0.1
        writer.add_scalar("loss", loss)
        loss.backward()
        optimizer.step()
