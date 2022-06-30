from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from database import Base

class StormwaterVertex(Base):
    __tablename__ = "stormwater_pipe_vertices_pgr"
    __table_args__ = {"schema": "postgres"}

    id = Column(BigInteger, primary_key=True)
    the_geom = Column(Geometry)
    network_outlet = Column(BigInteger, ForeignKey("postgres.stormwater_outlet.objectid"))

    stormwater_structure = relationship("StormwaterStructure", back_populates="stormwater_vertex", uselist=False)
    stormwater_outlet = relationship("StormwaterOutlet", back_populates="stormwater_vertex")

class StormwaterStructure(Base):
    __tablename__ = "stormwater_structure"
    __table_args__ = {"schema": "postgres"}

    objectid = Column(Integer, primary_key=True)
    network_vertex = Column(BigInteger, ForeignKey("postgres.stormwater_pipe_vertices_pgr.id"))
    network_outlet = Column(BigInteger)

    stormwater_vertex = relationship("StormwaterVertex", back_populates="stormwater_structure")

class StormwaterOutlet(Base):
    __tablename__ = "stormwater_outlet"
    __table_args__ = {"schema": "postgres"}

    objectid = Column(Integer, primary_key=True)
    
    stormwater_vertex = relationship("StormwaterVertex", back_populates="stormwater_outlet", uselist=False)