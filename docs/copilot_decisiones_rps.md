# Reflexión sobre uso de Copilot — rps.py

## Sugerencias aceptadas
- **Estructura básica de la función `determine_result()`**:  
  Copilot propuso primero un diccionario `wins_against` para mapear qué le gana a qué. Acepté esa idea porque es clara, elegante y fácil de mantener.
- **Uso de `.strip().lower()` en la entrada del usuario**:  
  Esto ayuda a prevenir errores por espacios o mayúsculas. Fue razonable y lo mantuve.
- **Separar la lógica en una función `play()`**:  
  Copilot sugirió encapsular la validación, elección CPU y resultado en una sola función. Lo acepté porque mejora la modularidad del programa.

## Sugerencias rechazadas
- **Copilot intentó agregar menús complejos y loops adicionales**:  
  Algunas sugerencias incluían funciones extra como “mostrar menú”, “jugar varias rondas con puntaje”, etc. Las rechacé porque el ejercicio exige un programa simple, no un sistema completo.
- **Mensajes de error demasiado verbosos o decorados con emojis aleatorios**:  
  Rechazados para mantener claridad y consistencia.

## Parte más difícil
La parte más complicada fue evitar que Copilot tratara de overengineer el programa.  
El ejercicio pedía lógica simple basada en `if/elif`, pero Copilot insistía en versiones más avanzadas. La dificultad fue mantener el código accesible, limpio y didáctico sin perder funcionalidad.