import global_variables_module
import updater

updater.update_global_variable()
print(global_variables_module.global_variable)  # the global variable is indeed updated by the updater module
