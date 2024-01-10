# Pneumonia Detection Using CNN Algorithm

<p float="left">
  <img src="https://github.com/mhaidar10/pneumonia-cnn-basic/assets/72262185/4a7dec93-1b59-46ae-9886-ece720f919ac" width="200" />
  <img src="https://github.com/mhaidar10/pneumonia-cnn-basic/assets/72262185/dd4b64d7-3537-4121-b834-cedc35f08bca" width="800" height="430" /> 
</p>

## University Exam Project
Repository was created regarding the implementation of the CNN algorithm created using **Streamlit** <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo"></img>

## Description
A project was created that was able to **automatically detect pneumonia** based on x-ray images

# Dataset Source
Kaggle Dataset Chest X-Ray Images (Pneumonia) [(Link Download)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

# Directory Structure
```shell
machine_learning
├── model
│   └── pneunomia_model.h5
├── np2.ipynb
├── readme.md
└── streamlit
    ├── main.py
    └── requirements.txt
```
- **/model**: consists of a pneumonia model, which is used to store the trained machine learning model. The file contains the extension ".h5".
- **/streamlit**: Consists of the main.py file which is the main code in creating a website that can automatically detect pneumonia.
- **np2.ipynb**: file is the way to do the CNN algorithm creation process 

## Installation

1. Clone the repository to your local computer using the following command:

   ```shell
   git clone https://github.com/mhaidar10/Submission_Analisis_Data_Python.git](https://github.com/mhaidar10/pneumonia-cnn-basic.git
   ``` 
2. Install the Library with the following command:

    ```shell
    pip install streamlit tensorflow pillow requests
    
    ```
3. **[OPTIONAL]** Nodemon installation to perform Hot Reload
   ```shell
    npm install -g nodemon
    ```
   
## Usage

1. Perform Access and Compilation (Local):

    ```shell
    streamlit run streamlit/main.py
    ```
    **OR**  *nodemon installation require
    
   
    
    ```shell
    nodemon --exec streamlit run streamlit/main.py
    ```

    
2. Access in the Cloud (online):
   
   [Pnemonia Detection](https://ml-project-pneumonia-cnn-basic.streamlit.app/)
