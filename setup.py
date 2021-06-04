import cx_Freeze


executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Race and Crash",
    options={"Build_exe": {"packages": ["pygame"],
                           "include_files": ["plane.png"]}},
    executables=executables
)
