# Copilot: Decisiones Tomadas — k-mer Counter

## ✔️ Sugerencias aceptadas

- **Uso de `argparse` con argumento posicional y opción `-k/--kmer_size`**  
  Copilot sugirió una estructura estándar de parser. Coincidía con las buenas prácticas y con lo pedido por la práctica.

- **Uso del patrón `kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1`**  
  Sugerencia correcta, clara y alineada con el objetivo de practicar diccionarios sin depender de librerías externas.

- **Normalización de la secuencia (`upper()`, remover espacios y saltos de línea)**  
  Copilot acertó en sugerir limpieza antes del análisis. Se aceptó porque forma parte de una validación básica esperada.

## ❌ Sugerencias rechazadas

- **Leer la secuencia desde un archivo FASTA**  
  Copilot asumió que se debía leer un archivo, pero la práctica pide explícitamente “una secuencia desde la línea de comandos”. Se rechazó.

- **Ordenar los resultados alfabéticamente antes de imprimir**  
  No es parte del objetivo y Copilot lo sugería automáticamente. Se rechazó para mantener la salida simple y directa.

## ⭐ Parte más difícil

La parte más compleja fue definir validación robusta sin detener el programa innecesariamente.  
Copilot a veces proponía abortar por cualquier carácter inválido, o limpiar demasiado la secuencia.  
Ajustar ese comportamiento a lo que la práctica realmente pedía requirió mucho tweaking.