from utils import sector_utils
from utils import user_utils
import textwrap

def presentation():
    print("""
    Interastrum
    v1.0.0

    Bienvenido a Interastrum, un juego de exploración espacial en tu terminal.

    Q/1: Iniciar nueva partida
    W/2: Ajustes
    E/3: Novedades
    A/4: Como jugar
    S/5: Creditos
    D/6: Salir
    """)

def start_new_game():
    print("Iniciando nueva partida...")
    # Lógica de iniciar partida aquí

def open_settings():
    print("Ajustes… próximamente.")

def show_news():
    print("""
    Esta es la primera versión de Interastrum. Ve a Ayuda para entender cómo jugar.
    """)

def show_help():
    print(textwrap.dedent("""
    Interastrum es un juego de exploración espacial en terminal donde tomas el control de una nave con recursos limitados...
    """))

def show_credits():
    print("Créditos… próximamente.")

def exit_game():
    print("Saliendo del juego")
    exit()

def user_choice():
    actions = {
        'q': start_new_game, '1': start_new_game,
        'w': open_settings, '2': open_settings,
        'e': show_news, '3': show_news,
        'a': show_help, '4': show_help,
        's': show_credits, '5': show_credits,
        'd': exit_game, '6': exit_game
    }

    while True:
        choice = input("Acción: ").strip().lower()
        action = actions.get(choice)
        if action:
            action()
            if action == exit_game:
                break
        else:
            print("Opción no reconocida.\n")
            presentation()

def main():
    presentation()
    user_choice()

if __name__ == "__main__":
    main()
