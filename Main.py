from fastapi import FastAPI
import os
from Controllers.UrlController import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Gheychi",
    description="Im Gonna keep it Shorter for you but dont touch it , it may get bigger and spit on you on worse case",
    version="0.01",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))

    uvicorn.run("Main:app", host=host, port=port, reload=True)
