from fastapi import APIRouter, HTTPException
from app.schemas.simulation import SimulationRequest, SimulationResponse
from app.utils.pde_solver import solve_wave_equation

router = APIRouter(
    prefix="/simulation",
    tags=["Simulação"]
)

@router.post("/run", response_model=SimulationResponse)
async def run_simulation(simulation_request: SimulationRequest):
    try:
        result = solve_wave_equation(
            equation_type=simulation_request.equation_type,
            velocity=simulation_request.velocity,
            frequency=simulation_request.frequency,
            amplitude=simulation_request.amplitude,
            boundary_condition=simulation_request.boundary_condition,
        )
        return SimulationResponse(data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a simulação: {e}")
