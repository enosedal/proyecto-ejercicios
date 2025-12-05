"""
rps.py

Es un juego de piedra, papel o tijeras contra la CPU.

Uso:
    python src/rps.py

"""

import random
from typing import Tuple

VALID_CHOICES = ["rock", "paper", "scissors"]
WIN_EMOJIS = " 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉"

def determine_result(user: str, cpu: str) -> str:
    """
    Determina el resultado del enfrentamiento entre user y cpu.

    Retorna:
      - "win"  - si el usuario gana
      - "lose" - si el usuario pierde
      - "draw" - si hay empate
    """
    if user == cpu:
        return "draw"

    # Reglas: rock > scissors, scissors > paper, paper > rock
    wins_against = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if wins_against[user] == cpu:
        return "win"
    return "lose"

def play(user_choice: str) -> Tuple[str, str]:
    """
    Ejecuta una ronda (sin pedir input). Valida user_choice,
    selecciona la jugada de la CPU y devuelve (cpu_choice, resultado).

    Lanza ValueError si user_choice no es válido.
    """
    user = user_choice.strip().lower()
    if user not in VALID_CHOICES:
        raise ValueError(f"Entrada inválida: '{user_choice}'. Opciones válidas: {', '.join(VALID_CHOICES)}")

    cpu_choice = random.choice(VALID_CHOICES)
    result = determine_result(user, cpu_choice)
    return cpu_choice, result

def main() -> None:
    """
    Bucle principal que solicita input al usuario hasta que pulse ENTER.
    """
    print("Rock, Paper, Scissors")
    print("Escribe rock, paper o scissors.")
    print("Presiona ENTER sin escribir nada para salir.")
    print("-" * 40)

    while True:
        try:
            user_input = input("Tu elección: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo. ¡Hasta la próxima!")
            break

        if user_input == "":
            print("Juego terminado. ¡Hasta la vista!")
            break

        try:
            cpu_choice, outcome = play(user_input)
        except ValueError as e:
            print(e)
            continue

        print(f"CPU: {cpu_choice}")
        print(f"Resultado: {outcome}")

        if outcome == "win":
            print(f"¡Gansaste!{WIN_EMOJIS}")

        print("-" * 40)

if __name__ == "__main__":
    main()