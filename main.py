from stack import Stack
from operation import operation as op, doCalc
from os import system
import platform

def clear():
  return system("cls") if platform.system() == 'Windows' else system("clear")

def history(h):
    for p in h:
        doCalc(p["op"], p["a"], p["b"])

def do_undo(com):
    if com == "desfazer".lower():
        if calcs.is_empty(): 
            print("Não há mais operações para desfazer.")
            return
        remade.push(calcs.pop())
        if calcs.len() > 0:
            calc = calcs.top()
            hist.append(calc)
            doCalc(calc["op"], calc["a"], calc["b"])
        
    elif com == "refazer".lower():
        if remade.is_empty():
            print("Não há operações para refazer.")
            return
        calcs.push(remade.pop())
        calc = calcs.top()
        hist.append(calc)
        doCalc(calc["op"], calc["a"], calc["b"])
    return


calcs = Stack()
remade = Stack()
hist = []

while True:
    clear()
    if calcs.is_empty() and remade.is_empty():
        print("Deseja fazer uma operação?")
    else: print("Deseja fazer outra operação?")
    print("\tPressione qualquer tecla para prosseguir...")
    print("\tDigite 'sair' para terminar.")
    option = input().lower()
    if option == "sair".lower(): break

    calcs.push(op())
    hist.append(calcs.top())

    while True:
        if calcs.is_empty():
            break
        print("=" * 50)
        print('Digite "h" para exibir o histórico: (Digite "x" para ignorar)')
        option = input().lower()
        if option == "h".lower():
            history(hist)
        print('"desfazer" ou "refazer"? (Digite "x" para ignorar)')
        option = input().lower()
        if option != "desfazer".lower() and option != "refazer".lower():
            print("", end="")
            break
        else:
            do_undo(option)

    input("\nPressione qualquer tecla para continuar...")
