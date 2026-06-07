"""Script principal para ejecutar tareas simples del proyecto."""

import sys


def main(argv=None):
    argv = argv or sys.argv[1:]
    print("GCI-World-2026-competition — estructura inicial")
    if argv:
        print("Argumentos:", argv)


if __name__ == "__main__":
    main()
