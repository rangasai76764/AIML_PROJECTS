import streamlit as st
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

st.set_page_config(page_title="TPOT Genetic AutoML", page_icon="🧬")

st.title("🧬 TPOT Genetic Algorithm Classifier")
st.write(
    "This app uses **TPOT** (genetic programming) to automatically find the best ML pipeline "
    "for the **MAGIC Gamma Telescope** dataset."
)

@st.cache_data
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/magic/magic04.data"
    columns = [
        "fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym",
        "fM3Long", "fM3Trans", "fAlpha", "fDist", "Class"
    ]
    df = pd.read_csv(url, header=None, names=columns)
    df["Class"] = df["Class"].map({"g": 0, "h": 1})  # gamma:0, hadron:1
    return df

data = load_data()

with st.expander("👀 Preview Data"):
    st.write(data.head())
    st.write(data.describe())

data = data.sample(frac=1, random_state=42).reset_index(drop=True)
X = data.drop("Class", axis=1).values
y = data["Class"].values

# Sidebar
st.sidebar.header("TPOT Settings")
generations = st.sidebar.slider("Generations", 1, 20, 5)
population_size = st.sidebar.slider("Population Size", 10, 200, 50, step=10)
test_size = st.sidebar.slider("Test Size", 0.1, 0.4, 0.25)
config_dict = st.sidebar.selectbox("Preset", ["TPOT light", "Default"], index=0)
config_dict = config_dict if config_dict == "TPOT light" else None
random_state = st.sidebar.number_input("Random State", 0, 9999, 42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, train_size=1 - test_size, random_state=random_state
)

if st.button("🚀 Run TPOT"):
    with st.spinner("Running TPOT... please wait ⏳"):
        tpot = TPOTClassifier(
            generations=generations,
            population_size=population_size,
            verbosity=2,
            random_state=random_state,
            disable_update_check=True,
            config_dict=config_dict,
            n_jobs=-1,
        )
        tpot.fit(X_train, y_train)
        y_pred = tpot.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

    st.success(f"✅ TPOT model accuracy: **{acc:.4f}**")
    pipeline_code = tpot.export()
    st.code(pipeline_code, language="python")
    st.download_button("📥 Download pipeline.py", pipeline_code, file_name="pipeline.py")
else:
    st.info("Set your parameters and click **Run TPOT**.")
