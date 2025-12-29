from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from Models.UrlDto import RequestDto, ResponseDto
from Logic.UrlLogic_Creator import UrlLogic

router = APIRouter()
logic = UrlLogic()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.post("/shorten", response_model=ResponseDto)
async def shorten_the_url(request: RequestDto):
    try:
        result = logic.shorten_the_url_method(request.long_url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{short_code}")
async def redirect_to_long_url(short_code: str):
    try:
        long_url = logic.get_long_url(short_code)
        if not long_url:
            raise HTTPException(status_code=404, detail="Short URL not found")
        return RedirectResponse(url=long_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
