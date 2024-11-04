# # Importing execute and metrics modules

import sys
sys.path[1:1] = [ "../../_common", "../../_common/qsim" ]
sys.path[1:1] = [ "_common", "_common/qsim" ]
import execute as ex
import metrics as metrics

metrics.show_plot_images = False
metrics.data_suffix = "_noisefree"

import os

def toggle_cuda_visible_devices():
    while True:
        # Get the current value, default to '0' if it's not set
        current_value = os.environ.get("CUDA_VISIBLE_DEVICES", "0")
        
        # Toggle between '0' and '1'
        new_value = "1" if current_value == "0" else "0"
        os.environ["CUDA_VISIBLE_DEVICES"] = new_value
        
        # Print the updated value for confirmation
        print(f"CUDA_VISIBLE_DEVICES set to {new_value}")



min_qubits=6
max_qubits=15
skip_qubits=1
max_circuits=3
num_shots=1
backend_id="dm_simulator"
provider_backend = None
exec_options = {}

# -----------------------------------------------Deutsch-Jozsa-----------------------------------------------

max_qubits=15

sys.path.insert(1, "deutsch-jozsa/qsim")
import dj_benchmark
dj_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Bernstein-Vazirani-----------------------------------------------

max_qubits=15

sys.path.insert(1, "bernstein-vazirani/qsim")
import bv_benchmark
bv_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Hidden-Shift-----------------------------------------------

max_qubits=15

sys.path.insert(1, "hidden-shift/qsim")
import hs_benchmark
hs_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Quantum-Fourier-Transform-----------------------------------------------

# QFT Method-1

max_qubits=15

sys.path.insert(1, "quantum-fourier-transform/qsim")
import qft_benchmark
qft_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()

# QFT Method-2

max_qubits=15

sys.path.insert(1, "quantum-fourier-transform/qsim")
import qft_benchmark
qft_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=2,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Phase-Estimation-----------------------------------------------

max_qubits=15

sys.path.insert(1, "phase-estimation/qsim")
import pe_benchmark
pe_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Amplitude-Estimation-----------------------------------------------

max_qubits=13

sys.path.insert(1, "amplitude-estimation/qsim")
import ae_benchmark
ae_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Hamiltonian-Simulation-----------------------------------------------

max_qubits=15

sys.path.insert(1, "hamiltonian-simulation/qsim")
import hamiltonian_simulation_benchmark
hamiltonian_simulation_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Grover's-Search--------------------------------------------------

max_qubits=12

sys.path.insert(1, "grovers/qsim")
import grovers_benchmark
grovers_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Monte-Carlo-Sampling----------------------------------------------

max_qubits=14

sys.path.insert(1, "monte-carlo/qsim")
import mc_benchmark
mc_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------Variational-Quantum-Eigensolver ---------------------------------

max_qubits=12

sys.path.insert(1, "vqe/qsim")
import vqe_benchmark
vqe_num_shots=4098
vqe_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits,
                max_circuits=max_circuits, num_shots=vqe_num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# ------------------------------------------------Shor’s-Order-Finding-Algorithm ----------------------------------

# Shor's Algorithm (Method-1)

max_qubits=15

sys.path.insert(1, "shors/qsim")
import shors_benchmark
shors_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, max_circuits=1, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()



# -----------------------------------------------HHL-Linear-Solver-------------------------------------------------

max_qubits=15

sys.path.insert(1, "hhl/qsim")
import hhl_benchmark

hhl_benchmark.verbose=False

hhl_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1, use_best_widths=True,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)
toggle_cuda_visible_devices()


# -----------------------------------------------MaxCut-QAOA-Algorithm---------------------------------------------

max_qubits=10

sys.path.insert(1, "maxcut/qsim")
import maxcut_benchmark

maxcut_benchmark.run(
    min_qubits=min_qubits, max_qubits=max_qubits, max_circuits=max_circuits, num_shots=num_shots,
    method=1, rounds=1, do_fidelities=True,
    backend_id=backend_id, provider_backend=provider_backend,
    exec_options=exec_options
)
toggle_cuda_visible_devices()

# ---------------------------------------------Creation of xls file from __data/*****.json file---------------------------------------------

# Define the benchmark folder and API as needed (leave blank to get json file from top-level __data folder)
benchmark_folder = ''   
api = ''               #qsim
backend_id = 'dm_simulator_noisefree'       

# Call the json_to_excel function
metrics.json_to_excel(benchmark_folder, api, backend_id)


