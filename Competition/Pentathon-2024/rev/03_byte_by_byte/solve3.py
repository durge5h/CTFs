import angr
import re 

project = angr.Project("./condition", auto_load_libs=False)

@project.hook(0x401584)  # Target address
def print_flag(state):
    print("VALID INPUT:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()


