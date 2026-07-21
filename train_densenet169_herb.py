import os
import shutil
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
import matplotlib.pyplot as plt
from PIL import Image

# =======================
# 1️⃣ Paths
# =======================
zip_path = 'C:/hash/herb_dataset.zip'           # If you still have zip (optional)
dataset_path = 'C:/hash/herb_dataset'          # Extracted dataset
clean_path = 'C:/hash/herb_dataset_clean'      # Clean dataset (no __MACOSX)

# =======================
# 2️⃣ Clean dataset
# =======================
os.makedirs(clean_path, exist_ok=True)
for cls in os.listdir(dataset_path):
    cls_path = os.path.join(dataset_path, cls)
    if os.path.isdir(cls_path) and not cls.startswith('__'):
        shutil.copytree(cls_path, os.path.join(clean_path, cls), dirs_exist_ok=True)
print(f"✅ Dataset cleaned. Clean path: {clean_path}")

# =======================
# 3️⃣ Transformations
# =======================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# =======================
# 4️⃣ Load dataset
# =======================
full_dataset = datasets.ImageFolder(clean_path, transform=transform)
print("Classes detected:", full_dataset.classes)

# =======================
# 5️⃣ Split train/val
# =======================
train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size
train_dataset, val_dataset = random_split(full_dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

print(f"Training samples: {len(train_dataset)}")
print(f"Validation samples: {len(val_dataset)}")

# =======================
# 6️⃣ Load DenseNet169
# =======================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.densenet169(pretrained=True)
num_classes = len(full_dataset.classes)
model.classifier = nn.Linear(model.classifier.in_features, num_classes)
model = model.to(device)
print("✅ DenseNet169 model ready.")

# =======================
# 7️⃣ Loss and Optimizer
# =======================
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)

# =======================
# 8️⃣ Training loop
# =======================
num_epochs = 5  # adjust as needed
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    print(f"Epoch {epoch+1}/{num_epochs}, Training Loss: {running_loss/len(train_loader):.4f}")

    # Validation
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    val_acc = 100 * correct / total
    print(f"Validation Accuracy: {val_acc:.2f}%\n")

# =======================
# 9️⃣ Save the model
# =======================
torch.save(model.state_dict(), 'densenet169_herb.pth')
print("✅ Model saved as densenet169_herb.pth")

# =======================
# 10️⃣ Preview 4 training images
# =======================
data_iter = iter(train_loader)
images, labels = next(data_iter)

fig, axes = plt.subplots(1, 4, figsize=(12, 3))
for i in range(4):
    img = images[i].numpy().transpose((1, 2, 0))
    axes[i].imshow(img)
    axes[i].set_title(full_dataset.classes[labels[i]])
    axes[i].axis('off')
plt.show()

# =======================
# 11️⃣ Test on a new image
# =======================
def predict_image(img_path):
    model.eval()
    img = Image.open(img_path)
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])
    img_tensor = transform(img).unsqueeze(0).to(device)
    output = model(img_tensor)
    _, pred_class = torch.max(output, 1)
    print("Predicted class:", full_dataset.classes[pred_class.item()])

# Example usage:
# predict_image('C:/hash/new_herb.jpg')
