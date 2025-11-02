🧠 TASK 2 – Mall Customer Segmentation using K-Means Clustering
📘 Project Overview

This project demonstrates the use of K-Means Clustering, an unsupervised machine learning algorithm, to segment mall customers based on their purchasing behavior.
By analyzing parameters such as Annual Income and Spending Score, the model identifies distinct customer groups to help retail businesses design targeted marketing strategies, improve engagement, and optimize sales performance.

This project is developed as part of the SkillCraft Technology Machine Learning Internship (Task 2).

🎯 Objective

The main goal of this project is to group customers of a retail store into meaningful clusters based on their income and spending patterns.
Each cluster represents a unique type of customer — such as high-income high-spenders, low-income low-spenders, and moderate buyers — providing insights into customer behavior for better business decisions.

📂 Dataset Details

Dataset Name: Mall Customer Dataset
Source: Kaggle – Customer Segmentation Dataset

File Name: Mall_Customers.csv

📊 Columns:

CustomerID – Unique ID assigned to each customer

Gender – Male or Female

Age – Age of the customer

Annual Income (k$) – Customer’s annual income in thousand dollars

Spending Score (1–100) – Score assigned by the mall based on customer’s behavior and spending nature

⚙️ Features Used for Clustering:

Annual Income (k$)

Spending Score (1–100)

🧰 Technologies and Tools Used
Tool / Library	Purpose
🐍 Python 3	Programming Language
💻 VS Code	Code Editor
📦 pandas, numpy	Data Handling & Preprocessing
📈 matplotlib, seaborn	Data Visualization
🧮 scikit-learn	K-Means Model Implementation
🌐 streamlit	Web Application Interface
🧱 Project Structure
MallCustomerClustering/
│
├── app.py                   → Streamlit web application
├── kmeans_model.py          → Core ML script for K-Means
├── Mall_Customers.csv       → Dataset file
└── clustered_customers.csv  → Output file after clustering

⚙️ Installation and Setup Steps

Create a Folder

MallCustomerClustering


Install Required Libraries

pip install pandas numpy matplotlib seaborn scikit-learn streamlit


Add Files

Place the Mall_Customers.csv dataset in the folder.

Add kmeans_model.py and app.py.

Run the Model Script

python kmeans_model.py


Launch the Streamlit App

streamlit run app.py


Open Browser
Visit the local URL (usually http://localhost:8501/) to interact with the app.

🧩 Working Process

Data Loading – The dataset is loaded using pandas for analysis.

Feature Selection – Annual Income and Spending Score are chosen for clustering.

Scaling – StandardScaler is applied to normalize feature values.

Elbow Method – Used to find the optimal number of clusters (k).

Model Training – K-Means is trained on the selected features.

Visualization – Clusters are visualized using scatter plots.

Streamlit Integration – App displays dataset, elbow graph, and clusters interactively.

📊 Results and Insights

The project identifies 5 key customer segments based on their spending habits and income levels.
Each cluster represents a distinct type of shopper:

Cluster	Type of Customer	Behavior
0	High Income – High Spending	Loyal Premium Shoppers
1	Low Income – Low Spending	Budget Shoppers
2	Average Income – Moderate Spending	Regular Buyers
3	High Income – Low Spending	Cautious Spenders
4	Low Income – High Spending	Impulsive Shoppers
🌐 Streamlit App Features

📄 Display raw dataset

📊 Elbow graph for finding best k

🎚️ Interactive slider to select number of clusters

🎨 Live cluster visualization

💾 Download clustered results

🧾 Conclusion

This project effectively demonstrates how K-Means Clustering can be used to analyze and group customers based on purchasing patterns.
The insights derived from this model can help businesses:

Identify premium and budget customers

Personalize marketing strategies

Improve customer satisfaction and retention

Through the use of machine learning and data visualization, this project showcases the power of unsupervised learning in business analytics.

👩‍💻 Developer Information

Name: Misba Sikandar
Internship: SkillCraft Technology – Machine Learning Internship
Task: Task 2 – Mall Customer Segmentation using K-Means Clustering
Tools Used: Python, Scikit-learn, Streamlit, Matplotlib, Seaborn
