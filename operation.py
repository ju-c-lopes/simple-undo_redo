def operation():
    while True:
        print("Escolha um número entre as opções:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão\n")
        try:        
            op = input("Digite sua escolha: ")
            while int(op) < 1 or int(op) > 4:
                print("\nOpção inválida\n" + ("=" * 50))
                op = input("Digite sua escolha: ")
        except ValueError:
            print("\nA entrada deve ser apenas numero.\n")
            continue
        print("Digite os números:\n")
        return doCalc(int(op))

def doCalc(op, a=None, b=None):
    if op == 1 and a is None and b is None:
        #soma
        while True:
            try:
                a = int(input())
                print(f"{a} + ", end="")
                b = int(input())
            except ValueError:
                print("\nA entrada deve ser apenas número.\n")
                continue
            print(f"{a} + {b} = {a + b}")
            return {
                "op": op,
                "a": a,
                "b": b,
            }
    elif op == 1:
        print(f"{a} + {b} = {a + b}")
        return {
            "op": op,
            "a": a,
            "b": b,
        }


    if op == 2 and a is None and b is None:
        # subtracao
        while True:
            try:
                a = int(input())
                print(f"{a} - ", end="")
                b = int(input())
            except ValueError:
                print("\nA entrada deve ser apenas número.\n")
                continue
            print(f"{a} - {b} = {a - b}")
            return {
                "op": op,
                "a": a,
                "b": b,
            }
    elif op == 2:
        print(f"{a} - {b} = {a - b}")
        return {
            "op": op,
            "a": a,
            "b": b,
        }

    if op == 3 and a is None and b is None:
        # multiplicacao
        while True:
            try:
                a = int(input())
                print(f"{a} * ", end="")
                b = int(input())
            except ValueError:
                print("\nA entrada deve ser apenas número.\n")
                continue
            print(f"{a} * {b} = {a * b}")
            return {
                "op": op,
                "a": a,
                "b": b,
            }
    elif op == 3:
        print(f"{a} * {b} = {a * b}")
        return {
                "a": a,
                "op": op,
                "b": b,
            }

    if op == 4 and a is None and b is None:
        # divisao
        while True:
            try:

                a = int(input())
                print(f"{a} / ", end="")
                b = int(input())
                if b == 0:
                    print("Não é possível dividir por Zero(0)")
                    print("Digite os números:\n")
                    continue
            except ValueError:
                print("\nA entrada deve ser apenas número.\n")
                continue
            print(f"{a} / {b} = {a / b}")
            return {
                "a": a,
                "op": op,
                "b": b,
            }
    elif op == 4:
        print(f"{a} / {b} = {a / b}")
        return {
                "a": a,
                "op": op,
                "b": b,
            }