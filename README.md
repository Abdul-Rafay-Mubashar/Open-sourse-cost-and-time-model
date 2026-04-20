📊 AI-Based Project Effort & Cost Estimation System
📌 Overview

This project is a machine learning-based project estimation system that predicts task duration, calculates project cost, and analyzes task dependencies using graph algorithms.

It combines Machine Learning + Graph Theory + Automation logic to simulate real-world project planning and effort estimation.

🚀 Key Features
🤖 Machine Learning-based time prediction using Linear Regression
📊 Task effort estimation based on:
Complexity level
Developer experience
Task type
🔗 Dependency graph construction for project workflow
🔁 DFS-based path analysis for critical path detection
⏱️ Project timeline estimation (longest execution path)
💰 Automatic cost calculation per developer and project
👨‍💻 Simulated task assignment system

🧠 How It Works
1️⃣ Data Training
Reads dataset (synthetic_effort_dataset.csv)
Encodes categorical task data using LabelEncoder
Trains a Linear Regression model

2️⃣ Activity Graph Creation
Builds a dependency graph of project tasks
Identifies root and child nodes
Maps execution flow using adjacency list

3️⃣ Path Analysis
Uses DFS to find all possible execution paths
Calculates total time for each path
Identifies critical path (longest duration)

4️⃣ Prediction System
Predicts task completion time using ML model
Assigns random developer attributes (experience, rate)
Calculates cost per activity

5️⃣ Cost & Report Generation
Total project cost calculation
Developer-wise payment breakdown
Activity-wise time and cost report

⚙️ Tech Stack
Python 3
Pandas
NumPy
Scikit-learn (Linear Regression)
Graph Theory (DFS, dependency graphs)
Randomized simulation logic

🧠 Core Concepts Used
📈 Machine Learning (Regression Model)
🔗 Directed Acyclic Graph (DAG)
🔍 Depth First Search (DFS)
📊 Feature Engineering
💰 Cost Estimation Logic
🧩 Dependency Management

📊 Example Output
Total cost for project is 450$
Total time for project is 18hrs

------Activities Prices-------
Activity A is done in 2hrs in 40$ by Ali
Activity B is done in 3hrs in 60$ by Iqbal

------Developer Prices------
You need to pay Ali 120$
You need to pay Iqbal 180$

💡 Project Highlights
Simulates real-world project planning system
Combines ML prediction with graph-based scheduling
Demonstrates algorithmic thinking + AI integration
Useful for project management and effort estimation systems

🚀 Future Improvements
Replace random assignment with real scheduling algorithm
Improve ML model accuracy (XGBoost / Random Forest)
Add UI dashboard (React / Streamlit)
Store results in database
Add real-time project tracking system

📌 Summary

This system demonstrates a hybrid approach of:

👉 Machine Learning (effort prediction)
👉 Graph Theory (task dependency analysis)
👉 Automation logic (project simulation)

It can be extended into a real project management AI tool.
