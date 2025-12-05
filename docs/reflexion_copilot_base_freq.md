# Reflexión sobre el uso de Copilot en `base_freq.py`

Durante el desarrollo del script, Copilot ofreció varias sugerencias útiles, pero también generó propuestas que tuve que descartar.

## ✔️ Sugerencias aceptadas
- Separar la lógica en funciones más pequeñas (`validate_file`, `extract_first_sequence`, `clean_sequence`, etc.).
- Agregar docstrings detallados para mejorar la claridad del programa.
- Utilizar un diccionario para almacenar frecuencias y porcentajes.
- Implementar `argparse` con una función `build_parser()` dedicada.

Estas sugerencias mejoraron la organización y legibilidad general del código.

## ❌ Sugerencias rechazadas
- Crear clases innecesarias para un script pequeño (por ejemplo, una clase `FastaParser`).
- Usar expresiones regulares complejas para validar FASTA, lo cual era excesivo para este caso.
- Intentar procesar múltiples secuencias FASTA cuando el requerimiento pedía **una sola**.

Se rechazaron porque aumentaban la complejidad sin aportar valor al objetivo del ejercicio.

## 💀 Parte más difícil
La parte más dificl fue reorganizar el código manteniendolo igualito con el mismo comportamiento original pero con buenas prácticas. Dividir la validación y el procesamiento sin romper la forma en que el script manejaba sus errores lo tuve que hacer con mucho cuidado para no alterar la lógica original.