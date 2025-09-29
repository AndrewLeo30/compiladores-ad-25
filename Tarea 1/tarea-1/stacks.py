def main():
    stack = []
    stack_modificado = push_modificaciones(stack)
    mostrar_historial_con_formato(stack_modificado)
    peek_modificacion_reciente(stack_modificado)
    print("======================================================================")

    print("Haciendo un par de modificaciones...")
    stack_modificado.append("Modificación: 4:49 pm")
    stack_modificado.append("Modificación: 4:50 pm")
    mostrar_historial_con_formato(stack_modificado)
    print("======================================================================")

    pop_modificacion_reciente(stack_modificado)
    mostrar_historial_con_formato(stack_modificado)
    peek_modificacion_reciente(stack_modificado)

def push_modificaciones(historial):
    for i in range(2, 9, 2):
        historial.append(f"Modificación: 4:4{i} pm")
    return historial

def mostrar_historial_con_formato(historial):
    historial_con_formato = historial.copy()
    historial_con_formato.reverse()
    print(f"Historial de modificaciones más recientes: \n{("\n".join(historial_con_formato))}")

def peek_modificacion_reciente(historial):
    print(f"Modificación más reciente ({historial[-1]})")

def pop_modificacion_reciente(historial):
    print(f"Descartando la modificación más reciente ({historial.pop()})...")

main()
