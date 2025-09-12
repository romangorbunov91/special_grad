# version 0.0.1 by romangorbunov91
# 11-Sep-2025
import numpy as np

def momentum_descent(grad_func, x_init, learning_rate, beta, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    p_prev = 0
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        p = beta * p_prev + (1-beta) * learning_rate * grad
        x -= p
        p_prev = p.copy()
        trajectory.append(x.copy())
        
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)

        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(grad_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(grad_norm,4))
    # always func_counter = 0
    return x, trajectory, i+1, 0, grad_counter

def nesterov_descent(grad_func, x_init, learning_rate, beta, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    p_prev = 0
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        p = beta * p_prev + (1-beta) * learning_rate * grad_func(x - learning_rate*grad)
        x -= p
        p_prev = p.copy()
        trajectory.append(x.copy())
        
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)

        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(grad_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(grad_norm,4))
    # always func_counter = 0
    return x, trajectory, i+1, 0, grad_counter

def adagrad_descent(grad_func, x_init, learning_rate, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    eps_zero = 1e-6
    
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    G = np.array([0.0]*len(x_init))
    G_prev = G.copy()
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        for idx, grad_coord in enumerate(grad):
            G[idx] = G_prev[idx] + grad_coord**2
            x[idx] -= learning_rate / np.sqrt(G[idx] + eps_zero) * grad_coord
        
        G_prev = G.copy()
        trajectory.append(x.copy())
        
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)

        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(grad_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(grad_norm,4))
    # always func_counter = 0
    return x, trajectory, i+1, 0, grad_counter

def rmsprop_descent(grad_func, x_init, learning_rate, beta, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 10000000
    
    eps_zero = 1e-6
    
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    G = np.array([0.0]*len(x_init))
    G_prev = G.copy()
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        for idx, grad_coord in enumerate(grad):
            G[idx] = beta * G_prev[idx] + (1-beta) * grad_coord**2
            x[idx] -= learning_rate / np.sqrt(G[idx] + eps_zero) * grad_coord
        
        G_prev = G.copy()
        trajectory.append(x.copy())
        
        grad_norm = np.linalg.norm(grad, ord=None, axis=None)

        if (grad_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(grad_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(grad_norm,4))
    # always func_counter = 0
    return x, trajectory, i+1, 0, grad_counter

# Метод сопряженных градиентов.
def conjugate_grad_descent(A, b, x_init, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = 100
    
    x = (np.matrix(x_init)).T.copy()
    trajectory = []
    trajectory.append(np.array(x.T).flatten().tolist().copy())

    r = b.T - A * x
    r_prev = r.copy()
    p = r.copy()

    for i in range(iteration_max):
        learning_rate = ((r.T * r)/(p.T * A*p)).item()
        
        x += learning_rate * p
        trajectory.append(np.array(x.T).flatten().tolist().copy())

        r -= learning_rate * A * p
        beta = ((r.T * r)/(r_prev.T * r_prev)).item()
        r_prev = r.copy()
        p = r + beta * p
        p_norm = np.linalg.norm(p, ord=None, axis=None)
        
        if (p_norm < tolerance):
            if printoutput:
                print('Iteration:', i)
                print('x-values:', np.round(x,4))
                print('Gradient norm:', np.round(p_norm,4))
            break
    if printoutput:
        print('Iteration:', i)
        print('x-values:', np.round(x,4))
        print('Gradient norm:', np.round(p_norm,4))
    func_counter = 0
    grad_counter = 0
    return x, trajectory, i+1, func_counter, grad_counter