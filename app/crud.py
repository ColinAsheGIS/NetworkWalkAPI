from sqlalchemy.orm import Session

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