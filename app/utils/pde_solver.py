from app.utils.solvers.wave_1d_solver import simulate_wave1d
from app.utils.solvers.wave_2d_solver import simulate_wave2d
from app.utils.solvers.wave_3d_solver import simulate_wave3d
from app.utils.solvers.dalembert_solver import solve_dalembert

def solve_wave_equation(equation_type: str, L: float = None, Lx: float = None, Ly: float = None, Lz: float = None,
                        T: float = None, c: float = None, initial_condition: str = None,
                        initial_velocity: str = None, boundary_condition: str = 'Dirichlet',
                        alpha: float = None, beta: float = None, Nx: int = 100, Ny: int = 100, Nz: int = 100, Nt: int = 100):
    """
    Soluciona diferentes tipos de equações de onda com base no tipo especificado pelo usuário.
    
    Parâmetros:
    - equation_type: Tipo de equação de onda ('wave1d', 'wave2d', 'wave3d', 'dalembert').
    - L, Lx, Ly, Lz: Dimensões do domínio (dependendo da equação).
    - T: Tempo total de simulação.
    - c: Velocidade de propagação da onda.
    - initial_condition: Condição inicial da onda.
    - initial_velocity: Derivada inicial da onda.
    - boundary_condition: Tipo de condição de contorno ('Dirichlet', 'Neumann', 'Robin').
    - alpha, beta: Coeficientes da condição de contorno de Robin.
    - Nx, Ny, Nz: Número de pontos no espaço.
    - Nt: Número de pontos no tempo.

    Retorna:
    - A solução da equação de onda.
    """

    if equation_type == 'wave1d':
        return simulate_wave1d(L, T, c, initial_condition, initial_velocity, 
                               boundary_condition, alpha, beta, Nx, Nt)
    elif equation_type == 'wave2d':
        return simulate_wave2d(Lx, Ly, T, c, initial_condition, initial_velocity, 
                               boundary_condition, alpha, beta, Nx, Ny, Nt)
    elif equation_type == 'wave3d':
        return simulate_wave3d(Lx, Ly, Lz, T, c, initial_condition, initial_velocity, 
                               boundary_condition, alpha, beta, Nx, Ny, Nz, Nt)
    elif equation_type == 'dalembert':
        return solve_dalembert(L, T, c, initial_condition, initial_velocity, boundary_condition, Nx, Nt)
    else:
        raise ValueError("Tipo de equação desconhecido.")
