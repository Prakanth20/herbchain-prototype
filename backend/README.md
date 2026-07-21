# 🌿 Herbal Batch Registration Backend (FastAPI + IPFS)

This repository contains backend examples for registering and validating herbal collection batches.
It includes two versions:

1. **Backend Dev 1** → Basic validation and dummy storage.
2. **Backend Dev 2** → Integration with **IPFS** using [Pinata API](https://www.pinata.cloud/).

---

## 🚀 Features

* **FastAPI**-based backend for quick development and testing
* **Batch registration schema** with:

  * Herb name
  * Collection location (latitude, longitude)
  * Collector ID
  * Collection timestamp
* **Endpoints**:

  * `/validate` → Validate incoming batch data (dummy validation)
  * `/registerBatch` → Register batch (dummy CID or IPFS storage via Pinata)
* **IPFS support** → Store batch metadata permanently on decentralized storage

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/herbal-batch-backend.git
   cd herbal-batch-backend
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install fastapi uvicorn requests
   ```

---

## ▶️ Running the Server

Run either backend version:

### **Backend Dev 1 (Dummy Example)**

```bash
uvicorn backend_dev1:app --reload
```

### **Backend Dev 2 (IPFS + Pinata Integration)**

```bash
uvicorn backend_dev2:app --reload
```

---

## 🔑 Pinata API Setup (for Backend Dev 2)

1. Sign up at [Pinata](https://www.pinata.cloud/).
2. Get your **API Key** and **Secret API Key** from the dashboard.
3. Replace the placeholders in `backend_dev2.py`:

   ```python
   PINATA_API_KEY = "YOUR_PINATA_API_KEY"
   PINATA_SECRET_API_KEY = "YOUR_PINATA_SECRET_API_KEY"
   ```

---

## 📡 Example API Usage

### Validate a Batch (Dev 1 only)

```bash
curl -X POST "http://127.0.0.1:8000/validate" \
-H "Content-Type: application/json" \
-d '{
  "herb_name": "Mint",
  "location": {"latitude": 40.7128, "longitude": -74.0060},
  "collector_id": "collector123",
  "collection_timestamp": "2025-09-20T10:00:00Z"
}'
```

### Register a Batch (Both Dev 1 & Dev 2)

```bash
curl -X POST "http://127.0.0.1:8000/registerBatch" \
-H "Content-Type: application/json" \
-d '{
  "herb_name": "Mint",
  "location": {"latitude": 40.7128, "longitude": -74.0060},
  "collector_id": "collector123",
  "collection_timestamp": "2025-09-20T10:00:00Z"
}'
```

* **Dev 1 Response:** Returns a dummy CID.
* **Dev 2 Response:** Returns the real IPFS CID from Pinata.

---

## 📂 Project Structure

```
.
├── backend_dev1.py   # Basic validation + dummy CID
├── backend_dev2.py   # Pinata IPFS integration
├── README.md         # Project documentation
```

---

## ⚡ Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) – Web framework
* [Uvicorn](https://www.uvicorn.org/) – ASGI server
* [IPFS](https://ipfs.tech/) – Decentralized storage
* [Pinata](https://www.pinata.cloud/) – IPFS API gateway
