from pydantic import BaseModel

class SimulationRequest(BaseModel):
    equation_type: str
    velocity: float
    frequency: float
    amplitude: float
    boundary_condition: str

class SimulationResponse(BaseModel):
    data: list
