# version 0.7.1 by romangorbunov91
# 13-Sep-2025
import numpy as np

def momentum(grad_func, x_init, learning_rate, beta, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = int(1e7)
    
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    p = 0
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        p = beta * p + (1-beta) * learning_rate * grad
        x -= p
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
    return x, trajectory, i+1, grad_counter

def nesterov(grad_func, x_init, learning_rate, beta, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = int(1e7)

    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    p = 0
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        p = beta * p + (1-beta) * learning_rate * grad_func(x - learning_rate*grad)
        x -= p
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
    return x, trajectory, i+1, grad_counter

def adagrad(grad_func, x_init, learning_rate, eps_zero, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = int(1e7)
    
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
    return x, trajectory, i+1, grad_counter

def rmsprop(grad_func, x_init, learning_rate, beta, eps_zero, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = int(1e7)
    
    grad_counter = 0
    
    x = x_init.copy()
    trajectory = []
    trajectory.append(x.copy())
    G = np.array([0.0]*len(x_init))
    for i in range(iteration_max):
        grad = grad_func(x)
        grad_counter += 1
        
        for idx, grad_coord in enumerate(grad):
            G[idx] = beta * G[idx] + (1-beta) * grad_coord**2
            x[idx] -= learning_rate / np.sqrt(G[idx] + eps_zero) * grad_coord
        
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
    return x, trajectory, i+1, grad_counter

def adadelta(grad_func, x_init, beta, eps_zero, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = int(1e7)
    
    grad_counter = 0
    
    x = x_init.copy()
    
    trajectory = []
    trajectory.append(x.copy())
    G = np.array([0.0]*len(x_init))
    H = np.array([0.0]*len(x_init))
    
    for i in range(iteration_max):
        # Compute Gradient.
        grad = grad_func(x)
        grad_counter += 1
        
        for idx, grad_coord in enumerate(grad):
            # Accumulate Gradient.
            G[idx] = beta * G[idx] + (1-beta) * grad_coord**2
            # Compute Update.
            d_x = - np.sqrt((H[idx] + 1e-10) / (G[idx] + eps_zero)) * grad_coord
            # Accumulate Updates.
            H[idx] = beta * H[idx] + (1-beta) * d_x**2
            # Apply Update.
            x[idx] += d_x
        
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
    return x, trajectory, i+1, grad_counter

def adam(grad_func, x_init, learning_rate, beta1, beta2, eps_zero, tolerance, printoutput):
    # 'x_init' must be np.array([val1, val2]).
    # 'printoutput' is BOOL.
    iteration_max = int(1e7)
    
    grad_counter = 0
    
    x = x_init.copy()
    
    trajectory = []
    trajectory.append(x.copy())
    m = np.array([0.0]*len(x_init))
    v = np.array([0.0]*len(x_init))
    
    for i in range(iteration_max):
        # Compute Gradient.
        grad = grad_func(x)
        grad_counter += 1
        
        for idx, grad_coord in enumerate(grad):
            # Update biased first moment estimate.
            m[idx] = beta1 * m[idx] + (1-beta1) * grad_coord
            # Update biased second raw moment estimate.
            v[idx] = beta2 * v[idx] + (1-beta2) * grad_coord**2
            # Apply Update.
            x[idx] -= learning_rate * m[idx]/(1 - beta1**(i+1)) / (np.sqrt(v[idx]/(1 - beta2**(i+1)) + eps_zero))
        
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
    return x, trajectory, i+1, grad_counter

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
    grad_counter = 0
    return x, trajectory, i+1, grad_counter