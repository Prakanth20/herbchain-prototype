import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
import matplotlib.pyplot as plt
import numpy as np
import os

# === Paths ===
dataset_path = 'C:/hash/herb_dataset_clean'

# === Transformations ===
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# === Load dataset ===
full_dataset = datasets.ImageFolder(dataset_path, transform=transform)
print("Classes detected:", full_dataset.classes)

# === Split 80/20 train/val ===
train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size
train_dataset, val_dataset = random_split(full_dataset, [train_size, val_size])

# === DataLoaders ===
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

print(f"Training samples: {len(train_dataset)}")
print(f"Validation samples: {len(val_dataset)}")

# === Preview 4 sample images ===
data_iter = iter(train_loader)
images, labels = next(data_iter)

fig, axes = plt.subplots(1, 4, figsize=(12, 3))
for i in range(4):
    img = images[i].numpy().transpose((1, 2, 0))  # C,H,W -> H,W,C
    axes[i].imshow(img)
    axes[i].set_title(full_dataset.classes[labels[i]])
    axes[i].axis('off')
plt.show()
