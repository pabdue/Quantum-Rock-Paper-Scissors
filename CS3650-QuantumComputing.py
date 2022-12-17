#Pablo Duenas
#CS3650
#FINAL

from qiskit import *
import random

# Set up the quantum and classical registers
q = QuantumRegister(2)  # 2 qubits to represent 3 choices (rock, paper, scissors)
c = ClassicalRegister(2)

# Set up the quantum circuit
qc = QuantumCircuit(q, c)

# Create a quantum superposition of all possible choices
qc.h(q[0])
qc.h(q[1])

# Add a measure gate to the qubits
qc.measure(q, c)

# Execute the quantum circuit on a simulator
provider = IBMQ.get_provider('ibm-q')
backend = provider.get_backend('ibmq_quito')
job = execute(qc, backend)
result = job.result()

# Get the measurement result
measurement = int(list(result.get_counts().keys())[0], 2)

# Map the measurement result to a choice (rock, paper, scissors)
choices = ["rock", "paper", "scissors"]
choice = choices[measurement]

# Generate the computer's choice
computer_choice = random.choice(choices)

# Determine the winner
if choice == computer_choice:
    print("It's a tie!")
elif (choice == "rock" and computer_choice == "scissors") or (choice == "scissors" and computer_choice == "paper") or (choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("You lose...")

print("You chose", choice)
print("The computer chose", computer_choice)
