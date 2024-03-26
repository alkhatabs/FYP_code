import math

def cordic_iteration(x, y, z, mode):
    if mode == 'cosine':
        x_new = x - y * (2**(-z))
        y_new = y + x * (2**(-z))
        z_new = z - 1
    elif mode == 'sine':
        x_new = x + y * (2**(-z))
        y_new = y - x * (2**(-z))
        z_new = z - 1
    else:
        raise ValueError("Invalid mode. Use 'cosine' or 'sine'.")

    return x_new, y_new, z_new

def cordic(theta, iterations=10, mode='cosine'):
    x, y, z = 1.0, 0.0, 0.0

    for i in range(iterations):
        x, y, z = cordic_iteration(x, y, z, mode)

    if mode == 'cosine':
        return x
    elif mode == 'sine':
        return y

def target_angle_convergence(target_angle, iterations=10):
    angle = 90.0
    for i in range(iterations):
        angle -= math.degrees(math.atan(2**(-i)))

    while angle < target_angle:
        angle += 0.01  # Adjust the step size as needed for convergence

    return angle

target_angle = 32.5
converged_angle = target_angle_convergence(target_angle)
result_cosine = cordic(math.radians(converged_angle), iterations=10, mode='cosine')
result_sine = cordic(math.radians(converged_angle), iterations=10, mode='sine')

print(f"Target Angle: {target_angle} degrees")
print(f"Converged Angle: {converged_angle} degrees")
print(f"Cosine({converged_angle}): {result_cosine}")
print(f"Sine({converged_angle}): {result_sine}")