# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from pathlib import Path
import base64
from .core import read_text, read_bytes, write_text, C

EMOJI = ["😀","😃","😄","😁","😅","🤣","😂","😉","😊","😍"]
CHUNK = 64

def to_base64(src: Path, dst: Path, var: str = "payload") -> None:
    if not var or not (var[0].isalpha() or var[0] == "_"):
        raise ValueError("invalid var name")
    data = read_text(src)
    b64 = base64.b64encode(data.encode()).decode()
    lines: list[str] = [f"{var}=''"]
    for i in range(0, len(b64), CHUNK):
        seg = b64[i:i+CHUNK]
        esc = ''.join(f"\\x{ord(c):02x}" for c in seg)
        lines.append(f"{var}+='{esc}'")
    lines.append("import base64")
    lines.append(f"exec(base64.b64decode({var}.encode()).decode())")
    write_text(dst, "\n".join(lines))
    print(C.green + "Obfuscated to base64 -> " + str(dst) + C.reset)

def to_emoji(src: Path, dst: Path) -> None:
    if len(EMOJI) < 10:
        raise RuntimeError("emoji list too small")
    digit_map = {str(i): EMOJI[i] for i in range(10)}
    rev_map = {v: k for k, v in digit_map.items()}
    data = read_bytes(src)
    if not data:
        raise RuntimeError("empty source")
    tokens: list[str] = []
    for b in data:
        s = f"{b:03d}"
        token = " ".join(digit_map[d] for d in s)
        tokens.append(token)
    big = "  ".join(tokens)
    gen: list[str] = []
    gen.append(f"emoji_map = {rev_map!r}")
    gen.append(f"data = '''{big}'''")
    gen.append("parts = []")
    gen.append("for token in data.split('  '):")
    gen.append("    digits = ''.join(emoji_map.get(ch, '') for ch in token.split())")
    gen.append("    if digits and len(digits) == 3:")
    gen.append("        parts.append(int(digits))")
    gen.append("payload = bytes(parts).decode('utf-8')")
    gen.append("exec(payload)")
    write_text(dst, "\n".join(gen))
    print(C.green + "Obfuscated to emoji -> " + str(dst) + C.reset)
