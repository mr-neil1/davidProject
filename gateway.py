import serial
import time
from flask import Flask, jsonify

app = Flask(__name__)

# --- CONFIGURATION ARDUINO ---
# Remplacez 'COM3' (Windows) ou '/dev/ttyACM0' (Linux/Mac) par votre port
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Pause pour laisser l'Arduino redémarrer
    print(f"Connecté à l'Arduino sur {SERIAL_PORT}")
except Exception as e:
    print(f"Erreur de connexion série : {e}")
    ser = None

@app.route('/raw-data')
def get_raw_data():
    if ser and ser.is_open:
        try:
            # On vide le tampon pour avoir la donnée la plus fraîche
            ser.reset_input_buffer() 
            line = ser.readline().decode('utf-8').strip()
            
            if line:
                return jsonify({"status": "success", "value": line})
            return jsonify({"status": "empty", "value": "Pas de données"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    return jsonify({"status": "offline", "value": "Arduino non trouvé"}), 503

if __name__ == '__main__':
    # On lance Flask sur le port 5001 pour ne pas entrer en conflit avec Django (8000)
    app.run(host='0.0.0.0', port=5001, debug=True)