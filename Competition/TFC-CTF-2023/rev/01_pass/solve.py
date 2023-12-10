import angr
import re 

project = angr.Project("./pass", auto_load_libs=False)

@project.hook(0x4019b3)  # Target address
def print_flag(state):
    print("VALID INPUT:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()


