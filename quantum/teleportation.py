from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_teleportation():
    qc = QuantumCircuit(3,3)
    qc.h(0)
    qc.h(1)
    qc.cx(1,2)
    qc.cx(0,1)
    qc.h(0)
    qc.measure([0,1,2],[0,1,2])
    return qc
def run_teleportation(qc):
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1024).result()
    return result.get_counts()

def save_histogram(result):
    plot_histogram(result)
    plt.savefig("outputs/teleportation_histogram.png")
    plt.close()

if __name__ == "__main__":
    # 1. Create the circuit
    teleport_circuit = create_teleportation()
    
    # 2. Run the simulation
    results = run_teleportation(teleport_circuit)
    
    # 3. Print the results to the terminal
    print("Teleportation circuit measurement counts:")
    print(results)
    #Save the histogram
    save_histogram(results)
    print("Histogram saved to outputs/teleportation_histogram.png")