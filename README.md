# Horizonte Travel

Sitio web de viajes creado con Flask, Jinja, CSS y JavaScript.

## Ejecutar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Abrir `http://127.0.0.1:5001`.

Puedes cambiar el puerto con `PORT=5050 python main.py`.

## Rutas

- `GET /` interfaz principal
- `GET /destinos` catálogo completo
- `GET /api/destinations` lista de destinos
- `GET /api/destinations/<id>` detalle de destino
- `POST /api/contact` recibe consultas del formulario
- `GET /health` estado del servicio
