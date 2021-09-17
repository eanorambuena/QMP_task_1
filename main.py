# Import required packages

import qiskit as q

# Classical

vector = [2, 5, 7, 10]

# Quantum

q_registers, c_registers = 7, 7

circuit = q.QuantumCircuit(q_registers, c_registers)


