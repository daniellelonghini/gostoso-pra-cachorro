from modelos import PerfilCachorro
from emergencia import exibir_dicas_emergencia
from gestacao import DiarioGestacao

# 1. Preparando os perfis
teo = PerfilCachorro("Téo", "Médio")
lilica = PerfilCachorro("Lilica", "Pequeno")
luna = PerfilCachorro("Luna", "Pequeno")
thel = PerfilCachorro("Thel", "Pequeno")

# 2. Registrando Medicamentos
luna.registrar_medicamento("Capstar", "14/09/2026", "Antipulgas")
teo.registrar_medicamento("Canex composto", "14/09/2026", "Vermífugo")

# 3. Configurando a Árvore Genealógica (Luna e Thel)
luna.adicionar_filhote("Filhote 1")
luna.adicionar_filhote("Filhote 2")
luna.adicionar_filhote("Filhote 3")

# 4. Configurando o Diário da Mamãe
diario_luna = DiarioGestacao(luna.nome)
diario_luna.registrar_exame("10/05/2026", "Ultrassom", "4 filhotes detectados inicialmente")
diario_luna.adicionar_anotacao("15/05/2026", "Início da ração para filhotes para reforçar a nutrição da mamãe")

def exibir_menu():
    print("\n--- GOSTOSO PRA CACHORRO ---")
    print("Digite o número da opção desejada e aperte Enter:")
    print("1. Ver Perfis e Medicamentos")
    print("2. Dicas de Emergência")
    print("3. Árvore Genealógica")
    print("4. Diário da Mamãe Grávida")
    print("5. Sair do Aplicativo")
    
# O Loop principal do aplicativo
while True:
    exibir_menu()
    escolha = input("Sua escolha: ")
    
    if escolha == '1':
        print(f"\nPerfis Ativos: {teo.nome}, {luna.nome}, {lilica.nome} e {thel.nome}.")
        print("Últimos medicamentos registrados:")
        for med in luna.historico_saude:
            print(f"- {luna.nome}: {med['tipo']} ({med['medicamento']}) em {med['data']}")
        for med in teo.historico_saude:
            print(f"- {teo.nome}: {med['tipo']} ({med['medicamento']}) em {med['data']}")
            
    elif escolha == '2':
        exibir_dicas_emergencia()

    elif escolha == '3':
        print("\n--- ÁRVORE GENEALÓGICA ---")
        print(f"Mãe: {luna.nome}")
        print(f"Pai: {thel.nome}")
        print(f"Filhotes vivos registrados: {', '.join(luna.filhotes)}")
        
    elif escolha == '4':
        print("\n--- DIÁRIO DA MAMÃE GRÁVIDA ---")
        print(f"Mamãe: {diario_luna.nome_mae}")
        for exame in diario_luna.exames:
            print(f"Exame de {exame['tipo']} em {exame['data']}: {exame['resultado']}")
        for nota in diario_luna.anotacoes:
            print(f"Anotação em {nota['data']}: {nota['nota']}")
            
    elif escolha == '5':
        print("\nSaindo do aplicativo... Um lambeijo e até a próxima!")
        break
        
    else:
        print("\nOpção inválida. Por favor, digite um número de 1 a 5.")