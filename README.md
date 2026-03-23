## 🚚📄 Vendor Invoice Intelligence Portal

An end-to-end Machine Learning application that predicts freight costs and flags high-risk vendor invoices to improve financial decision-making and reduce operational inefficiencies.

### 🚀 Key Highlights
 - Built a dual ML system:
   - 📈 Freight Cost Prediction (Regression)
   - 🧾 Invoice Risk Detection (Classification)
 - Developed using real-world relational data (SQL → ML pipeline)
 - Deployed via interactive Streamlit web app
 - Designed with production-style modular architecture

### 🧠 Business Impact
 - 💰 Improved freight cost forecasting accuracy
 - 🧾 Automated invoice risk detection
 - ⚡ Reduced manual auditing effort
 - 📉 Minimized potential financial leakage

### ⚙️ Tech Stack
 - Python, Pandas, NumPy
 - Scikit-learn (Regression & Classification Models)
 - SQLite (Data source with SQL joins)
 - Streamlit (Deployment & UI)
 - Joblib (Model persistence)

### 🔄 ML Pipeline
1. Data Engineering
 - Extracted and transformed data from SQLite database
 - Designed aggregated SQL queries (JOIN + feature aggregation)
 - Converted large dataset (400MB+) → optimized CSV for deployment
2. Feature Engineering
 - Created meaningful features such as:
   - Unit price
   - Freight ratio
   - Dollar difference ratio
 - Ensured training–inference consistency
3. Model Development
 - Regression: Linear Regression, Random Forest
 - Classification: Random Forest with GridSearchCV
 - Handled:
   - ❌ Data leakage
   - ⚖️ Class imbalance (class_weight='balanced')
   - 🎯 Model evaluation (MAE, RMSE, F1-score)
4. Real-World Simulation
 - Introduced probabilistic labeling to simulate noisy business scenarios
 - Avoided overfitting from rule-based labels
5. Deployment
 - Built interactive UI using Streamlit
 - Implemented separate inference pipeline
 - Ensured feature alignment between training and prediction

### 📊 Model Performance
 - Freight Prediction:
   - Achieved strong performance using Random Forest regression
 - Invoice Risk Detection:
   - Balanced model improving detection of minority (risky) cases
   - Optimized for recall over accuracy (business-critical)
   - 
 ### 🧩 Project Structure
 ML_PROJECT/
 │
 ├── data/
 ├── models/
 ├── notebooks/
 ├── src/
 │   ├── freight/
 │   └── invoice/
 ├── inference/
 ├── app.py
 └── README.md

### 💡 Key Learnings
 - Importance of feature consistency between training & inference
 - Handling data leakage and class imbalance
 - Designing scalable ML pipelines
 - Translating business problems into ML solutions
