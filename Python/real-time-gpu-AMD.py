import pyopencl as cl
import numpy as np
import matplotlib.pyplot as plt
import random
import time

# OpenCL platform és eszköz választása
platform = cl.get_platforms()[0]  # Az első elérhető platform
device = platform.get_devices()[0]  # Az első elérhető eszköz (pl. AMD GPU)
context = cl.Context([device])
queue = cl.CommandQueue(context, device)

# OpenCL program
program_src = """
__kernel void sierpinski(__global float* points, const int iterations, const float A[2], const float B[2], const float C[2]) {
    int i = get_global_id(0);
    float2 current_point = (float2)(0.5f, 0.5f);
    
    for (int j = 0; j < iterations; ++j) {
        int random_vertex = (int)(i * 3.0f) % 3;
        if (random_vertex == 0)
            current_point = (current_point + (float2)(A[0], A[1])) * 0.5f;
        else if (random_vertex == 1)
            current_point = (current_point + (float2)(B[0], B[1])) * 0.5f;
        else
            current_point = (current_point + (float2)(C[0], C[1])) * 0.5f;
    }
    points[i * 2] = current_point.x;
    points[i * 2 + 1] = current_point.y;
}
"""

# A háromszög csúcsai
A = np.array([0.0, 0.0], dtype=np.float32)
B = np.array([1.0, 0.0], dtype=np.float32)
C = np.array([0.5, np.sqrt(3) / 2], dtype=np.float32)

# Iterációk száma
iterations = 10000

# OpenCL bufferek létrehozása
points_buffer = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, np.zeros((iterations, 2), dtype=np.float32))

# OpenCL program kompilezése
program = cl.Program(context, program_src).build()

# Kernel futtatása
start_time = time.time()
program.sierpinski(queue, (iterations,), None, points_buffer, np.int32(iterations), A, B, C)

# Eredmények kiolvasása
points = np.zeros((iterations, 2), dtype=np.float32)
cl.enqueue_copy(queue, points, points_buffer).wait()

# Valós idejű ábra frissítés
plt.figure()
plt.axis('equal')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.title('Sierpiński-háromszög (OpenCL - AMD GPU)')

for i in range(0, iterations, 100):
    plt.plot(points[:i, 0], points[:i, 1], 'b.', markersize=1)
    percent_complete = (i / iterations) * 100
    elapsed_time = time.time() - start_time
    print(f"Progress: {percent_complete:.2f}% - Elapsed Time: {elapsed_time:.2f} seconds")
    plt.pause(0.001)  # Frissítés

plt.show()
print("Progress: 100.00% - Done!")
