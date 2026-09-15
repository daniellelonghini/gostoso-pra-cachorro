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