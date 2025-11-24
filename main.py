# ============================================================
# Archivo: main.py
# Objetivo: Aplicación Flask con menú principal y los dos ejercicios
#           - Ejercicio 1: Cálculo de compras con descuentos por edad
#           - Ejercicio 2: Login con usuarios predefinidos
# Estructura: templates/ (HTML) y static/ (CSS)
# ============================================================

from flask import Flask, render_template, request

app = Flask(__name__)

# ------------------------------
# Página principal (menú)
# ------------------------------
@app.route('/')
def index():
    # Muestra dos botones: Ejercicio 1 y Ejercicio 2
    return render_template('index.html')

# ------------------------------
# Ejercicio 1: Cálculo de compras
# ------------------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Captura de datos del formulario
        nombre = request.form.get('nombre', '').strip()
        edad_str = request.form.get('edad', '0').strip()
        cantidad_str = request.form.get('cantidad', '0').strip()

        # Validaciones básicas de entrada de datos
        try:
            edad = int(edad_str)
            cantidad = int(cantidad_str)
        except ValueError:
            # Si hay valores no numéricos, retornamos con mensaje de error
            return render_template('resultado1.html',
                                   nombre=nombre or '(sin nombre)',
                                   total=0,
                                   descuento=0,
                                   total_final=0,
                                   error='Edad y cantidad deben ser números enteros.')

        # reglas de negocio del ejercicio
        precio_unitario = 9000
        total = cantidad * precio_unitario

        if edad < 18:
            descuento = 0
        elif edad <= 30:
            descuento = total * 0.15
        else:
            descuento = total * 0.25

        total_final = total - descuento

        # Renderiza la vista de resultados
        return render_template('resultado1.html',
                               nombre=nombre,
                               total=total,
                               descuento=descuento,
                               total_final=total_final,
                               error=None)
    # Renderiza el formulario
    return render_template('ejercicio1.html')

# ------------------------------
# Ejercicio 2: Login con usuarios predefinidos
# ------------------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip().lower()
        clave = request.form.get('clave', '').strip()

        # Usuarios predefinidos
        users = {
            'juan': 'admin',
            'pepe': 'user'
        }

        # Validación de las credenciales
        if usuario in users and clave == users[usuario]:
            if usuario == 'juan':
                mensaje = f'Bienvenido Administrador {usuario}'
            else:
                mensaje = f'Bienvenido Usuario {usuario}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

        return render_template('resultado2.html', mensaje=mensaje)

    # Renderiza el formulario de login
    return render_template('ejercicio2.html')

# ------------------------------
# Inicia la aplicación
# ------------------------------
if __name__ == '__main__':
    # Ejecuta en modo desarrollo en localhost:5000
    app.run(host='127.0.0.1', port=5000, debug=True)
