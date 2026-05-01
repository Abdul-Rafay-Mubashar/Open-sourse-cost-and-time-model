# 📊 AI-Based Project Effort & Cost Estimation System

### Machine Learning + Graph-Based Project Planning Tool

---

## 📌 Overview

This project is a **machine learning-based project estimation system** that predicts task duration, estimates cost, and analyzes task dependencies using **graph algorithms**.

It combines **Machine Learning + Graph Theory + Automation logic** to simulate real-world **project planning and effort estimation systems**.

---

## 🚀 Key Features

### 🤖 Machine Learning

* Predicts task duration using **Linear Regression**
* Estimates effort based on:

  * Task complexity
  * Developer experience
  * Task type

---

### 🔗 Dependency Analysis

* Builds task dependency graph (DAG)
* Uses DFS for execution path analysis
* Identifies **critical path (longest execution time)**

---

### ⏱️ Project Estimation

* Calculates total project timeline
* Finds longest execution route
* Simulates real project scheduling flow

---

### 💰 Cost Calculation

* Auto cost estimation per developer
* Task-wise cost breakdown
* Total project cost generation

---

## 🧠 System Workflow

### 1️⃣ Data Preparation

* Loads dataset (`synthetic_effort_dataset.csv`)
* Encodes categorical features using Label Encoding
* Trains **Linear Regression model**

---

### 2️⃣ Graph Construction

* Builds dependency graph of tasks
* Maps parent-child task relationships
* Represents project as **Directed Acyclic Graph (DAG)**

---

### 3️⃣ Path Analysis

* Uses **DFS (Depth First Search)**
* Finds all execution paths
* Identifies **critical path (maximum duration)**

---

### 4️⃣ Prediction System

* Predicts task completion time using ML model
* Assigns simulated developer attributes
* Calculates effort per task

---

### 5️⃣ Cost & Reporting

* Computes total project cost
* Developer-wise breakdown
* Activity-wise time and cost report

---

## ⚙️ Tech Stack

* Python 3
* Pandas
* NumPy
* Scikit-learn (Linear Regression)
* Graph Theory (DFS, DAG)
* Randomized Simulation Logic

---

## 🧠 Core Concepts Used

* 📈 Machine Learning (Regression Model)
* 🔗 Directed Acyclic Graph (DAG)
* 🔍 Depth First Search (DFS)
* 📊 Feature Engineering
* 💰 Cost Estimation Logic
* 🧩 Dependency Management

---

## 📊 Example Output

```
Total cost for project is 450$  
Total time for project is 18hrs  

------ Activities Prices ------  
Activity A is done in 2hrs in 40$ by Ali  
Activity B is done in 3hrs in 60$ by Iqbal  

------ Developer Prices ------  
You need to pay Ali 120$  
You need to pay Iqbal 180$  
```

---

## 💡 Project Highlights

* Simulates real-world project management system
* Combines ML prediction + graph scheduling
* Demonstrates algorithmic + AI integration
* Useful for effort estimation and planning tools

---

## 🚀 Future Improvements

* Replace Linear Regression with **XGBoost / Random Forest**
* Add real scheduling optimization algorithm
* Build UI dashboard (React / Streamlit)
* Store project history in database
* Add real-time tracking system

---

## 📌 Summary

This system demonstrates a **hybrid AI approach** combining:

* 🤖 Machine Learning (effort prediction)
* 🔗 Graph Theory (dependency analysis)
* ⚙️ Automation logic (project simulation)

It can be extended into a **real-world AI-powered project management system**.

---
