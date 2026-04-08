# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from pathlib import Path
import subprocess

class C:
    reset = "\033[0m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[0;34m"
    cyan = "\033[0;36m"
    purple = "\033[0;35m"

def read_text(p: Path) -> str:
    if not p.exists():
        raise FileNotFoundError(str(p))
    return p.read_text(encoding="utf-8", errors="ignore")

def read_bytes(p: Path) -> bytes:
    if not p.exists():
        raise FileNotFoundError(str(p))
    return p.read_bytes()

def write_text(p: Path, data: str) -> None:
    p.write_text(data, encoding="utf-8")

def run_cmd(cmd: list[str], capture: bool=False, check: bool=True):
    if not cmd:
        raise RuntimeError("empty command")
    return subprocess.run(cmd, capture_output=capture, text=True, check=check)
