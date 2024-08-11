from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from firebase_admin import auth
from db import db
from schemas import Camp

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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