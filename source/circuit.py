from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


def get_backend(token: str, min_num_qubits: int):
    service = QiskitRuntimeService(channel='ibm_quantum', token=token)
    backend = service.least_busy(
        operational=True, 
        simulator=False, 
        min_num_qubits=min_num_qubits
    )
    
    print(f"Chosen Backend: {backend.name}")
    
    return backend


def get_circuit(num_qubit: int):
    qc = QuantumCircuit(num_qubit)
    for i in range(num_qubit):
        qc.h(i)
    qc.measure_all()

    print("Circuit generation complete!")

    return qc


def get_isa_circuit(qc, backend):
    pass_manager = generate_preset_pass_manager(optimization_level=0, backend=backend)
    isa_qc = pass_manager.run(qc)

    print("Transpilation complete!")

    return isa_qc


def dispatch_job(isa_qc, backend, reps: int):
    sampler = Sampler(backend=backend)
    job = sampler.run([isa_qc] * reps, shots=backend.max_shots)

    print("Job dispatching complete!")

    return job


def execute(token: str, min_num_qubits: int, reps: int):
    backend = get_backend(token, min_num_qubits)
    qc = get_circuit(backend.num_qubits)
    isa_qc = get_isa_circuit(qc, backend)
    job = dispatch_job(isa_qc, backend, reps)
    result = job.result()

    print("Job execution complete!")

    return result


if __name__ == '__main__':
    raise RuntimeError("Please use 'main.py' to run.")