import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase service account key file
SERVICE_ACCOUNT_KEY_PATH = 'config.json'

# Initialize the Firebase app
cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
