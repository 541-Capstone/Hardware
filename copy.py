import pathlib
import shutil



# from rich import pretty
# from rich import inspect
# pretty.install()


dev_root = pathlib.Path.cwd()
dev_code = dev_root / "code.py"



run_root = pathlib.Path('F:/')
run_code = run_root / "code.py"


shutil.copy(dev_code, run_code)