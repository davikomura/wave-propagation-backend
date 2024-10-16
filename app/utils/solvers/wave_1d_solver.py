import numpy as np

def simulate_wave1d(L, T, c, initial_condition, initial_velocity, 
                    boundary_condition, alpha=1.0, beta=0.0, 
                    Nx=100, Nt=100):
    """
    Simula a equação da onda 1D usando o Método das Diferenças Finitas, permitindo condições iniciais e de contorno personalizadas.
    
    Parâmetros:
    L (float)                   : Comprimento do domínio (ex: corda)
    T (float)                   : Tempo total de simulação
    c (float)                   : Velocidade de propagação da onda
    initial_condition (function) : Função que define a condição inicial u(x, 0)
    initial_velocity (function)  : Função que define a derivada inicial ∂u/∂t(x, 0)
    boundary_condition (string)   : Tipo de condição de contorno ('Dirichlet', 'Neumann' ou 'Robin')
    alpha (float)                : Coeficiente da condição de contorno de Robin
    beta (float)                 : Coeficiente da condição de contorno de Robin
    Nx (int)                    : Número de pontos no espaço
    Nt (int)                    : Número de pontos no tempo
    
    Retorna:
    x (array)  : Posições espaciais
    u (array)  : Solução da onda ao longo do tempo
    """
    
    # Passos de tempo e espaço
    dx = L / (Nx - 1)
    dt = T / (Nt - 1)
    
    # Verificar condição de estabilidade (CFL)
    if dt > dx / c:
        raise ValueError("Condição CFL não satisfeita. Ajuste os parâmetros para satisfazer dt <= dx / c.")
    
    # Inicializar as posições no espaço e a solução u
    x = np.linspace(0, L, Nx)
    u = np.zeros((Nt, Nx))
    
    # Aplicar a condição inicial u(x, 0)
    u[0, :] = initial_condition(x)
    
    # Aplicar a derivada inicial (condição de velocidade ∂u/∂t em t=0)
    for i in range(1, Nx-1):
        u[1, i] = (u[0, i] + dt * initial_velocity(x[i]) 
                   + 0.5 * (c**2 * dt**2 / dx**2) * (u[0, i+1] - 2*u[0, i] + u[0, i-1]))
    
    # Esquema de diferenças finitas para t > 0
    for n in range(1, Nt-1):
        for i in range(1, Nx-1):
            u[n+1, i] = (2 * u[n, i] - u[n-1, i] 
                         + (c**2 * dt**2 / dx**2) * (u[n, i+1] - 2 * u[n, i] + u[n, i-1]))
        
        # Aplicar condições de contorno
        if boundary_condition == 'Dirichlet':
            u[n, 0] = 0  # Valor fixo na borda esquerda
            u[n, -1] = 0  # Valor fixo na borda direita
        elif boundary_condition == 'Neumann':
            u[n, 0] = u[n, 1]  # Valor igual ao próximo ponto (sem fluxo na borda esquerda)
            u[n, -1] = u[n, -2]  # Valor igual ao penúltimo ponto (sem fluxo na borda direita)
        elif boundary_condition == 'Robin':
            # Aplicando condição de Robin: α * u + β * ∂u/∂x = 0
            # Aqui assumimos que ∂u/∂x é aproximado por diferenças finitas
            u[n, 0] = (-beta / alpha) * u[n, 1]  # Borda esquerda
            u[n, -1] = (-beta / alpha) * u[n, -2]  # Borda direita

    # Retornar a solução como listas para fácil conversão em JSON
    return x.tolist(), u.tolist()
