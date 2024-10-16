from app.utils.solvers.wave_1d_solver import simulate_wave1d
from app.utils.solvers.wave_2d_solver import solve_wave_2d
from app.utils.solvers.wave_3d_solver import solve_wave_3d
from app.utils.solvers.dalembert_solver import solve_dalembert

def solve_wave_equation(equation_type: str, velocity: float, frequency: float, amplitude: float, boundary_condition: str):
    if equation_type == 'wave1d':
        return simulate_wave1d(velocity, frequency, amplitude, boundary_condition)
    elif equation_type == 'wave2d':
        return solve_wave_2d(velocity, frequency, amplitude)
    elif equation_type == 'wave3d':
        return solve_wave_3d(velocity, frequency, amplitude)
    elif equation_type == 'dalembert':
        return solve_dalembert(velocity, frequency, amplitude)
    else:
        raise ValueError("Tipo de equação desconhecido.")
