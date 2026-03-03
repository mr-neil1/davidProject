# davidProject
📟 Arduino Web Dashboard (Django + Flask)
Ce projet est une interface web de monitoring en temps réel pour Arduino. Il utilise une architecture en micro-services pour séparer la gestion du matériel (Flask) de la logique applicative et de l'affichage (Django).

🏗️ Architecture du projet
Hardware (Arduino) : Lit les données analogiques et les envoie sur le port Série.

Hardware Gateway (Flask) : Un micro-service léger qui écoute le port Série et expose une API JSON.

Web Server (Django) : Le moteur principal qui récupère les données de la Gateway et les sert à l'utilisateur.

Frontend (Chart.js) : Affiche les données sous forme de graphique dynamique.

🛠️ Installation
1. Prérequis
Python 3.8+

Arduino IDE

Un câble USB pour l'Arduino

2. Configuration de l'environnement
Bash
# Cloner le projet (ou entrer dans le dossier)
cd mon_projet_firmware

# Créer et activer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
3. Flash de l'Arduino
Téléversez le code suivant (situé dans arduino/sensor.ino) sur votre carte :

C++
void setup() { Serial.begin(9600); }
void loop() {
  Serial.println(analogRead(A0));
  delay(500);
}
🚀 Démarrage
Pour faire fonctionner le système, vous devez lancer deux terminaux simultanément.

Étape 1 : Lancer la passerelle matérielle (Flask)
Vérifiez d'abord le nom de votre port série dans gateway.py (ex: COM3 ou /dev/ttyUSB0).

Bash
python gateway.py
Le service sera disponible sur : http://127.0.0.1:5001/raw-data

Étape 2 : Lancer le serveur Web (Django)
Dans un second terminal :

Bash
python manage.py runserver
L'interface sera disponible sur : http://127.0.0.1:8000

📂 Structure des fichiers
Plaintext
.
├── core/                # Configuration Django
├── dashboard/           # App Django (Logique & Templates)
│   ├── templates/       # Interface HTML/JavaScript
│   └── views.py         # Consomme l'API Flask
├── gateway.py           # Micro-service Flask (Liaison Série)
├── manage.py            # Gestionnaire Django
└── requirements.txt     # Dépendances Python
📈 Flux de données
L'Arduino écrit sur le port Serial.

Flask lit le port Serial via pyserial.

Le Navigateur appelle l'URL /api/sensor/ de Django.

Django utilise requests pour appeler Flask sur le port 5001.

Django renvoie la valeur finale au Navigateur.

Chart.js met à jour le graphique.

📝 Notes importantes
Sécurité : Flask est configuré en mode debug=True pour le développement. Pour une utilisation réelle, passez-le en mode production.

Port Série : Si le script Flask crash au démarrage, vérifiez qu'aucun autre logiciel (comme le moniteur série d'Arduino IDE) n'utilise le port USB.
