# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from pathlib import Path
import sys
import argparse

from .core import read_text, read_bytes, write_text, run_cmd, C
from .python_obf import to_base64, to_emoji
from .bash_obf import obf_bash
from .menu import menu

def main() -> None:
    p = argparse.ArgumentParser(prog="CodeShade")
    sub = p.add_subparsers(dest="cmd")
    a1 = sub.add_parser("py-base64")
    a1.add_argument("src", type=Path)
    a1.add_argument("dst", type=Path)
    a1.add_argument("--var", type=str, default="payload")

    a2 = sub.add_parser("py-emoji")
    a2.add_argument("src", type=Path)
    a2.add_argument("dst", type=Path)

    a3 = sub.add_parser("bash-obf")
    a3.add_argument("src", type=Path)
    a3.add_argument("dst", type=Path)
    a3.add_argument("--auto-install", action="store_true")

    p.add_argument("--interactive", action="store_true")

    args = p.parse_args()

    if len(sys.argv) == 1 or args.interactive or args.cmd is None:
        menu()
        return

    try:
        if args.cmd == "py-base64":
            to_base64(args.src, args.dst, args.var)
        elif args.cmd == "py-emoji":
            to_emoji(args.src, args.dst)
        elif args.cmd == "bash-obf":
            obf_bash(args.src, args.dst, auto_install=args.auto_install)
        else:
            print(C.red + "Unknown command" + C.reset)
    except Exception as e:
        print(C.red + "Error: " + str(e) + C.reset)

if __name__ == "__main__":
    main()
