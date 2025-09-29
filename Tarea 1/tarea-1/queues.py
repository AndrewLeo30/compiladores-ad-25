from collections import deque

# Clientes en la fila
fila_clientes = deque(["Primer cliente", "Segundo cliente"])

# Más clientes llegan (enqueue)
fila_clientes.append("Tercer cliente")
fila_clientes.append("Cuarto cliente")
fila_clientes.append("Quinto cliente")

# Clientes por atender 
print(f"Clientes por atender:\n{"\n".join(list(fila_clientes))}\n")

# Los primeros dos clientes son atendidos (dequeue)
print("Clientes atendidos:")
print(fila_clientes.popleft())
print(fila_clientes.popleft())
print()

# Cliente que quedó hasta adelante en la fila
print(f"Siguiente cliente a atender: {fila_clientes[0]}")

# Clientes que faltan por atender 
print(f"Clientes que aún faltan por atender:\n{"\n".join(list(fila_clientes))}")