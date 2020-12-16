"""Machine learning functions"""

from fastapi import APIRouter

router = APIRouter()  # Router ready to go


@router.get("/sum")  # Adding endpoints to the router
async def my_sum(a: int, b: int):
    return {"sum": a + b}
