# Smart Household Waste Segregation Assistant

An AI-based application that uses image classification to identify household waste as **Glass** or **Non-Glass** and provides basic waste segregation guidance.

## 1. Project Overview

The Smart Household Waste Segregation Assistant is an image-based waste classification prototype developed using Deep Learning.

Users can upload an image of a waste object through a Streamlit web application. The trained model analyses the image and predicts whether the object belongs to the Glass or Non-Glass category.

The application also displays model scores and provides basic segregation guidance.

## 2. Objectives

- Develop an image-based waste classification system.
- Distinguish Glass waste from Non-Glass waste.
- Apply transfer learning using MobileNetV2.
- Build an interactive interface using Streamlit.
- Provide basic guidance to assist household waste segregation.

## 3. Technologies Used

- Python
- TensorFlow and Keras
- MobileNetV2
- NumPy
- Pillow
- Streamlit
- Kaggle Notebooks

## 4. Dataset

The project uses a dataset based on six categories of household waste:

- Glass
- Paper
- Cardboard
- Plastic
- Metal
- Trash

The original dataset contains 2,527 images.

For binary classification:
- Glass is mapped to the Glass category.
- Paper, Cardboard, Plastic, Metal and Trash are mapped to Non-Glass.

The dataset was divided into training, validation and testing sets.

| Dataset | Images |
|---|---:|
| Training | 1,768 |
| Validation | 378 |
| Testing | 381 |
| **Total** | **2,527** |

## 5. Model Architecture

The project uses MobileNetV2 with transfer learning.

The architecture consists of:
1. MobileNetV2 as the pretrained feature extraction base.
2. Global Average Pooling layer.
3. Dropout layer.
4. Dense output layer with sigmoid activation.

Data augmentation techniques such as horizontal flipping, rotation, zoom and contrast adjustment were used during training.

The final candidate model was trained for five epochs.

## 6. Model Evaluation

The final candidate model was evaluated on the test dataset using a Non-Glass score threshold of 0.35.

| Metric | Result |
|---|---:|
| Test Accuracy | 89.24% |
| Glass Precision | 0.79 |
| Glass Recall | 0.63 |
| Glass F1-score | 0.70 |
| Non-Glass Precision | 0.91 |
| Non-Glass Recall | 0.96 |
| Non-Glass F1-score | 0.93 |

The classification threshold was selected using validation data. A lower threshold reduces false Glass predictions but can increase the number of actual Glass objects classified as Non-Glass.

## 7. Application Features

- Image upload through a web interface.
- Classification into Glass or Non-Glass.
- Display of Glass and Non-Glass model scores.
- Basic waste segregation guidance.
- Warning about possible incorrect predictions.

## 8. How to Run the Project

### Prerequisites

Install Python and ensure pip is available.

### Step 1: Clone the repository

```bash
git clone <your-repository-url>
cd SmartWasteAssistant
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the application

```bash
streamlit run app.py
```

The application will open in your web browser.

**Note:** The trained model file `smart_waste_final_candidate.keras` must be present in the project directory before running the application.

## 9. Limitations

- The model performs binary classification only.
- It does not identify the exact material type of Non-Glass objects.
- Predictions may be affected by lighting, object shape, transparency and reflective surfaces.
- The model may misclassify unfamiliar objects.
- The current prototype does not include a physical waste-sorting mechanism.

## 10. Future Scope

- Expand classification to multiple waste categories.
- Improve performance on transparent and reflective objects.
- Increase dataset diversity.
- Integrate a physical waste-sorting mechanism.
- Explore real-time waste detection.

## 11. Disclaimer

This project is an experimental academic prototype. Model scores are not guaranteed probabilities, and predictions should be verified before disposal. Users should follow local waste management and recycling guidelines.

---

**Project:** Smart Household Waste Segregation Assistant  
**Course:** Major Project 330