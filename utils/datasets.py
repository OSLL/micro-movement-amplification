from utils.constants import FRAME_AMP
from torchvision.io import read_image
from torch.utils.data import Dataset
import os


class AmplifierDataset(Dataset):
    def __init__(self, img_dir, transform=None, target_transform=None):
        self.img_dir = img_dir
        self.transform = transform

    def __len__(self):
        return 1  # TODO: check lens

    def __getitem__(self, idx):
        img_folder_path = os.path.join(self.img_dir, f"imgs{idx}")
        images = []
        for i in range(3):
            images.append(read_image(f"{img_folder_path}/frame{chr(65 + i)}.jpg"))
        amp_img = read_image(f"{img_folder_path}/{FRAME_AMP}")
        return images, amp_img
