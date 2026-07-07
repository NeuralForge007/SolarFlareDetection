Solar Flare Forecasting using Multi-modal Soft & Hard X-ray Data (Aditya-L1)
Overview :

This project aims to forecast and nowcast solar flares using the combined observations from the SoLEXS (Soft X-ray) and HEL1OS (Hard X-ray) instruments onboard ISRO's Aditya-L1 mission.
Unlike conventional approaches that rely on a single X-ray source, this work integrates both soft and hard X-ray observations to capture the complete physical evolution of solar flares. Physics-informed feature engineering is incorporated to improve the model's ability to distinguish genuine flare precursors from background solar activity.

Objectives :
Detect and forecast solar flares using multi-modal X-ray observations.
Combine soft and hard X-ray temporal behavior.
Engineer physics-informed features based on solar flare theory.
Reduce false alarms caused by phenomena such as delayed hard X-ray emission and electron trapping.
Build an explainable machine learning pipeline for space weather forecasting.

Dataset :
SoLEXS (Solar Low Energy X-ray Spectrometer)
Soft X-ray light curves
1-second temporal resolution
Photon count rate (cts/sec)
HEL1OS (High Energy L1 Orbiting X-ray Spectrometer)
Hard X-ray light curves
Event-level photon observations
Photon energy (keV)
Count rate (cts/sec)
GOES X-ray Flare Catalogue

Used for ground-truth flare labels.

Flare Classes:


C
M
X

Feature Engineering:

Raw Features:
UTC Timestamp
Soft X-ray Count Rate
Hard X-ray Count Rate
Mean Hard Photon Energy

Physics-Informed Features:
Background Photon Count
Adaptive Threshold
Excess Soft Photon Count
Threshold Excess
Pre-heating Index

Cross-Energy Correlation Features :
Rolling Soft–Hard Correlation
Hardness Ratio
Neupert Deviation Index (NDI)
Neupert Consistency Indicator (NCI)

Machine Learning Pipeline:

SoLEXS Light Curve
        │
        ▼
Feature Engineering
        │
        ▼
HEL1OS Event Processing
        │
        ▼
Physics-informed Feature Extraction
        │
        ▼
Feature Fusion
        │
        ▼
Machine Learning Model
        │
        ▼
Solar Flare Prediction

Project Structure :

SolarFlareDetection/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── SoLEXS/
│   │   ├── HEL1OS/
│   │   └── GOES/
│   │
│   ├── processed/
│   │   ├── Updated_data.csv
│   │   ├── heliosMeanEnergy.csv
│   │   └── labelled_dataset.csv
│   │
│   └── Dataset_Png/
│       ├── Screenshot1.png
│       ├── Screenshot2.png
│       └── ...
│
├── FeatureEngineering/
│   ├── dataframeCreation.py
│   ├── extraction(event).py
│   ├── extraction(pi).py
│   ├── correlation.py
│   ├── delete.py
│   └── featureEngineering.py
│
├── flareevent/
│   ├── f1csv.py
│   ├── lccsv.py
│   ├── loaddata.py
│   ├── multiflare.py
│   ├── threshold.py
│   └── __pycache__/
│
├── plots/
│   ├── backgroundanalysis.py
│   ├── bgsub.py
│   ├── ddx.py
│   ├── loaddata.py
│   ├── loghist.py
│   ├── rollingper.py
│   ├── threshold.py
│   └── zoomedflare.py
│
├── models/
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── saved_models/
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── FeatureEngineering.ipynb
│   └── ModelTraining.ipynb
│
├── results/
│   ├── figures/
│   ├── predictions/
│   └── metrics/
│
└── utils/
    ├── preprocessing.py
    ├── helpers.py
    └── visualization.py
