from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.utils.pde_solver import solve_wave_equation

# Criação da aplicação FastAPI
app = FastAPI()

# Configurações para permitir que o frontend se comunique com o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que todas as origens se conectem, ajuste conforme necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definição do modelo para os parâmetros da simulação
class SimulationParameters(BaseModel):
    equation_type: str
    L: float = None
    Lx: float = None
    Ly: float = None
    Lz: float = None
    T: float
    c: float
    initial_condition: str
    initial_velocity: str
    boundary_condition: str
    alpha: float = None
    beta: float = None
    Nx: int = 100
    Ny: int = 100
    Nz: int = 100
    Nt: int = 100

# Rota para processar a simulação
@app.post("/simulate/")
async def simulate_wave(params: SimulationParameters):
    try:
        # Chama a função para resolver a equação da onda com os parâmetros fornecidos
        result = solve_wave_equation(params)
        return {"x": result[0], "u": result[1]}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na simulação: {e}")

# Rota básica para testar se o servidor está ativo
@app.get("/")
async def root():
    return {"message": "Simulador de Ondas em execução"}
