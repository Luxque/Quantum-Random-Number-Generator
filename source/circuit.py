from qiskit import QuantumCircuit
from qiskit_ibm_runtime import IBMBackend, QiskitRuntimeService, SamplerV2 as Sampler, Batch
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


def get_backend(token: str, min_num_qubits: int) -> IBMBackend:
    service = QiskitRuntimeService(channel='ibm_quantum', token=token)
    backend = service.least_busy(
        operational=True, 
        simulator=False, 
        min_num_qubits=min_num_qubits
    )
    
    print(f"Chosen Backend: {backend.name}")
    
    return backend


def get_circuit(num_qubit: int) -> QuantumCircuit:
    qc = QuantumCircuit(num_qubit)
    for i in range(num_qubit):
        qc.h(i)
    qc.measure_all()

    print("Circuit generation complete!")

    return qc


def get_isa_circuit(qc: QuantumCircuit, backend: IBMBackend) -> QuantumCircuit:
    pass_manager = generate_preset_pass_manager(optimization_level=0, backend=backend)
    isa_qc = pass_manager.run(qc)

    print("Circuit transpilation complete!")

    return isa_qc


def dispatch_jobs(isa_qc: QuantumCircuit, backend: IBMBackend, reps: int) -> list:
    max_circuits = 10
    circuits = []
    for _ in range(reps // max_circuits):
        circuits.append([isa_qc] * max_circuits)
    if (reps % max_circuits != 0):
        circuits.append([isa_qc] * (reps % max_circuits))
    
    jobs = []
    with Batch(backend=backend):
        sampler = Sampler(backend=backend)
        for circuit in circuits:
            job = sampler.run(circuit, shots=backend.max_shots)
            jobs.append(job)

    print("Job dispatching complete!")

    return jobs


def execute(token: str, min_num_qubits: int, reps: int) -> list:
    backend = get_backend(token, min_num_qubits)
    qc = get_circuit(backend.num_qubits)
    isa_qc = get_isa_circuit(qc, backend)
    jobs = dispatch_jobs(isa_qc, backend, reps)
    
    results = []
    for job in jobs:
        result = job.result()
        results.append(result)

    print("Job execution complete!")

    return results


if __name__ == '__main__':
    raise RuntimeError("Please use 'main.py' to run.")