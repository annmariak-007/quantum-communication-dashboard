from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_entanglement():
    qc = QuantumCircuit(2,2)
    qc.h(0)
    qc.cx(0,1)
    qc.measure([0,1],[0,1])
    return qc
def run_entanglement(qc):
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1024).result()
    return result.get_counts()

def save_histogram(counts):
    plot_histogram(counts)
    plt.savefig("outputs/entanglement_histogram.png")
    plt.close()

if __name__ == "__main__":
    # 1. Create the circuit
    entanglement_circuit = create_entanglement()
    
    # 2. Run the simulation
    counts = run_entanglement(entanglement_circuit)
    
    # 3. Print the counts to the terminal
    print("Entanglement circuit measurement counts:")
    print(counts)
    
    # 4. Save the histogram
    save_histogram(counts)
    print("Histogram saved to outputs/entanglement_histogram.png")