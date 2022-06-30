from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/vertex/{vertex_id}", response_model=schemas.VertexBase)
async def get_vertex_by_id(vertex_id: int, db: Session = Depends(get_db)):
    id_exists = crud.get_vertex(db, vertex_id=vertex_id)
    if id_exists is None:
        raise HTTPException(status_code=404, detail=f"vertexid {vertex_id} doesn't exist")
    return id_exists

@app.get("/outlet/{outlet_id}/vertex", response_model=List[schemas.VertexBase])
async def get_vertex_by_outlet(outlet_id: int, db: Session = Depends(get_db)):
    outlet_exists = crud.get_vertices_by_outlet(db, outlet_id=outlet_id)
    if outlet_exists is None:
        raise HTTPException(status_code=404, detail=f"outletid {outlet_id} doesn't exist")
    return outlet_exists

