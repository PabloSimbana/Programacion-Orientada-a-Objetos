import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código del módulo futbolístico: {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("⚠️ El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"❌ Error al ejecutar el módulo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    ligas = {
        '1': 'Liga_Ecuatoriana',
        '2': 'Liga_Europea',
        '3': 'Mundial'
    }

    while True:
        print("\n⚽ MENU PRINCIPAL - DASHBOARD FUTBOLERO ⚽")
        for key in ligas:
            print(f"{key} - {ligas[key]}")
        print("0 - Salir")

        eleccion_liga = input("Elige una liga o '0' para salir: ")
        if eleccion_liga == '0':
            print("👋 Saliendo del dashboard futbolero.")
            break
        elif eleccion_liga in ligas:
            mostrar_sub_menu(os.path.join(ruta_base, ligas[eleccion_liga]))
        else:
            print("❌ Opción no válida.")

def mostrar_sub_menu(ruta_liga):
    if not os.path.exists(ruta_liga):
        print("⚠️ La liga no tiene carpetas aún.")
        return

    equipos = [f.name for f in os.scandir(ruta_liga) if f.is_dir()]

    while True:
        print("\n🏟️ SUBMENÚ - Selecciona un equipo")
        for i, equipo in enumerate(equipos, start=1):
            print(f"{i} - {equipo}")
        print("0 - Regresar al menú principal")

        eleccion_equipo = input("Elige un equipo o '0' para regresar: ")
        if eleccion_equipo == '0':
            break
        else:
            try:
                eleccion_equipo = int(eleccion_equipo) - 1
                if 0 <= eleccion_equipo < len(equipos):
                    mostrar_scripts(os.path.join(ruta_liga, equipos[eleccion_equipo]))
                else:
                    print("❌ Opción no válida.")
            except ValueError:
                print("❌ Ingresa un número válido.")

def mostrar_scripts(ruta_equipo):
    scripts = [f.name for f in os.scandir(ruta_equipo) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n📊 MÓDULOS DE FÚTBOL - Selecciona una opción")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al menú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un módulo, '0' para regresar o '9' para menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_equipo, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)

                    if codigo:
                        ejecutar = input("⚽ ¿Ejecutar módulo? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("📋 Módulo no ejecutado.")
                        else:
                            print("❌ Opción inválida.")

                        input("\nPresiona Enter para continuar...")
                else:
                    print("❌ Opción inválida.")
            except ValueError:
                print("❌ Ingresa un número válido.")

if __name__ == "__main__":
    mostrar_menu()
