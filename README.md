# Furniture Classification API
This repository contains an API for furniture classification using a deep learning CNN model developed in TensorFlow. The API is built using FastAPI framework and Uvicorn server.

## Model
The classification_model.ipynb notebook contains the code for developing the CNN model. The model was trained on a provided dataset and saved as a folder called cnn_model under the API project folder.

## API Usage
To run this API, 
1) Open the terminal window under this project, and run the command: pip install fastapi uvicorn
2) The command to run the app is: uvicorn src.main:app 
3) Now you can access the welcome page at http://127.0.0.1:8000/
4) To try the classification feature, visit http://127.0.0.1:8000/docs --> select “try it out” --> upload an image file --> select “execute” --> "response body" will show the predicted label

![FastAPI - Swagger UI - Google Chrome 2_23_2023 7_08_23 PM](https://user-images.githubusercontent.com/71278811/221062352-f486a0af-afe8-4cb3-8407-d8b5e70b22ce.png)
![FastAPI - Swagger UI - Google Chrome 2_23_2023 7_08_35 PM](https://user-images.githubusercontent.com/71278811/221062376-e2d8d97b-9fc1-4283-91d8-ef55fc02e840.png)



## Docker Image
A pre-built Docker image is available for this API in a shared Google folder (https://drive.google.com/file/d/1j0k22Gf8J9oyiz8uW1EuaxBvDg0OqTpP/view?usp=sharing). The Docker image was built using Docker Desktop and PowerShell.
