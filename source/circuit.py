from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


def get_backend(token: str):
    service = QiskitRuntimeService(channel='ibm_quantum', token=token)
    backend = service.least_busy(
        operational=True, 
        simulator=False, 
        min_num_qubits=127
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


def get_job(isa_qc, backend, num_shots):
    sampler = Sampler(backend=backend)
    job = sampler.run([isa_qc] * 100, shots=num_shots)

    print("Sending job complete!")

    return job


def execute(token: str, num_shots: int) -> any:
    backend = get_backend(token)
    qc = get_circuit(127)
    isa_qc = get_isa_circuit(qc, backend)
    job = get_job(isa_qc, backend, num_shots)
    result = job.result()

    print("Execution complete!")

    return result


if __name__ == '__main__':
    raise RuntimeError("Please 'main.py' to run.")