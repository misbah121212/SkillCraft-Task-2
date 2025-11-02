# kmeans_model.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# Load data
data = pd.read_csv("mall_customers.csv")

# Display first few rows
print("Data Preview:")
print(data.head())

# Select features for clustering
X = data[["Annual Income (k$)", "Spending Score (1-100)"]]

# Use Elbow Method to find optimal clusters
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plot Elbow graph
plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), inertia, marker='o', color='teal')
plt.title("Elbow Method - Optimal K")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.show()

# Train final KMeans model
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Add cluster column to data
data["Cluster"] = y_kmeans

# Plot clusters
plt.figure(figsize=(7, 5))
sns.scatterplot(
    x=X["Annual Income (k$)"],
    y=X["Spending Score (1-100)"],
    hue=data["Cluster"],
    palette="tab10",
    s=100
)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, c="black", marker="*", label="Centroids")
plt.title("Customer Segments based on Income & Spending")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
