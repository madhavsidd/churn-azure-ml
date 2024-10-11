
# Telecom Customer Churn Prediction Model

## Problem Statement
A telecom company is facing a challenge with customers churning, which impacts its revenue and growth. The company collects data from its on-premises systems and stores it in Azure Blob Storage. The goal is to build a predictive model to identify customers likely to churn so that retention strategies can be implemented.

## Solution
This project implements a machine learning model to predict customer churn for the telecom company. It utilizes Azure cloud services for data storage, model training, and deployment, ensuring scalability and efficient workflow management.

## Architecture
1. **Data Source**: Telecom application database (on-premises) → Azure Blob Storage.
2. **Data Processing**: Data is preprocessed and prepared for model training.
3. **Model Training**: Performed using Azure Machine Learning Studio, leveraging automated machine learning and custom ML pipelines.
4. **Model Deployment**: The model is deployed to an Azure ML Endpoint for real-time predictions.

![flowchart](https://github.com/user-attachments/assets/dfeceace-f1dd-485d-b41e-05e2dff55dd0)


## Technology Stack
- **Data Storage**: Telecom customer data in Azure Blob Storage.
- **Model Training**: Azure Machine Learning Studio.
- **Model Deployment**: Azure ML Endpoint for API-based predictions.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YourUsername/telecom-customer-churn
    ```

2. **Navigate into the project directory**:
    ```bash
    cd telecom-customer-churn
    ```

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Azure credentials**:
    - Ensure your Azure CLI is set up and you're authenticated:
    ```bash
    az login
    ```

    - Set up the Azure Machine Learning workspace for training and deployment:
    ```bash
    az ml workspace configure --workspace-name your-workspace --resource-group your-resource-group
    ```

## Implementation Process
The project follows these key steps:

1. **Data Ingestion**: Data is loaded from Azure Blob Storage.
2. **Data Preprocessing**: Data is cleaned, transformed, and split into training and testing datasets.
3. **Feature Engineering**: Key features that affect customer churn are identified and processed.
4. **Model Training**: The predictive model is trained using Azure Machine Learning Studio's AutoML or custom ML pipelines.
5. **Model Evaluation**: The model is evaluated on test data to measure accuracy and performance.
6. **Deployment**: The model is deployed as an Azure ML Endpoint for real-time prediction.

All steps are documented in detail within the project files.

## Model Performance
- **Accuracy**: 0.81
- **Precision**: High precision in identifying likely churners, enabling proactive retention strategies.

## Deployment
The model is deployed as an Azure ML Endpoint, accessible via a REST API. Refer to the deployment documentation for detailed steps on how to deploy and interact with the model.

## Skills Learned

1. **Data Engineering**
   - Managing telecom customer data in Azure Blob Storage.
   - Data cleaning, preprocessing, and feature engineering.

2. **Cloud Computing**
   - Leveraging Azure services for end-to-end machine learning workflows.
   - Understanding and implementing cloud-based data storage and processing.

3. **Machine Learning**
   - Developing and training predictive models for customer churn.
   - Feature selection and hyperparameter tuning.

4. **MLOps (Machine Learning Operations)**
   - Deploying machine learning models as API endpoints using Azure ML.
   - Continuous model monitoring and version control.

5. **Domain Knowledge**
   - Understanding factors that influence customer churn in the telecom industry.
   - Translating business problems into machine learning solutions.

## Contributing
Contributions are welcome! If you have any ideas to improve this project, feel free to open an issue or submit a pull request.

