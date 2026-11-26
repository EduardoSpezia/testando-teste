#Aqui vou desenvolver meu código de teste para a revisão .# Lista (array) global para armazenar os dicionários com os dados dos motores
motores = []

def cadastrar_motor():
    print("\n--- CADASTRAR NOVO MOTOR ---")
    codigo = input("Código/ID do motor: ").strip()
    
    # Verifica se já existe um motor com o mesmo código
    for motor in motores:
        if motor["codigo"].lower() == codigo.lower():
            print("Erro: Já existe um motor cadastrado com este código!")
            return

    marca = input("Marca (ex: WEG, Siemens): ").strip()
    modelo = input("Modelo: ").strip()
    
    try:
        potencia_cv = float(input("Potência (CV): "))
        rpm = int(input("Rotação (RPM): "))
        tensao = input("Tensão (ex: 220V/380V): ").strip()
    except ValueError:
        print("Erro: Potência e RPM devem ser valores numéricos. Cadastro cancelado.")
        return

    novo_motor = {
        "codigo": codigo,
        "marca": marca,
        "modelo": modelo,
        "potencia_cv": potencia_cv,
        "rpm": rpm,
        "tensao": tensao
    }
    
    motores.append(novo_motor)
    print(f"Motor '{codigo}' cadastrado com sucesso!")

def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for i, motor in enumerate(motores, start=1):
        print(f"{i}. [Cód: {motor['codigo']}] {motor['marca']} - Mod: {motor['modelo']} | "
              f"{motor['potencia_cv']} CV | {motor['rpm']} RPM | {motor['tensao']}")

def buscar_motor():
    print("\n--- BUSCAR MOTOR ---")
    termo = input("Digite o código ou marca para buscar: ").strip().lower()
    encontrados = [
        m for m in motores 
        if termo in m["codigo"].lower() or termo in m["marca"].lower()
    ]

    if not encontrados:
        print("Nenhum motor encontrado com esse critério.")
        return

    for motor in encontrados:
        print(f"-> Cód: {motor['codigo']} | Marca: {motor['marca']} | Modelo: {motor['modelo']} | "
              f"Potência: {motor['potencia_cv']} CV | RPM: {motor['rpm']} | Tensão: {motor['tensao']}")

def atualizar_motor():
    print("\n--- ATUALIZAR MOTOR ---")
    codigo = input("Digite o código do motor que deseja atualizar: ").strip()

    for motor in motores:
        if motor["codigo"].lower() == codigo.lower():
            print(f"Editando motor: {motor['marca']} {motor['modelo']} (Deixe em branco para manter o atual)")
            
            nova_marca = input(f"Marca [{motor['marca']}]: ").strip()
            novo_modelo = input(f"Modelo [{motor['modelo']}]: ").strip()
            nova_potencia = input(f"Potência CV [{motor['potencia_cv']}]: ").strip()
            novo_rpm = input(f"RPM [{motor['rpm']}]: ").strip()
            nova_tensao = input(f"Tensão [{motor['tensao']}]: ").strip()

            if nova_marca:
                motor["marca"] = nova_marca
            if novo_modelo:
                motor["modelo"] = novo_modelo
            if nova_potencia:
                try:
                    motor["potencia_cv"] = float(nova_potencia)
                except ValueError:
                    print("Aviso: Potência inválida, valor anterior mantido.")
            if novo_rpm:
                try:
                    motor["rpm"] = int(novo_rpm)
                except ValueError:
                    print("Aviso: RPM inválido, valor anterior mantido.")
            if nova_tensao:
                motor["tensao"] = nova_tensao

            print("Motor atualizado com sucesso!")
            return

    print("Motor não encontrado.")

def remover_motor():
    print("\n--- REMOVER MOTOR ---")
    codigo = input("Digite o código do motor que deseja remover: ").strip()

    for i, motor in enumerate(motores):
        if motor["codigo"].lower() == codigo.lower():
            removido = motores.pop(i)
            print(f"Motor '{removido['codigo']} - {removido['marca']}' removido com sucesso!")
            return

    print("Motor não encontrado.")

def menu():
    while True:
        print("\n===============================")
        print("   SISTEMA DE MOTORES (TESTE)  ")
        print("===============================")
        print("1. Cadastrar motor")
        print("2. Listar todos os motores")
        print("3. Buscar motor")
        print("4. Atualizar motor")
        print("5. Remover motor")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            atualizar_motor()
        elif opcao == "5":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    # Dados iniciais pré-carregados para facilitar seus testes
    motores.extend([
        {"codigo": "M001", "marca": "WEG", "modelo": "W22", "potencia_cv": 10.0, "rpm": 1750, "tensao": "220V/380V"},
        {"codigo": "M002", "marca": "Siemens", "modelo": "1LE0", "potencia_cv": 5.0, "rpm": 3500, "tensao": "380V/660V"}
    ])
    
    menu()