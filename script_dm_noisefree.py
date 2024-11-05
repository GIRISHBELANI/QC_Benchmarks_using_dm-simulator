# # Importing execute and metrics modules

import sys
import cupy as cp
sys.path[1:1] = [ "../../_common", "../../_common/qsim" ]
sys.path[1:1] = [ "_common", "_common/qsim" ]
import execute as ex
import metrics as metrics

metrics.show_plot_images = False
metrics.data_suffix = "_noisefree"





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
cp.cuda.Device(0).use()
print('running on GPU 0')
dj_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Bernstein-Vazirani-----------------------------------------------

max_qubits=15

sys.path.insert(1, "bernstein-vazirani/qsim")
import bv_benchmark
cp.cuda.Device(1).use()
print('running on GPU 1')
bv_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Hidden-Shift-----------------------------------------------

max_qubits=15

sys.path.insert(1, "hidden-shift/qsim")
import hs_benchmark
cp.cuda.Device(0).use()
print('running on GPU 0')
hs_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Quantum-Fourier-Transform-----------------------------------------------

# QFT Method-1

max_qubits=15

sys.path.insert(1, "quantum-fourier-transform/qsim")
import qft_benchmark
cp.cuda.Device(1).use()
print('running on GPU 1')
qft_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)


# QFT Method-2

max_qubits=15

sys.path.insert(1, "quantum-fourier-transform/qsim")
import qft_benchmark
cp.cuda.Device(0).use()
print('running on GPU 0')
qft_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=2,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Phase-Estimation-----------------------------------------------

max_qubits=15

sys.path.insert(1, "phase-estimation/qsim")
import pe_benchmark
cp.cuda.Device(1).use()
print('running on GPU 1')
pe_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Amplitude-Estimation-----------------------------------------------

max_qubits=13

sys.path.insert(1, "amplitude-estimation/qsim")
import ae_benchmark
cp.cuda.Device(0).use()
print('running on GPU 0')
ae_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Hamiltonian-Simulation-----------------------------------------------

max_qubits=15

sys.path.insert(1, "hamiltonian-simulation/qsim")
import hamiltonian_simulation_benchmark
cp.cuda.Device(0).use()
print('running on GPU 0')
hamiltonian_simulation_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Grover's-Search--------------------------------------------------

max_qubits=12

sys.path.insert(1, "grovers/qsim")
import grovers_benchmark
cp.cuda.Device(1).use()
print('running on GPU 1')
grovers_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Monte-Carlo-Sampling----------------------------------------------

max_qubits=14

sys.path.insert(1, "monte-carlo/qsim")
import mc_benchmark
cp.cuda.Device(0).use()
print('running on GPU 0')
mc_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------Variational-Quantum-Eigensolver ---------------------------------

max_qubits=12

sys.path.insert(1, "vqe/qsim")
import vqe_benchmark
cp.cuda.Device(1).use()
print('running on GPU 1')
vqe_num_shots=4098
vqe_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits,
                max_circuits=max_circuits, num_shots=vqe_num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# ------------------------------------------------Shor’s-Order-Finding-Algorithm ----------------------------------

# Shor's Algorithm (Method-1)

max_qubits=15

sys.path.insert(1, "shors/qsim")
import shors_benchmark
cp.cuda.Device(0).use()
print('running on GPU 0')
shors_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, max_circuits=1, num_shots=num_shots,
                method=1,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)




# -----------------------------------------------HHL-Linear-Solver-------------------------------------------------

max_qubits=15

sys.path.insert(1, "hhl/qsim")
import hhl_benchmark

hhl_benchmark.verbose=False
cp.cuda.Device(1).use()
print('running on GPU 1')

hhl_benchmark.run(min_qubits=min_qubits, max_qubits=max_qubits, skip_qubits=skip_qubits,
                max_circuits=max_circuits, num_shots=num_shots,
                method=1, use_best_widths=True,
                backend_id=backend_id, provider_backend=provider_backend,
                exec_options=exec_options)



# -----------------------------------------------MaxCut-QAOA-Algorithm---------------------------------------------

max_qubits=10

sys.path.insert(1, "maxcut/qsim")
import maxcut_benchmark
cp.cuda.Device(0).use()
print('running on GPU 0')

maxcut_benchmark.run(
    min_qubits=min_qubits, max_qubits=max_qubits, max_circuits=max_circuits, num_shots=num_shots,
    method=1, rounds=1, do_fidelities=True,
    backend_id=backend_id, provider_backend=provider_backend,
    exec_options=exec_options
)


# ---------------------------------------------Creation of xls file from __data/*****.json file---------------------------------------------

# Define the benchmark folder and API as needed (leave blank to get json file from top-level __data folder)
benchmark_folder = ''   
api = ''               #qsim
backend_id = 'dm_simulator_noisefree'       

# Call the json_to_excel function
metrics.json_to_excel(benchmark_folder, api, backend_id)


