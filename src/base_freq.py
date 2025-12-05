"""
base_freq.py

Calcula la frecuencias de las bases (A, T, G y C) de las secuencias de un archivo FASTA.

Uso:
    python src/base_freq.py data/sample.fasta

"""

import argparse
import os
import sys


# ============================================================
# ARGPARSE
# ============================================================

def build_parser():
    """Construye el parser para la línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Calcula la frecuencia de A, T, G y C de un archivo FASTA con una sola secuencia."
    )
    parser.add_argument("fasta", help="Archivo FASTA que contiene una sola secuencia.")
    return parser


# ============================================================
# VALIDACIONES
# ============================================================

def validate_file(path: str) -> str:
    """Valida que el archivo exista y sea legible."""
    if not os.path.exists(path):
        print(f"Error: el archivo no existe: {path}")
        sys.exit(1)

    try:
        contenido = open(path, "r", encoding="utf-8").read()
    except Exception as e:
        print("Error al leer el archivo:", e)
        sys.exit(1)

    if ">" not in contenido:
        print("Error: el archivo no parece estar en formato FASTA.")
        sys.exit(1)

    return contenido


# ============================================================
# PROCESAMIENTO FASTA
# ============================================================

def extract_first_sequence(contenido: str) -> tuple[str, str]:
    """
    Extrae el encabezado y secuencia de la primera entrada FASTA.
    Regresa: (header, secuencia)
    """
    partes = contenido.split(">")

    if len(partes) < 2:
        print("Error: FASTA vacío o sin secuencia válida.")
        sys.exit(1)

    bloque = partes[1].strip().split("\n")
    header = bloque[0]
    sec = "".join(bloque[1:]).strip().upper()

    if len(sec) == 0:
        print("Error: la secuencia está vacía.")
        sys.exit(1)

    return header, sec


def clean_sequence(seq: str) -> str:
    """Elimina caracteres inválidos, solo permite A,T,G,C."""
    bases_validas = {"A", "T", "G", "C"}
    limpia = []

    for base in seq:
        if base in bases_validas:
            limpia.append(base)
        else:
            print(f"Aviso: caracter inválido '{base}' ignorado.")

    seq_limpia = "".join(limpia)

    if len(seq_limpia) == 0:
        print("Error: la secuencia no contiene bases válidas (A,T,G,C).")
        sys.exit(1)

    return seq_limpia


# ============================================================
# CÁLCULO DE FRECUENCIAS
# ============================================================

def compute_frequencies(seq: str) -> dict:
    """Calcula frecuencias absolutas y porcentuales."""
    total = len(seq)
    freqs = {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C"),
    }
    percentages = {b: round((freqs[b] / total) * 100, 2) for b in freqs}
    return {"total": total, "freqs": freqs, "pct": percentages}


# ============================================================
# IMPRESIÓN
# ============================================================

def print_results(header: str, data: dict):
    """Imprime los resultados de manera ordenada."""
    print("Encabezado:", header)
    print("Longitud secuencia válida:", data["total"])
    print("Frecuencias:")

    for base in ["A", "T", "G", "C"]:
        f = data["freqs"][base]
        p = data["pct"][base]
        print(f"{base}: {f} ({p}%)")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = build_parser()
    args = parser.parse_args()

    contenido = validate_file(args.fasta)
    header, sec = extract_first_sequence(contenido)
    seq_limpia = clean_sequence(sec)
    resultados = compute_frequencies(seq_limpia)
    print_results(header, resultados)


if __name__ == "__main__":
    main()