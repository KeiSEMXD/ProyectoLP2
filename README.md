# Yayo Colmado

Este es un proyecto web simple para la gestión y visualización de productos de un colmado, desarrollado con **Flask** y **Bootstrap**.

## Características

- Listado de productos con tabla responsiva y diseño moderno.
- Vista de detalle para cada producto.
- Interfaz atractiva usando Bootstrap 5 y Bootstrap Icons.
- Datos cargados desde un archivo CSV.
- Navegación sencilla y footer personalizado.

## Estructura del proyecto

```
Proyecto/
│
├── app.py
├── productos.csv
├── templates/
│   ├── productos.html
│   └── detallep.html
└── static/
```

## Instalación

1. **Clona este repositorio:**

   ```sh
   git clone https://github.com/KeiSEMXD/ProyectoLP2.git
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```sh
   pip install flask pandas
   ```

4. **Asegúrate de tener el archivo `productos.csv` en la raíz del proyecto.**

## Uso

1. Ejecuta la aplicación:

   ```sh
   python app.py
   ```

2. Abre tu navegador y visita:  
   [http://localhost:5000](http://localhost:5000)

## Personalización

- Puedes modificar los estilos en los archivos HTML dentro de la carpeta `templates`.
- Para agregar o editar productos, modifica el archivo `productos.csv`.

## Capturas de pantalla

![Listado de productos](./screenshot![Screenshot 2025-06-08 113908](https://github.com/user-attachments/assets/239772e7-3224-41c2-bc11-812bcd842270)
s/listado.png)
![Detalle de producto]![Screenshot 2025-06-08 113851](https://github.com/user-attachments/assets/a2dfd5c1-e2b0-4dad-bc5d-308701ecd167)
()

## Licencia

Este proyecto es solo para fines educativos.

---

**Desarrollado por Keiter Sanchez**
