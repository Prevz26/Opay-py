import fastapi
#from pyngrok import ngrok
from dotenv import load_dotenv
import os
from pydantic import BaseModel
#from pyngrok.exception import NgrokLog, PyngrokNgrokError
load_dotenv()

ngrok_key = str(os.getenv("NGROK_AUTHTOKEN"))
#print(ngrok_key )

#ngrok.set_auth_token(ngrok_key)

class DataModel(BaseModel):
    message:str
    data:str

app = fastapi.FastAPI()

@app.post("/webhook/")
def webhook_func(data, DataModel):
    print(f"data recived: {data}")
    return {"message":"sucess"}



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
