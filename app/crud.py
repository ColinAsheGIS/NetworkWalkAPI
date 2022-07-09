from sqlalchemy.orm import Session
from sqlalchemy import bindparam, text
import models, schemas

def get_vertex(db: Session, vertex_id: int):
    return (
        db.query(models.StormwaterVertex)
            .filter(models.StormwaterVertex.id == vertex_id).first()
        )

def get_vertices_by_outlet(db: Session, outlet_id: int, limit: int = 100):
    return (
        db.query(models.StormwaterVertex)
            .filter(models.StormwaterVertex.network_outlet == outlet_id).limit(limit)
            .all()
    )

def get_vertices_in_network(db: Session, outlet_id: int, limit: int = 100):
    return (
        db.query(models.StormwaterVertex)
            .filter()
    )

def get_downstream_proc(db: Session, vertex_id: int):
    trace_downstream_string = text(
        """
        SELECT edge FROM postgres.trace_downstream_schema(:vertex_id)
        """
    )
    params = {"vertex_id": [vertex_id]}
    trace_paramed = trace_downstream_string.bindparams(bindparam('vertex_id', expanding=True))
    execute = db.execute(trace_paramed, params)
    return execute.all()