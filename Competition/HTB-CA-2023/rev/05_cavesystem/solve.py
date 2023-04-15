import angr

project = angr.Project("./cave", auto_load_libs=False)

@project.hook(0x401aba)  # Target address
def print_flag(state):
    print("VALID INPUT:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()
