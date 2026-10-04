import matplotlib.pyplot as plt
import math

height_start = float(input('From what height does the ball fall? '))
time_step = float(input('Enter the time step for the simulation (e.g., 1 or 0.1) '))
if time_step <= 0:
    print('Time step must be greater than 0')
gravity = 9.81

def simulate_fall(height_start, time_step, show_steps=True):
    time = 0.0
    current_height = height_start
    speed = 0.0
    times = [time]
    heights = [current_height]
    speeds = [speed]

    while current_height > 0:
        current_height = current_height - speed * time_step
        speed = speed + gravity * time_step
        time += time_step

        hit_ground = False
        if current_height <= 0:
            current_height = 0.0
            hit_ground = True

        times.append(time)
        heights.append(current_height)
        speeds.append(speed)

        if show_steps:
            print(f'Time: {round(time, 2)} s | Height: {round(current_height, 2)} m | Speed: {round(speed, 2)} m/s')

            if hit_ground:
                print('The ball has hit the ground.')

    return(time, times, heights, speeds)


def theoretical(height_start):
    theoretical_fall_time = math.sqrt(2 * height_start / gravity)
    return theoretical_fall_time


def difference(simulated_fall_time, theoretical_fall_time):
    return abs(simulated_fall_time - theoretical_fall_time)


def time_step_function(height_start, time_step):
    time, times, heights, speeds = simulate_fall(height_start, time_step, False)
    theoretical_time = theoretical(height_start)
    error = difference(time, theoretical_time)
    return time_step, time, theoretical_time, error


simulated_fall_time, times, heights, speeds = simulate_fall(height_start, time_step, True)
theoretical_fall_time = theoretical(height_start)

print (f'\nSimulated fall time: {round(simulated_fall_time, 6)} s')
print (f'Theoretical fall time: {round(theoretical_fall_time, 6)} s')
print (f'Fall time error: {round(difference(simulated_fall_time, theoretical_fall_time), 6)} s')



print ('\ntime step | simulated time | theoretical time | error')
print ('------------------------------------------------------')

time_steps = [10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
errors = []

for dt in time_steps:
    step, simulated, theoretical_time, error = time_step_function(height_start, dt)
    step_text = f"{step:.5f}".rstrip("0").rstrip(".")
    simulated_text = f"{simulated:.5f}".rstrip("0").rstrip(".")
    theoretical_text = f"{theoretical_time:.5f}".rstrip("0").rstrip(".")
    error_text = f"{error:.5f}".rstrip("0").rstrip(".")

    print(f"{step_text:<9} | {simulated_text:<14} | {theoretical_text:<16} | {error_text:<10}")
    errors.append(error)

plt.plot(time_steps, errors, marker='o')
plt.xlabel('Time step')
plt.ylabel('Error in seconds')
plt.xscale('log')
plt.yscale('log')
plt.title('Euler Method Convergence')
plt.grid(True)
plt.show()


plt.plot(times, heights)
plt.xlabel('Time in s')
plt.ylabel('Height in m')
plt.title('Falling ball')
plt.show()

plt.plot(times, speeds)
plt.xlabel('Time in s')
plt.ylabel('Speed in m/s')
plt.title('Falling Ball')
plt.show()


