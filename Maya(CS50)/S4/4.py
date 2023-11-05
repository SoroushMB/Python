import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.dragon(f"Hello, {sys.argv[1]}")