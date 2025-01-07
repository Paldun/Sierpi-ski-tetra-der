import pyopencl as cl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import time

# OpenCL platform és eszköz választása
platform = cl.get_platforms()[0]  # Az első elérhető platform
device = platform.get_devices()[0]  # Az első elérhető eszköz (pl. AMD GPU)
context = cl.Context([device])
queue = cl.CommandQueue(context, device)

# OpenCL program
program_src = """
__kernel void sierpinski(__global float* points, const int iterations, const float A[3], const float B[3], const float C[3], const float D[3]) {
    int i = get_global_id(0);
    float3 current_point = (float3)(0.5f, 0.5f, 0.5f);
    
    for (int j = 0; j < iterations; ++j) {
        int random_vertex = (int)(i * 4.0f) % 4;
        if (random_vertex == 0)
            current_point = (current_point + (float3)(A[0], A[1], A[2])) * 0.5f;
        else if (random_vertex == 1)
            current_point = (current_point + (float3)(B[0], B[1], B[2])) * 0.5f;
        else if (random_vertex == 2)
            current_point = (current_point + (float3)(C[0], C[1], C[2])) * 0.5f;
        else
            current_point = (current_point + (float3)(D[0], D[1], D[2])) * 0.5f;
    }
    points[i * 3] = current_point.x;
    points[i * 3 + 1] = current_point.y;
    points[i * 3 + 2] = current_point.z;
}
"""

# Tetraéder csúcsai
A = np.array([0.0, 0.0, 0.0], dtype=np.float32)
B = np.array([1.0, 0.0, 0.0], dtype=np.float32)
C = np.array([0.5, np.sqrt(3) / 2, 0.0], dtype=np.float32)
D = np.array([0.5, np.sqrt(3) / 6, np.sqrt(2 / 3)], dtype=np.float32)

# Iterációk száma
iterations = 10000

# OpenCL bufferek létrehozása
points_buffer = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, np.zeros((iterations, 3), dtype=np.float32))

# OpenCL program kompilezése
program = cl.Program(context, program_src).build()

# Kernel futtatása
start_time = time.time()
program.sierpinski(queue, (iterations,), None, points_buffer, np.int32(iterations), A, B, C, D)

# Eredmények kiolvasása
points = np.zeros((iterations, 3), dtype=np.float32)
cl.enqueue_copy(queue, points, points_buffer).wait()

# Valós idejű ábra frissítés
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Sierpiński-tetraéder (OpenCL - AMD GPU)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

for i in range(0, iterations, 100):
    ax.scatter(points[:i, 0], points[:i, 1], points[:i, 2], color='b', s=1)
    percent_complete = (i / iterations) * 100
    elapsed_time = time.time() - start_time
    print(f"Progress: {percent_complete:.2f}% - Elapsed Time: {elapsed_time:.2f} seconds")
    plt.pause(0.001)  # Frissítés

plt.show()
print("Progress: 100.00% - Done!")
