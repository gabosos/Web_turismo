from datetime import datetime, timezone

from flask import Flask, jsonify, render_template, request, send_from_directory

app = Flask(__name__)

DESTINATIONS = [
    {
        "id": "japon",
        "name": "Japón",
        "region": "Asia",
        "description": "Templos milenarios, jardines zen y la energía creativa de Tokio.",
        "price": 2500,
        "duration": "10 días",
        "image": "pagoda-fondo-rosa-cielo-rosa-nieve-el_542777-176.avif",
    },
    {
        "id": "islandia",
        "name": "Islandia",
        "region": "Europa",
        "description": "Auroras boreales, géiseres y paisajes volcánicos en la tierra del hielo.",
        "price": 3200,
        "duration": "8 días",
        "image": "photo-1476610182048-b716b8518aae.avif",
    },
    {
        "id": "kenia",
        "name": "Kenia",
        "region": "África",
        "description": "Safaris inolvidables, la Gran Migración y culturas ancestrales.",
        "price": 2800,
        "duration": "9 días",
        "image": "aerial-views-cape-town-south-africa-video-may-10-2021.webp",
    },
]

CONTACT_REQUESTS = []


@app.get("/")
def home():
    return render_template("index.html", destinations=DESTINATIONS)


@app.get("/media/<path:filename>")
def media(filename):
    return send_from_directory("Image", filename)


@app.get("/destinos")
def destinations_page():
    return render_template("destinations.html", destinations=DESTINATIONS)


@app.get("/api/destinations")
def destinations_api():
    return jsonify({"data": DESTINATIONS, "count": len(DESTINATIONS)})


@app.get("/api/destinations/<destination_id>")
def destination_api(destination_id):
    destination = next((item for item in DESTINATIONS if item["id"] == destination_id), None)
    if destination is None:
        return jsonify({"error": "Destino no encontrado"}), 404
    return jsonify({"data": destination})


@app.post("/api/contact")
def contact_api():
    payload = request.get_json(silent=True) or request.form
    required_fields = ("name", "email", "message")
    missing_fields = [field for field in required_fields if not str(payload.get(field, "")).strip()]
    if missing_fields:
        return jsonify({"error": "Completa los campos obligatorios", "fields": missing_fields}), 400

    contact_request = {
        "name": str(payload["name"]).strip(),
        "email": str(payload["email"]).strip(),
        "destination": str(payload.get("destination", "")).strip(),
        "message": str(payload["message"]).strip(),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    CONTACT_REQUESTS.append(contact_request)
    return jsonify({"message": "Solicitud recibida. Te contactaremos pronto.", "data": contact_request}), 201


@app.get("/health")
def health_check():
    return jsonify({"status": "ok", "service": "horizonte-travel"})
