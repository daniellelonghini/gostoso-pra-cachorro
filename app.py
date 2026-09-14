from modelos import PerfilCachorro
from receitas import ReceitaNatural
from emergencia import exibir_dicas_emergencia

# Preparando os dados iniciais
teo = PerfilCachorro("Téo", "Médio")
luna = PerfilCachorro("Luna", "Pequeno")
lilica = PerfilCachorro("Lilica", "Pequeno")

luna.registrar_medicamento("Capstar", "14/09/2026", "Antipulgas")
teo.registrar_medicamento("Canex composto", "14/09/2026", "Vermífugo")

def exibir_menu():
    print("\n--- GOSTOSO PRA CACHORRO ---")
    print("Digite o número da opção desejada e aperte Enter:")
    print("1. Ver Perfis e Medicamentos")
    print("2. Dicas de Emergência")
    print("3. Sair do Aplicativo")
    
# O Loop principal do aplicativo
while True:
    exibir_menu()
    escolha = input("Sua escolha: ")
    
    if escolha == '1':
        print(f"\nPerfis Ativos: {teo.nome}, {luna.nome} e {lilica.nome}.")
        print("Últimos medicamentos registrados:")
        for med in luna.historico_saude:
            print(f"- {luna.nome}: {med['tipo']} ({med['medicamento']}) em {med['data']}")
        for med in teo.historico_saude:
            print(f"- {teo.nome}: {med['tipo']} ({med['medicamento']}) em {med['data']}")
            
    elif escolha == '2':
        exibir_dicas_emergencia()
        
    elif escolha == '3':
        print("\nSaindo do aplicativo... Um lambeijo e até a próxima!")
        break
        
    else:
        print("\nOpção inválida. Por favor, digite 1, 2 ou 3.")
