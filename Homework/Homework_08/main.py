import UI
import logger as lg
import adding as add


lg.logging.info('Start')
add.init_data_base('employees_base.csv')
UI.ls_menu()
