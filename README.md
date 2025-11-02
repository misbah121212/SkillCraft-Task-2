📘 Project Title

Mall Customer Segmentation using K-Means Clustering
(SkillCraft Technology Internship – Task 02)

🧩 Project Overview

This project focuses on applying K-Means Clustering, an unsupervised machine learning algorithm, to segment customers of a retail store based on their purchasing behavior.

By analyzing data such as customers’ Annual Income and Spending Score, we can identify distinct customer groups or segments. These segments help retail stores in creating personalized marketing strategies, improving customer experience, and boosting sales.

This task is part of SkillCraft Technology’s Machine Learning Internship program.

🧠 Objective

To create a K-Means clustering algorithm that groups mall customers into meaningful clusters based on their purchase history.

Each cluster represents a distinct type of customer — for example:

High Income, High Spending

Low Income, Low Spending

High Income, Low Spending

Average Income, Average Spending, etc.

📂 Dataset Details

Dataset Name: Mall Customer Dataset
Source: Kaggle – Customer Segmentation Dataset

File Name: Mall_Customers.csv

📊 Dataset Columns:
Column Name	Description
CustomerID	Unique ID assigned to each customer
Gender	Gender of the customer
Age	Age of the customer
Annual Income (k$)	Annual income of the customer in thousand dollars
Spending Score (1-100)	Score assigned by the mall based on customer behavior and spending nature
⚙️ Features Used for Clustering:

Annual Income (k$)

Spending Score (1–100)

These two features are chosen because they best represent the customers’ purchasing capacity and behavior.

💻 Tools and Technologies Used
Tool / Library	Purpose
Python 3.10+	Programming Language
VS Code	Development Environment
pandas	Data manipulation and analysis
numpy	Numerical computation
matplotlib / seaborn	Data visualization
scikit-learn	Machine Learning model (K-Means)
streamlit	Web App Framework
🧱 Project Structure
MallCustomerClustering/
│
├── app.py                   → Streamlit web app
├── kmeans_model.py          → Core ML model script
├── Mall_Customers.csv       → Dataset file
└── clustered_customers.csv  → Output after clustering

⚙️ Installation and Setup

Create a Project Folder

MallCustomerClustering


Install Required Libraries
Open terminal and run:

pip install pandas numpy matplotlib seaborn scikit-learn streamlit


Add Files

Place Mall_Customers.csv inside your project folder.

Add both app.py and kmeans_model.py files.

Run Model Script (optional)

python kmeans_model.py


This will:

Load and preprocess data

Plot Elbow Method

Train K-Means

Save results to clustered_customers.csv

Run the Streamlit App

streamlit run app.py


Open the Local Webpage
After running, Streamlit will give a link like:

http://localhost:8501/


Open this in your browser.

📊 Working Process
Step 1 – Load the Data

The dataset is loaded using pandas. Initial exploration helps to understand data patterns, missing values, and data distribution.

Step 2 – Feature Selection

The two most significant features are:

Annual Income (k$)

Spending Score (1-100)

These are extracted for clustering.

Step 3 – Feature Scaling

Since K-Means is a distance-based algorithm, all features are standardized using StandardScaler().

Step 4 – Finding Optimal Clusters (Elbow Method)

We run K-Means with different k values (1–10) and plot Inertia vs k.
The point where the graph starts bending (“elbow”) is the optimal number of clusters.

Step 5 – Training the K-Means Model

After determining the optimal number of clusters (usually k=5), the final K-Means model is trained and labels are assigned to each customer.

Step 6 – Visualizing the Clusters

A scatter plot is generated using seaborn to visualize the clusters:

X-axis → Annual Income

Y-axis → Spending Score

Colors → Cluster groups

Step 7 – Streamlit Web App

The app displays:

The raw dataset

Elbow Method graph

Cluster visualization

Downloadable clustered results (clustered_customers.csv)

🖥️ Output and Results

Elbow Method Graph:
Helps identify the ideal number of clusters (usually k = 5).

Cluster Visualization Plot:
Displays customer groups in different colors.

Clustered Data:
File clustered_customers.csv contains the cluster label for each customer.

Example Cluster Insights:

Cluster	Type of Customer	Behavior
0	High Income – High Spending	Premium, Loyal Shoppers
1	Low Income – Low Spending	Budget Shoppers
2	Average Income – Moderate Spending	Occasional Buyers
3	High Income – Low Spending	Cautious Spenders
4	Low Income – High Spending	Impulsive Buyers
🌐 Streamlit App Features

Display raw dataset.

Interactive Elbow graph to find best k.

User can select number of clusters via slider.

Cluster visualization updates automatically.

Download option for clustered results.

🧾 Conclusion

This project successfully demonstrates unsupervised learning using K-Means Clustering to group customers based on purchasing patterns.

Through visualization and cluster analysis:

Businesses can target each customer group effectively.

Marketing strategies can be customized to improve engagement and sales.

Thus, this model helps in data-driven decision-making for retail businesses.

👩‍💻 Developer Information

Name: Misba Sikandar
Internship: SkillCraft Technology – Machine Learning Internship
Task: Task 02 – Mall Customer Segmentation using K-Means Clustering
Tools Used: Python, Scikit-learn, Streamlit, Seaborn, Matplotlib
