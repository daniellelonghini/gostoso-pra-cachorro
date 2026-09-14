from modelos import PerfilCachorro
from receitas import ReceitaNatural

# 1. Carregando os perfis da família
teo = PerfilCachorro("Téo", "Médio")
luna = PerfilCachorro("Luna", "Pequeno")
lilica = PerfilCachorro("Lilica", "Pequeno")

print("--- Sistema Gostoso pra Cachorro Iniciado ---")
print(f"Perfis carregados com sucesso: {teo.nome}, {luna.nome} e {lilica.nome}.")

# 2. Registrando o histórico de medicamentos reais
teo.registrar_medicamento("Canex composto", "14/09/2026", "Vermífugo")
luna.registrar_medicamento("Capstar", "14/09/2026", "Antipulgas")
lilica.registrar_medicamento("Capstar", "14/09/2026", "Antipulgas")

# 3. Criando uma receita e vinculando aos perfis
receita_imunidade = ReceitaNatural("Sopinha de Cenoura com Frango", "Aumentar imunidade", "Todos os portes")
receita_imunidade.adicionar_ingrediente("Cenoura", "200g")
receita_imunidade.adicionar_ingrediente("Frango desfiado", "300g")

print("\n--- Resumo do Dia ---")
print(f"Receita do dia: {receita_imunidade.nome} (Objetivo: {receita_imunidade.objetivo})")
print("Tudo pronto e funcionando em conjunto!")
