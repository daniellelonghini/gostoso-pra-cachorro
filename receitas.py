class ReceitaNatural:
    def __init__(self, nome, objetivo, porte_indicado):
        self.nome = nome
        self.objetivo = objetivo
        self.porte_indicado = porte_indicado
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente, quantidade):
        # Lista de alimentos proibidos e perigosos para cachorros
        alimentos_toxicos = ["cebola", "alho", "uva", "chocolate", "abacate", "macadâmia"]
        
        # Verifica se o ingrediente digitado está na lista de proibidos
        if ingrediente.lower() in alimentos_toxicos:
            print(f"ALERTA CRÍTICO: '{ingrediente}' é TÓXICO para cachorros! Ingrediente bloqueado.")
            return False
        else:
            self.ingredientes.append({"item": ingrediente, "quantidade": quantidade})
            print(f"Sucesso: {ingrediente} ({quantidade}) adicionado à receita '{self.nome}'.")
            return True

# --- Testando o molde (Banco de Receitas) ---

# 1. Criando uma receita que pode servir para o Téo, a Luna e a Lilica
receita_energia = ReceitaNatural("Frango com Legumes", "Manutenção de peso", "Todos os portes")

# 2. Adicionando ingredientes seguros
receita_energia.adicionar_ingrediente("Peito de Frango", "500g")
receita_energia.adicionar_ingrediente("Cenoura", "100g")

# 3. Testando a trava de segurança (tentando adicionar cebola por engano)
receita_energia.adicionar_ingrediente("Cebola", "50g")
