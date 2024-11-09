import fastapi
#from pyngrok import ngrok
from pydantic import BaseModel

#ngrok.set_auth_token(ngrok_key)

class DataModel(BaseModel):
    message:str
    data:str

app = fastapi.FastAPI()

@app.post("/callBack/")
def webhook_func(data, DataModel):
    #print(f"data recived: {data}")
 return {"message":"sucess"}

@app.post("/cancelUrl")
def cancel(data, DataModel):
    return {"message":"sucess", "data": f"{data}"}

@app.post("/returnUrl")
def returnUrl(data, DataModel):
    return {"message":"sucess", "data": f"{data}"}




# Set up Ngrok tunnel
#try:
#    public_url = ngrok.connect(8000)
#except PyngrokNgrokError as e:
#    print({e})
#else:
##Run the FastAPI app using uvicorn
#    print("Ngrok Tunnel URL:", public_url)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5000)
