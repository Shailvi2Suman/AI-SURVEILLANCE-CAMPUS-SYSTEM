# AI-SURVEILLANCE-CAMPUS-SYSTEM
# 🚨 Helmet & Safety Violation Alert System

A Streamlit-based dashboard that simulates alerts and visualizes performance metrics of YOLOv5 object detection models trained on safety-critical datasets: **VIRAT** and **OSF**. It also includes a sample **mosaic image** to depict multi-class detections in real-world scenes.

---

## 📁 Project Structure

```
📦 Helmet-Safety-Alert-System
├── app.py                  # Streamlit dashboard code
├── requirements.txt        # All required packages
├── .streamlit/
│   └── config.toml         # Optional Streamlit config
├── README.md               # You're here
├── assets/
│   └── mosaic_example.jpg  # Sample mosaic image for UI
```

---
## 🚀 Model Training Logs

Tracked with [Weights & Biases](https://wandb.ai/):

- 🟢 [VIRAT Dataset – YOLOv5 Run #1](https://wandb.ai/shailvisuman-iit-madras-/YOLOv5/runs/18ilcby5?nw=nwusershailvisuman)
- 🔵 [OSF Dataset – YOLOv5 Run #2](https://wandb.ai/shailvisuman-iit-madras-/YOLOv5/runs/jqmyl3tq?nw=nwusershailvisuman)
- 📊 [Project Dashboard – YOLOv5](https://wandb.ai/shailvisuman-iit-madras-/YOLOv5?nw=nwusershailvisuman)


## 🧠 Overview

This tool was developed for a safety-focused hackathon challenge to:

- Compare YOLOv5 model performance across two datasets (VIRAT & OSF)
- Display class-wise metrics: **Precision**, **Recall**, **mAP@0.5**
- Simulate safety alerts based on model outputs
- Visualize detection capability using a **mosaic image**

---

## 🚀 Features

- 📊 Class-wise metric comparison between datasets
- 🔔 Alert simulation for selected classes
- 🖼️ Mosaic image showcasing detections
- ☁️ Deployable using **Streamlit Cloud**

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/Helmet-Safety-Alert-System.git
cd Helmet-Safety-Alert-System
pip install -r requirements.txt
streamlit run app.py

