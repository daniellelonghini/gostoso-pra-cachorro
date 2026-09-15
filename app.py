from autenticacao import fazer_login
from modelos import PerfilCachorro
from emergencia import exibir_dicas_emergencia
from gestacao import DiarioGestacao
import sys

def exibir_menu(papel):
    print("\n--- MENU PRINCIPAL ---")
    print("Digite o número da opção desejada e aperte Enter:")
    print("1. Ver Perfis e Medicamentos")
    print("2. Dicas de Emergência")
    print("3. Árvore Genealógica")
    print("4. Diário da Mamãe Grávida")
    if papel == "Mestra (Proprietária)":
        print("5. [Área da Mestra] Configurações de Usuários")
    print("0. Sair do Aplicativo")

# --- INÍCIO DO PROGRAMA ---
print("="*40)
print("BEM-VINDO AO APP GOSTOSO PRA CACHORRO")
print("="*40)
print("Por favor, identifique-se para abrir o sistema:")
email_digitado = input("E-mail: ").strip()
senha_digitada = input("Senha: ").strip()

usuario_logado = fazer_login(email_digitado, senha_digitada)

if usuario_logado is None:
    print("\nFechando o aplicativo por segurança...")
    sys.exit()

print(f"\nAcesso liberado! Perfil de uso: {usuario_logado['papel']}")
print("Carregando os dados dos seus pets...\n")

# SÓ AGORA (DEPOIS DE LOGAR) OS CACHORROS SÃO CARREGADOS
teo = PerfilCachorro("Téo", "Médio")
lilica = PerfilCachorro("Lilica", "Pequeno")
luna = PerfilCachorro("Luna", "Pequeno")
thel = PerfilCachorro("Thel", "Pequeno")

luna.registrar_medicamento("Capstar", "14/09/2026", "Antipulgas")
teo.registrar_medicamento("Canex composto", "14/09/2026", "Vermífugo")
luna.adicionar_filhote("Filhote 1")
luna.adicionar_filhote("Filhote 2")
luna.adicionar_filhote("Filhote 3")

diario_luna = DiarioGestacao(luna.nome)
diario_luna.registrar_exame("10/05/2026", "Ultrassom", "4 filhotes detectados inicialmente")

# O Loop principal do aplicativo protegido
while True:
    exibir_menu(usuario_logado['papel'])
    escolha = input("Sua escolha: ").strip()
    
    if escolha == '1':
        print(f"\nPerfis Ativos: {teo.nome}, {luna.nome}, {lilica.nome} e {thel.nome}.")
        print("Últimos medicamentos:")
        for med in luna.historico_saude:
            print(f"- {luna.nome}: {med['tipo']} ({med['medicamento']}) em {med['data']}")
            
    elif escolha == '2':
        exibir_dicas_emergencia()

    elif escolha == '3':
        print("\n--- ÁRVORE GENEALÓGICA ---")
        print(f"Mãe: {luna.nome}, Pai: {thel.nome}, Filhotes: {', '.join(luna.filhotes)}")
        
    elif escolha == '4':
        print("\n--- DIÁRIO DA MAMÃE GRÁVIDA ---")
        for exame in diario_luna.exames:
            print(f"Exame de {exame['tipo']} em {exame['data']}: {exame['resultado']}")

    elif escolha == '5' and usuario_logado['papel'] == "Mestra (Proprietária)":
        print("\n[Área Restrita] Aqui você poderá convidar e excluir colaboradores no futuro.")
        
    elif escolha == '0':
        print("\nDeslogando... Um lambeijo e até a próxima!")
        break
        
    else:
        print("\nOpção inválida ou sem permissão.")