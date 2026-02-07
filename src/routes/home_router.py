import fastapi
router=fastapi.APIRouter()
@router.get("/")
async def home():
    return {"message": "hello World"}