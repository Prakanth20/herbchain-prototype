FastAPI Backend Example for IPFS Integration (Backend Dev 2)

python
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict
import requests

app = FastAPI()

# Set these from your Pinata account
PINATA_API_KEY = "YOUR_PINATA_API_KEY"
PINATA_SECRET_API_KEY = "YOUR_PINATA_SECRET_API_KEY"

class BatchRegisterRequest(BaseModel):
    herb_name: str
    location: Dict[str, float]
    collector_id: str
    collection_timestamp: str

def upload_to_ipfs(json_data):
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }
    payload = {
        "pinataContent": json_data
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        ipfs_hash = response.json()["IpfsHash"]
        return ipfs_hash
    else:
        return None

@app.post("/registerBatch")
async def register_batch(batch: BatchRegisterRequest):
    batch_dict = batch.dict()
    cid = upload_to_ipfs(batch_dict)
    return {
        "status": "registered" if cid else "error",
        "cid": cid,
        "batch_info": batch_dict
    }


Notes:

- Replace YOUR_PINATA_API_KEY and YOUR_PINATA_SECRET_API_KEY with actual Pinata credentials.
