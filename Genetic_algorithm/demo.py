import streamlit as st
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

st.title("🧬 TPOT Genetic Algorithm Classifier")

st.write("This app uses TPOT (Genetic Programming) to automatically find the best ML model for the MAGIC Gamma Telescope dataset.")

# Load the dataset
@st.cache_data
def load_data():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.data'
    columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 'fAsym', 'fM3Long', 'fM3Trans',
               'fAlpha', 'fDist', 'Class']
    df = pd.read_csv(url, header=None, names=columns)
    df['Class'] = df['Class'].map({'g': 0, 'h': 1})  # gamma: 0, hadron: 1
    return df

data = load_data()

# Show dataset preview
if st.checkbox("Show raw data"):
    st.write(data.head())

# Shuffle and split data
data = data.sample(frac=1, random_state=42).reset_index(drop=True)
X = data.drop('Class', axis=1).values
y = data['Class'].values

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, train_size=0.75, random_state=42)

# TPOT Classifier
if st.button("Run TPOT"):
    with st.spinner("Running TPOT... this may take a few minutes ⏳"):
        tpot = TPOTClassifier(generations=5, population_size=20, verbosity=2, random_state=42, disable_update_check=True)
        tpot.fit(X_train, y_train)

        acc = tpot.score(X_test, y_test)
        st.success(f"✅ TPOT best model accuracy: **{acc:.4f}**")

        # Export pipeline
        with open("pipeline.py", "w") as f:
            f.write(tpot.export())

        st.download_button("📥 Download Generated Pipeline", data=open("pipeline.py", "r").read(), file_name="pipeline.py")
