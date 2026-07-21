import os
import torch
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
import torch.optim as optim
from PIL import Image

# ----- CONFIG -----
DATASET_PATH = "C:/hash/herb_dataset_clean"
MODEL_PATH = "densenet169_herb.pth"
TEST_IMAGE = "C:/hash/sample_herb.jpg"  # <-- put any sample image path here
BATCH_SIZE = 16
EPOCHS = 5
LR = 0.001

# ----- DATASET -----
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

dataset = datasets.ImageFolder(DATASET_PATH, transform=transform)
class_names = dataset.classes
print(f"✅ Classes: {class_names}")

# Split into train & val (80/20)
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# ----- MODEL -----
model = models.densenet169(weights="DEFAULT")
num_features = model.classifier.in_features
model.classifier = nn.Linear(num_features, len(class_names))

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# ----- TRAINING -----
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print(f"✅ Training on: {device}")

for epoch in range(EPOCHS):
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

    print(f"Epoch [{epoch+1}/{EPOCHS}] Loss: {running_loss/len(train_loader):.4f}")

# ----- SAVE MODEL -----
torch.save(model.state_dict(), MODEL_PATH)
print(f"✅ Model saved to {MODEL_PATH}")

# ----- RELOAD MODEL -----
reloaded_model = models.densenet169(weights="DEFAULT")
reloaded_model.classifier = nn.Linear(num_features, len(class_names))
reloaded_model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
reloaded_model.eval()
print("✅ Model reloaded successfully")

# ----- PREDICT SINGLE IMAGE -----
if os.path.exists(TEST_IMAGE):
    def predict_image(img_path):
        image = Image.open(img_path).convert("RGB")
        img_tensor = transform(image).unsqueeze(0).to(device)
        with torch.no_grad():
            outputs = reloaded_model(img_tensor)
            probs = torch.nn.functional.softmax(outputs, dim=1)
            confidence, pred_class = torch.max(probs, 1)
        print(f"✅ Prediction: {class_names[pred_class]} (Confidence: {confidence.item()*100:.2f}%)")

    predict_image(TEST_IMAGE)
else:
    print(f"⚠ TEST_IMAGE not found: {TEST_IMAGE}")
