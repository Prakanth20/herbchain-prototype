import os
import random
import torch
from torchvision import models, transforms
from PIL import Image

# ----- CONFIG -----
DATASET_PATH = "C:/hash/herb_dataset_clean"
MODEL_PATH = "densenet169_herb.pth"

# ----- LOAD MODEL -----
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.densenet169(weights=None)
num_features = model.classifier.in_features
model.classifier = torch.nn.Linear(num_features, 7)  # 7 classes
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()
model.to(device)

# ----- TRANSFORM -----
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# ----- PICK RANDOM IMAGE -----
classes = os.listdir(DATASET_PATH)
chosen_class = random.choice(classes)
class_path = os.path.join(DATASET_PATH, chosen_class)
image_file = random.choice([f for f in os.listdir(class_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))])
image_path = os.path.join(class_path, image_file)

print(f"✅ Random Test Image: {image_path}")

# ----- PREDICTION -----
image = Image.open(image_path).convert("RGB")
img_tensor = transform(image).unsqueeze(0).to(device)
with torch.no_grad():
    outputs = model(img_tensor)
    probs = torch.nn.functional.softmax(outputs, dim=1)
    confidence, pred_class = torch.max(probs, 1)

print(f"✅ Predicted Class: {pred_class.item()} | Confidence: {confidence.item()*100:.2f}%")
