import os
import shutil
from torchvision import datasets, transforms

dataset_path = 'C:/hash/herb_dataset'
clean_path = 'C:/hash/herb_dataset_clean'

os.makedirs(clean_path, exist_ok=True)

# Copy only valid class folders (skip __MACOSX and hidden)
for cls in os.listdir(dataset_path):
    cls_path = os.path.join(dataset_path, cls)
    if os.path.isdir(cls_path) and not cls.startswith('__'):
        shutil.copytree(cls_path, os.path.join(clean_path, cls), dirs_exist_ok=True)

# Now use ImageFolder safely
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

full_dataset = datasets.ImageFolder(clean_path, transform=transform)
print("Dataset loaded with classes:", full_dataset.classes)
