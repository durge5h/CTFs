import angr
import re 

project = angr.Project("./chall", auto_load_libs=False)

@project.hook(0x401467)  # Target address
def print_flag(state):
    print("VALID INPUT:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()

