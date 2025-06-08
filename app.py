from flask import Flask , render_template, jsonify, abort
import csv
import pandas as pd

app = Flask(__name__) 

def cargar_datos():
    productos = []
    with open('productos.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for idx, fila in enumerate(lector, start=1):
            print(fila)
            productos.append({
                'id': idx,
                'nombre': fila['nombre_producto'], 
                'precio': float(fila['precio'])
            })
    return productos

@app.route('/')
def index():
    productos = cargar_datos()
    return render_template('productos.html', productos=productos)

@app.route('/productos')
def productos_api():
    return jsonify(cargar_datos())


@app.route('/productos/<int:productos_id>')
def detalle_producto(productos_id):
    productos = cargar_datos()
    producto = next((p for p in productos if p['id'] == productos_id), None)
    if not producto:
        abort(404)
    return render_template('detallep.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)
