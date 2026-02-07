from auth_system import login_menu
from xprimer_tools import main_menu

def on_login_success(token):
    main_menu(token)

if __name__ == "__main__":
    login_menu(on_login_success)