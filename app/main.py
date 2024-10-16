from fastapi import FastAPI
from app.routers import wave_simulation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Wave Simulator API",
    description="API para simulação de equações de onda em diferentes meios",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(wave_simulation.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Simulador de Ondas!"}
