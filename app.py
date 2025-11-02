# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Page Setup
st.set_page_config(page_title="🛍️ Mall Customer Clustering", layout="wide")

st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #a6c0fe, #f68084);
    }
    .main {
        background-color: rgba(255,255,255,0.85);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        text-align: center;
        font-family: 'Trebuchet MS', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🛍️ Mall Customer Segmentation Dashboard")
st.markdown("### SkillCraft Internship - Task 02 | By **Misba Sikandar** 💫")

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("mall_customers.csv")
    return data

data = load_data()
st.dataframe(data.head())

# Feature selection
X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# Sidebar options
st.sidebar.header("⚙️ Clustering Controls")
num_clusters = st.sidebar.slider("Select Number of Clusters (K)", 2, 10, 5)

# KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, init="k-means++", random_state=42)
data["Cluster"] = kmeans.fit_predict(X)

# Elbow graph
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, init="k-means++", random_state=42)
    km.fit(X)
    inertia.append(km.inertia_)

st.subheader("📈 Elbow Method Graph")
fig1, ax1 = plt.subplots(figsize=(6,4))
ax1.plot(range(1, 11), inertia, marker="o", color="#4B8BBE")
ax1.set_xlabel("Number of Clusters (k)")
ax1.set_ylabel("Inertia")
ax1.set_title("Elbow Method for Optimal K")
st.pyplot(fig1)

# Cluster visualization
st.subheader("🎯 Customer Segmentation Visualization")
fig2, ax2 = plt.subplots(figsize=(7,5))
sns.scatterplot(
    x=data["Annual Income (k$)"],
    y=data["Spending Score (1-100)"],
    hue=data["Cluster"],
    palette="tab10",
    s=120,
    ax=ax2
)
ax2.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, c="black", marker="*", label="Centroids")
ax2.legend()
ax2.set_title("K-Means Customer Clusters")
st.pyplot(fig2)

# Cluster summary
st.subheader("📊 Cluster Summary")
st.dataframe(data.groupby("Cluster")[["Annual Income (k$)", "Spending Score (1-100)"]].mean())

st.markdown("---")
st.caption("✨ Developed by Misba Sikandar | SkillCraft Internship 2025 ✨")
