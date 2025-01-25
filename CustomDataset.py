import numpy as np
import torch
from torch.utils.data import Dataset
import csv

class CustomDataset(Dataset):
    def __init__(self, images_path:str):
        self.labels = []
        self.images = []
        counter = 0
        with open(images_path, mode="r") as numbers:
            csv_file = csv.reader(numbers)
            for lines in csv_file:
                if counter >= 1:
                    self.labels.append(lines[0])
                    self.images.append(lines[1:])
                counter +=1

    def __len__(self) -> int:
        return len(self.labels)
    
    def __getitem__(self, idx:int) -> tuple[int, np.array]:
        image = self.images[idx]
        temp_image = []
        temp_row = []
        for i in range(1,len(image)+1):
            temp_row.append(int(image[i-1]))
            if not i%28:
                temp_image.append(temp_row)
                temp_row = []
        

        return torch.tensor(int(self.labels[idx])), torch.from_numpy(np.array(temp_image))