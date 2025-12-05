"""
gene-expression.py

Lee una secuencia desde la línea de comandos y cuenta la frecuencia de cada k-mer.

Uso:
    python src/k-mers.py ATGCGAT --kmer_size 3

"""

import argparse
import sys

def validar_secuencia(seq: str) -> str:
    """
    Valida que la secuencia contenga únicamente A, T, G, C.
    Convierte a mayúsculas y elimina saltos de línea o espacios.
    """
    seq = seq.replace("\n", "").replace(" ", "").upper()

    bases_validas = {"A", "T", "G", "C"}
    seq_limpia = []

    for base in seq:
        if base in bases_validas:
            seq_limpia.append(base)
        else:
            print(f"Aviso: carácter inválido '{base}' ignorado.", file=sys.stderr)

    if len(seq_limpia) == 0:
        print("Error: la secuencia no contiene bases válidas (A, T, G, C).", file=sys.stderr)
        sys.exit(1)

    return "".join(seq_limpia)


def contar_kmers(seq: str, k: int) -> dict:
    """
    Devuelve un diccionario con la cuenta de todos los k-mers contiguos.
    """
    if k <= 0:
        print("Error: k debe ser un entero positivo.", file=sys.stderr)
        sys.exit(1)

    if k > len(seq):
        print("Error: k es mayor que la longitud de la secuencia.", file=sys.stderr)
        sys.exit(1)

    conteos = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i : i + k]
        conteos[kmer] = conteos.get(kmer, 0) + 1

    return conteos

def construir_argumentos():
    parser = argparse.ArgumentParser(
        description="Cuenta los k-mers contiguos de una secuencia de ADN."
    )

    parser.add_argument(
        "secuencia",
        help="Secuencia de ADN (solo A, T, G, C)."
    )

    parser.add_argument(
        "-k", "--kmer_size",
        type=int,
        default=2,
        help="Longitud del k-mer (por defecto: 2)."
    )

    return parser.parse_args()


def main():
    args = construir_argumentos()
    sec = validar_secuencia(args.secuencia)
    k = args.kmer_size

    conteos = contar_kmers(sec, k)

    # imprimir en formato requerido: kmer<TAB>conteo
    for kmer, count in conteos.items():
        print(f"{kmer}\t{count}")


if __name__ == "__main__":
    main()