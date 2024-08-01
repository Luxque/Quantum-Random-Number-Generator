import os, math, secrets

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


if __name__ == '__main__':
    print("Welcome to Quantum Random Number Generator!")
    print("─" * os.get_terminal_size().columns)

    num_qubit = int(input("Qubit: "))
    num_shots = int(input("Shots: "))
    token = input("Token: ")
    print("Input complete!")

    service = QiskitRuntimeService(channel='ibm_quantum', token=token)
    backend = service.least_busy(
        operational=True, 
        simulator=False, 
        min_num_qubits=num_qubit
    )
    print(f"Chosen Backend: {backend.name}")
    print(f"Max # of Shots: {backend.max_shots}")

    qc = QuantumCircuit(num_qubit)
    for i in range(num_qubit):
        qc.h(i)
    qc.measure_all()
    print("Circuit generation complete!")

    pass_manager = generate_preset_pass_manager(optimization_level=0, backend=backend)
    isa_qc = pass_manager.run(qc)
    print("Transpilation complete!")

    sampler = Sampler(backend=backend)
    job = sampler.run([isa_qc], shots=num_shots)
    print(f"Job ID: {job.job_id()}")

    result = job.result()
    bit_str_dict = result[0].data.meas.get_counts()
    print("Job complete!")
    
    width = math.floor(math.log10(num_shots-1)) + 1
    index = 0

    while len(bit_str_dict) > 0:
        bit_str = secrets.choice(list(bit_str_dict.keys()))
        if bit_str_dict[bit_str] <= 1:
            del bit_str_dict[bit_str]
        else:
            bit_str_dict[bit_str] -= 1
        
        bit_str_int = int(bit_str, 2)
        print(f"#{index:0{width}d}: {bit_str_int}")

        index += 1
    
    print("─" * os.get_terminal_size().columns)