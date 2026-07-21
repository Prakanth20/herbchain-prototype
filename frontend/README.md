# 🌿 HerbChain Frontend — Chemical AI

This is the **frontend UI** for **HerbChain**, a prototype that validates and registers Ayurvedic herbs on blockchain with AI-based chemical analysis.
Built with **React + Vite + Tailwind CSS**.

## 🚀 Features

* **Frontend Dev 1 – Scan & Validate**

  * Upload an herb image + metadata (herb name, source, batch ID).
  * Calls backend `/validate` to validate herb metadata.
  * Shows a **demo chemical report** (purity, moisture, adulterants).
  * Previews uploaded herb image.

* **Frontend Dev 2 – Register Batch**

  * Enter herb details, location, and timestamp.
  * Calls backend `/registerBatch` to store metadata on IPFS (via Pinata in backend).
  * Displays returned **CID** and provides link to view on `ipfs.io`.

* **Modern UI**

  * Tailwind design (rounded cards, gradients, progress bars).
  * Two tabs for easy switching between *Scan* and *Register*.
  * Mobile-friendly.

## 🛠 Tech Stack

* [React 18](https://react.dev/) (with [Vite](https://vitejs.dev/))
* [Tailwind CSS](https://tailwindcss.com/)
* FastAPI backend (runs separately — this repo is **frontend only**)

## 📦 Installation

Clone this repo and install dependencies:

```bash
git clone https://github.com/YOUR-ORG/herbchain-frontend.git
cd herbchain-frontend
npm install
```

Start development server:

```bash
npm run dev
```

The app will run at [http://localhost:5173](http://localhost:5173).

## ⚙️ Configuration

Create a `.env` file in the project root:

```
VITE_API_URL=http://127.0.0.1:8000
```

Change this URL if your backend is deployed elsewhere.

## 🔗 Backend API

The frontend expects these backend routes:

* `POST /validate` → validates herb metadata (returns dummy response in Dev 1 backend).
* `POST /registerBatch` → registers herb batch & returns `cid` (or `IpfsHash`).

👉 Make sure your backend allows **CORS** from `http://localhost:5173`.

## 📸 Screenshots

*(You can add UI screenshots here after you run the app and take captures)*

## 📌 Roadmap

* Integrate **real Chemical AI inference** (image upload → backend analysis).
* Add **report history** and **PDF export**.
* Polish UI with icons, charts, and animations.





