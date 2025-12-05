# Copilot: Decisiones para el script de expresión génica

A continuación se documentan las decisiones basadas en las sugerencias de Copilot durante la creación del script de análisis de expresión génica.

## Sugerencias aceptadas

* **Uso de `pandas` para cargar y manipular los datos**: Correcta porque es la herramienta estándar para análisis de datos tabulares y simplifica mucho el manejo del archivo CSV.
* **Validar la existencia del archivo de entrada** antes de procesarlo: Correcto porque evita errores en tiempo de ejecución y mejora la robustez del script.
* **Agregar manejo de argumentos con `argparse`**: Correcto porque permite que el script sea más flexible y usable desde la línea de comandos.
* **Verificar que las columnas esperadas existan**: Correcto para evitar fallos si el archivo tiene un formato inesperado.

## Sugerencias rechazadas

* **Hacer gráficos directamente dentro del script**: Rechazada porque no es parte de los requisitos del ejercicio y agregaría dependencias innecesarias.
* **Convertir automáticamente valores no numéricos a cero**: Incorrecto porque eso puede ocultar errores en los datos y producir resultados engañosos.
* **Escribir resultados en múltiples archivos separados**: Rechazada por exceso de complejidad; un solo archivo de salida era suficiente.

## Por qué me parecieron correctas o incorrectas

* Las sugerencias aceptadas mejoran la legibilidad y claridad del script, y siguen buenas prácticas del curso.
* Las rechazadas eran ambiguas, complejas y dificl de prededcir para el procesamiento de los datos.
* Queríamos flujo limpio, validado y transparente, evitando cualquier cosa que afectara la calidad del análisis.