# Name: Pablo Duenas
# Date: December 16, 2022
# Description: Rock Paper Scissors game between the user (computer) and IBM's Quantum Computer

from qiskit import *
import random

# Authenticate account
IBMQ.save_account('f0cf7a50880171732b0346bd1c616f6e7aa33f7b7ebaa402dbf9f39804984179868fb1237ef0dbb54f884eb4a58c4b736c68c2c115c06b27a2a6149e26912f7b', overwrite=True)
IBMQ.load_account()

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

# Select the provider matching your hub, group, and project
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')

# Select the backend to execute the quantum circuit
backend = provider.get_backend('ibmq_quito')

# Execute the quantum circuit on the selected backend
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

