import UI
import logger as lg
import adding as add


lg.logging.info('Start')
add.init_data_base('base_phone.csv')
UI.ls_menu()
