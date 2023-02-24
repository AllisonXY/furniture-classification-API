from fastapi import FastAPI, File, UploadFile
import uvicorn
from .prediction import read_image,preprocess,predict

app=FastAPI()

@app.get("/")
def main_page():
    return "Welcome to Image Classification API!"

@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_image(await file.read())
    image=preprocess(image)
    prediction=predict(image)
    print(prediction)
    return prediction


if __name__ == "__main__":
    uvicorn.run(app, port=9090, host="0.0.0.0")  # open the site http://localhost:9090
