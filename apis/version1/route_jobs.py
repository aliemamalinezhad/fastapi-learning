import current as current
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from apis.version1.route_users import router
from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import ShowJob, JobCreate

router = APIRouter()


@router.post("/create-job/", response_model="ShowJob")
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job
