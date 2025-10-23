from os import system
system("cls")

jogadores = ["Kenneth", "Mattos", "Pestana", "Rafaela", "Caetano", "Mariana"]
print(f"Time completo: {jogadores}")
titulares = jogadores[:3]
reservas = jogadores[3:]
print(f"Time titular: {titulares}")
print(f"Time reserva: {reservas}")