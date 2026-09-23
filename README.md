# quantum-communication-dashboard
A real-time interactive web application built with Python, Flask, and Qiskit that demonstrates core quantum communication concepts including Bell States, Quantum Entanglement, and Quantum Teleportation.

## 🛠️ Technology Stack
* **Python 3.11**
* **Flask**
* **Qiskit**
* **NumPy**
* **Matplotlib**
* **HTML / CSS / JavaScript**

---

## 📁 Project Structure & Modules

* **`app.py` (Main Flask Application):** Handles the web server routing, renders the dashboard templates, and coordinates backend quantum simulations.
* **`quantum/` (Quantum Logic):** Contains core scripts for simulating quantum states, polarization filters, and key exchange algorithms.
* **`static/` & `templates/` (Frontend):** Stylesheets, scripts, and HTML templates that power the user interface and charts.
* **`requirements.txt` (Package List):** Lists all required Python dependencies for the project.

---

## 🚀 Getting Started & Installation

### 1. Clone the Repository
Clone this repository to your local machine using Git or download it via GitHub.

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
```
### 3. Activate the Virtual Environment
Windows:
venv\Scripts\activate

macOS / Linux:
source venv/bin/activate

### 4. Install Required Libraries
pip install -r requirements.txt

### 💻 Running the Application
Start the Flask Server:
python app.py
