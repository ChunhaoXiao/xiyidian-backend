from fastapi import APIRouter

router = APIRouter(prefix="/api/cate")

@router.get("/")
def get_cate():
    return {
        "code":1,
        "data": [
            {"id":1, "name":"分类1"},
            {"id":2, "name":"分类2"},
            {"id":3, "name":"分类3"}
        ]
    }