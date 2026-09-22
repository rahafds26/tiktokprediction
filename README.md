# TikTok Day 30 Views Prediction

## Overview

A machine learning project for predicting the cumulative number of views a TikTok video will receive by Day 30 using early engagement metrics, video metadata, and creator statistics.

Developed as part of a Data Science Bootcamp.

## Objective

Predict `target_day30_views` based on information available during the early stages of a video's lifecycle.

## Dataset

The project uses:

- Video metadata
- Daily engagement data from Day 0 to Day 5
- Creator statistics
- Training and test datasets

## Data Preparation

- Data cleaning and inspection
- Exploratory Data Analysis (EDA)
- Feature engineering
- Combining video, engagement, and creator data
- Handling numerical and categorical features

## Model Results

The models were evaluated using RMSE.

| Model | RMSE |
|---|---:|
| Baseline | 269,760.8881 |
| Extra Trees - Original | 75,064.4732 |
| Extra Trees - 0.8 + Leaf 2 | 70,549.7324 |
| Extra Trees - 1500 Trees + 0.7 + Leaf 2 | **67,326.2713** |

## Final Model

**Extra Trees Regressor**

| Parameter | Value |
|---|---:|
| Number of Trees | 1500 |
| Max Features | 0.7 |
| Min Samples Leaf | 2 |
| Max Depth | None |
| Random State | 42 |

## Kaggle

[Kaggle Competition](https://www.kaggle.com/competitions/predictive-modelling-ds)

Public leaderboard RMSE:

**75,311.02064**

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Kaggle
- Streamlit

## Project Files

| File | Description |
|---|---|
| `notebook.ipynb` | Complete project workflow |
| `submission.csv` | Kaggle submission predictions |
| `model_results.csv` | Model evaluation results |
| `final_model_pipeline.pkl` | Trained final model |
| `app.py` | Streamlit application |

## Author

**Rahaf Mohammed Alzahrani**
