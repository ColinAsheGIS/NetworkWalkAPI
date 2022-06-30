from typing import List, Union

from pydantic import BaseModel

class VertexBase(BaseModel):
    id: int

    class Config:
        orm_mode = True

class Vertex(VertexBase):
    id: int
    stormwater_structure: int
    stormwater_outlet: int

    class Config:
        orm_mode = True

class StructureBase(BaseModel):
    objectid: int

class Structure(StructureBase):
    objectid: int
    stormwater_vertex: int

    class Config:
        orm_mode = True

class OutletBase(BaseModel):
    objectid: int

class Outlet(OutletBase):
    objectid: int
    stormwater_vertex: int
    
    class Config:
        orm_mode = True