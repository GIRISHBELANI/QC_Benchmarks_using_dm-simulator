# Qiskit dm_simulator User Guide
***
The details about the implementation of the density matrix simulator is given in the `arxiv` paper [1908.05154](https://arxiv.org/abs/1908.05154).
## Installation
> **Optional :** We advise you to use a virtual environment to install the files. Virtual environment can be created using `conda`.  
>
> ```bash
> conda create -y -n QiskitAakash python=3.8 pandas openpyxl
> ```
> See [this](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) for instruction to install `conda` into your system. You may also give a different name to the environment. In that case, replace QiskitAakash with the name of your choice in the above and below instructions
>
> You can activate/deactivate the virtual environment.
> ```bash
> conda activate QiskitAakash
> conda deactivate
> ```
> Once you have activated the virtual environment follow the instructions below.

Installing from source requires that you have the Rust compiler on your system. To install the Rust compiler the recommended path is to use rustup, which is a cross-platform Rust installer. To use rustup you can go to:

https://rustup.rs/

which will provide instructions for how to install rust on your platform. Besides rustup there are other [installation methods](https://forge.rust-lang.org/infra/other-installation-methods.html) available too.

OR

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
python -m pip install setuptools-rust
```

Once the Rust compiler is installed, you are ready to install Qiskit Aakash.
1. Clone the qiskit-aakash repo and enter it.
```bash
git clone -b terra_upgrade https://github.com/indian-institute-of-science-qc/qiskit-aakash.git
cd qiskit-aakash
```
2. Create a separate branch upto a stable commit
```bash
git checkout -b branchName bea98fbff86c234c0b1990add17493a1e86917cb
```

Note: If you're getting an error related to ipython_genutils, use below commands 
```bash
python -m pip install ipython-genutils
conda install -c conda-forge ipython_genutils
pip install --upgrade pip
```

3. If you want to run tests or linting checks, install the developer requirements.
```bash
pip install -r requirements-dev.txt
```
4. Install qiskit-aakash.
```bash
pip install .
```
If you want to install in editable mode (recommended), use 
```bash
pip install -e .
```

> If you want to use it in [`Google Colab`](https://colab.research.google.com/) (easier and convenient but only works online)then the same commands will work
> ```
> !git clone https://github.com/indian-institute-of-science-qc/qiskit-aakash.git && python3 -m pip install qiskit-aakash/
> ```

The code for the new back-end `dm_simulator` can be found in [`dm_simulator.py`](qiskit/providers/basicaer/dm_simulator.py).
This back-end also uses some functionalities from [`basicaertools.py`](qiskit/providers/basicaer/basicaertools.py).

## Executing Commands for QSim

### Using benchmark_runner.py file 
(chnage the algorithm names according to mentioned in benchmark_runner.py file, change other parameters according to your need)
```bash
python3 _common/qsim/benchmark_runner.py --algorithm shors --min_qubit 4 --max_qubit 10 --thermal_factor 0.9 --decoherence_factor 1.0 --depolarization_factor 0.9 --rotation_error 1.0 0.0 1.0 0.0 1.0 0.0 --tsp_model_error 1.0 0.0
```

### To run individual benchmark files without introducing any noise (example command for deutsch-jozsa)
```bash
python3 deutsch-jozsa/qsim/dj_benchmark.py
```

### To run individual benchmark file with introducing noise parameters 
(adjust noise parameter according to your experiment, below command introduced thermal_factor and depolarization_factor noises just for example)
```bash
python3 deutsch-jozsa/qsim/dj_benchmark.py --thermal_factor 0.9 --decoherence_factor 1.0 --depolarization_factor 0.9 --rotation_error 1.0 0.0 1.0 0.0 1.0 0.0 --tsp_model_error 1.0 0.0
```

Since by default plot and show_partition parameters are set to False, if you want to set as True, run below command:
```bash
python3 deutsch-jozsa/qsim/dj_benchmark.py --plot --show_partition --thermal_factor 0.9 --decoherence_factor 1.0 --depolarization_factor 0.9 --rotation_error 1.0 0.0 1.0 0.0 1.0 0.0 --tsp_model_error 1.0 0.0
```

## Example
Once installed, files can be changed and run in python (for instructions to use the qiskit-terra part of the software, please visit [here](https://github.com/Qiskit/qiskit-terra)). For example,
```bash
python3
```
```python
from qiskit import QuantumCircuit,BasicAer,execute
qc = QuantumCircuit(2)
# Gates
qc.x(1)
qc.cx(0,1)
# execution
backend = BasicAer.get_backend('dm_simulator')
run = execute(qc,backend)
result = run.result()
print(result.results[0].data.densitymatrix)
```
It would output the resultant `densitymatrix` as,
```python
[[0 0 0 0]
[0 1 0 0]
[0 0 0 0]
[0 0 0 0]]
```
There are some `jupyter` notebooks in the repository which provide detailed examples about how to use this simulator.
Those can be viewed in [`Github`](dm_simulator_user_guide/user_guide.ipynb). But the easiest way to interact with them is by using [`Binder Image`](https://mybinder.org/v2/gh/indian-institute-of-science-qc/qiskit-aakash/master?filepath=.%2Fdm_simulator_user_guide%2Fuser_guide.ipynb).

## NOTE :

As while installing a specific version of Qiskit-Aakash repository for dm_simulator please note that it has the following issues:

**1. Reverse Order of Probabilities :**

Density Matrix simulator (on the basis of Basic-Aer) represents the **Measurements** in the reverse order when compared with that of QASM-Simulator.

- To resolve this we are using a built-in functionality called **reverse_bits()**.

- This function places measurement gates in reverse order of which QASM Simulator uses.

- Use this function while creating the Quantum Circuit.

For example:
```python
qc = BernsteinVazirani(num_qubits, s_int, method).reverse_bits()
```

**2. Partial and Ensemble probabilities :**

Mainly there are 2 basis for the measurement:

a. Measurement with Ensemble Probability

b. Measurement with Partial Probability

In this repository we mostly measure our resulting probabilities using Partial Probability. 

- While creating Quantum Circuit, if we use basis as "Ensemble" then we get our measurements as **ensemble_probability** in our result object. But if we haven't mentioned any basis specifically, dm_simulator by default gives **partial_probability** in our result object.


**3. Issues with Ensemble Probability Measurement :**

Ensemble probability measures every qubit in the quantum circuit and returns measurements accordingly. But in our benchmarking suite most of the algorithms use **n-1** measurements for **n** number of qubits. This is because the remaining one qubit is considered as **auxillary** which isn't meant for measurement. (Check the algorithms for better clarification).

- Due to this reason we are not using Ensemble-measurement for our benchmarking.

**4. Limitations of Partial probability measurement :**

Atleast **2** measurements are needed to be performed (i.e., the Quantum circuit should have **atleast 2 measurement gates** at the output) to calculate **partial_probability** values. Anything less-than **2** doesn't work, it simply throws an error. ***This version of DM_Simulator doesn't have the implementation to get the partial_probability for single-qubit measurement***.

**Information about benchmarking limitations on native computers will be available as README of each directory of Algorithm.**
