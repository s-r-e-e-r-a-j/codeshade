# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from pathlib import Path
import base64, shutil
from .core import run_cmd, write_text, read_text, C

BASH_CMD = "bash-obfuscate"

def install_bash_obfuscate(auto: bool = False) -> None:
    if not shutil.which("npm"):
        print(C.yellow + "npm not found" + C.reset)
        return
    if not auto:
        ans = input("Install bash-obfuscate now? (y/N): ").strip().lower()
        if ans != "y":
            return
    run_cmd(["npm", "install", "-g", "bash-obfuscate"], check=True)
    print(C.green + "Installed" + C.reset)

def obf_bash(src: Path, dst: Path, auto_install: bool = False) -> None:
    if not shutil.which(BASH_CMD):
        print(C.yellow + "bash-obfuscate not found" + C.reset)
        if auto_install:
            install_bash_obfuscate(True)
    if not shutil.which(BASH_CMD):
        raise RuntimeError("bash-obfuscate missing")
    run_cmd([BASH_CMD, str(src), "-o", str(dst)], check=True)
    print(C.green + "Bash obfuscated -> " + str(dst) + C.reset)
