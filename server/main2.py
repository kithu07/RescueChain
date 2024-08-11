from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth, credentials, initialize_app
from db import db
from schemas import Camp

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

@app.get("/app/login")
async def secure_endpoint(token: str = Depends(oauth2_scheme)):
    user_data = verify_token(token)
    return {"message": f"Hello, {user_data['email']}, welcome to the secure endpoint!"}

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI server!"}

@app.get("/get/camps")
async def read_camps():
    # Reference to the 'camps' collection
    camps_ref = db.collection('camps')
    
    # Get all documents in the 'camps' collection
    docs = camps_ref.stream()
    
    # Create a list to store the camp data
    camps = []
    
    for doc in docs:
        camp_data = doc.to_dict()
        camp_data['id'] = doc.id  # Add document ID to the data
        camps.append(camp_data)
    
    return {"camps": camps}

@app.post("/add/camps")
async def add_camp(camp: Camp):
    # Reference to the 'camps' collection
    camps_ref = db.collection('camps')
    
    # Add a new document to the 'camps' collection with the provided data
    try:
        camps_ref.add(camp.dict())
        return {"message": "Camp added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding camp: {str(e)}")