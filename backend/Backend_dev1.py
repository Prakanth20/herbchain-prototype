from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Request schema for registering a batch (customize as per your requirements)
class BatchRegisterRequest(BaseModel):
    herb_name: str
    location: Dict[str, float]  # latitude and longitude
    collector_id: str
    collection_timestamp: str

# Dummy endpoint to validate data
@app.post("/validate")
async def validate_batch(request: Request):
    # In a real system, validate incoming data
    data = await request.json()
    # Respond with dummy validation
    return {
        "status": "success",
        "message": "Batch data is valid.",
        "input_data": data
    }

# Dummy endpoint to register a batch
@app.post("/registerBatch")
async def register_batch(batch: BatchRegisterRequest):
    # In a real system, this would store information with blockchain/IPFS integration
    return {
        "status": "registered",
        "cid": "bafybeigdyrzt3y4dp7vj4m5db7gxtt4npmwlzvck6e",  # dummy CID
        "batch_info": batch.dict()
    }

