from torch.utils.data import DataLoader

from utils.datasets import AmplifierDataset


def get_data_loaders(path_data, batch_size=64, shuffle=True):
    dataset = AmplifierDataset(path_data)
    train_dataloader = DataLoader(dataset,
                                  batch_size=batch_size,
                                  shuffle=shuffle)
    return train_dataloader