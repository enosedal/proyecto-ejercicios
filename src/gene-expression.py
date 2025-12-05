"""
gene-expression.py

Imprime una lista de genes ordenados alfabéticamente mayores en expresión a un umbral dado, ambos leídos de un archivo TSV

Uso:
    python src/gene-expression.py data/condA.tsv -t 10

"""

import argparse
import pandas as pd


def load_expression_table(path: str) -> pd.DataFrame:
    """
    Carga un archivo TSV con columnas 'gene' y 'expression'.

    Args:
        path (str): Ruta al archivo TSV.

    Returns:
        DataFrame: DataFrame limpio y validado.
    """

    df = pd.read_csv(path, sep="\t")

    # Validar columnas obligatorias
    if "gene" not in df.columns or "expression" not in df.columns:
        raise ValueError("El archivo debe tener columnas 'gene' y 'expression'.")

    # Conversión a numérico, errores - NaN
    df["expression"] = pd.to_numeric(df["expression"], errors="coerce")

    # Eliminar filas inválidas
    df = df.dropna(subset=["expression"])

    return df


def filter_genes(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Filtra genes cuya expresión sea >= threshold.

    Args:
        df: DataFrame con columnas 'gene' y 'expression'
        threshold (float): Umbral mínimo

    Returns:
        DataFrame: Genes filtrados y ordenados
    """

    filtered = df[df["expression"] >= threshold]

    # Ordenar alfabéticamente
    return filtered.sort_values("gene")


def build_parser() -> argparse.ArgumentParser:
    """
    Construye el parser de argumentos.

    Returns:
        ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description="Filtra genes por expresión usando un archivo TSV y pandas."
    )

    parser.add_argument(
        "file",
        help="Archivo TSV con columnas 'gene' y 'expression'."
    )

    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=0.0,
        help="Umbral mínimo de expresión (ej. 10.5)."
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    df = load_expression_table(args.file)

    threshold = args.threshold

    filtered = filter_genes(df, threshold)

    if filtered.empty:
        print("No se encontraron genes por encima del threshold.")
        return

    print("Genes filtrados:")
    for gene in filtered["gene"].tolist():
        print(gene)


if __name__ == "__main__":
    main()