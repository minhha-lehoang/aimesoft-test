# News Category Classification

This project aims to classify news articles into predefined categories using machine learning techniques. The model is trained using TF-IDF vectorization and a Linear Support Vector Machine (SVM) classifier.


## Files and Directories

- **model/**: Contains the serialized model, vectorizer, and label encoder.
  - `classifier.pkl`: The trained classifier.
  - `label_encoder.pkl`: The label encoder for the categories.
  - `vectorizer.pkl`: The TF-IDF vectorizer.

- **modules/**: Contains the Python modules for various tasks.
  - `__init__.py`: Initialization file for the module.
  - `api.py`: Contains functions to load the model and make predictions.
  - `create_dataset.py`: Script to create the dataset from raw data.
  - `inference.py`: Script to perform inference using the trained model.
  - `preprocessing.py`: Contains preprocessing functions.

- **News Category Classification - TFIDF + LinearSGD.ipynb**: Jupyter notebook for training and evaluating the model.

- **news_extracted/**: Contains the extracted datasets.
  - `train.csv`: Training dataset.
  - `test.csv`: Test dataset.
  - `val.csv`Validation dataset.


## Training the Model

Open the Jupyter notebook `News Category Classification - TFIDF + LinearSGD.ipynb` and follow the steps to train the model. The notebook includes data preprocessing, model training, and evaluation.


## Inference

### In a Python Script
To perform inference using the trained model, use the functions defined in `modules/api.py`. Example usage:

```python
from modules.api import load_model, load_model_route

# Load the model
model, vectorizer, encoder = load_model()

# Make predictions
predictions = model.predict(vectorizer.transform(["Sample news article text"]))
predicted_category = encoder.inverse_transform(predictions)
print(predicted_category)
```

### Using REST API
To run the API, execute the following command:

```bash
python modules/api.py path/to/models/folder
```

The API will be available at `http://localhost:5000`. You can make a POST request to the `/predict` endpoint with the news article text to get the predicted category.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "Sample news article text"}' http://localhost:5000/predict
```

Or you can use the `inference.py` script to make predictions from the command line:

```bash
python modules/inference.py "Sample news article text"
```