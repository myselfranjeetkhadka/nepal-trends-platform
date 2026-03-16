
from fastapi import APIRouter

router = APIRouter(prefix="/trends")

@router.get("/")
def get_trends():

    return {
        "trending":[
            "Artificial Intelligence",
            "Global Startups",
            "Nepal Technology",
            "Digital Economy"
        ]
    }
