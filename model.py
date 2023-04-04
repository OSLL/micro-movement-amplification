from torch import nn
from models.magnet import MagNet

def make_net(config):
    net = None
    if config.model == "resnet":
        net = MagNet

    print(net)
    return net()