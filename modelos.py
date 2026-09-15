class PerfilCachorro:
    def __init__(self, nome, porte):
        self.nome = nome
        self.porte = porte
        self.alergias = []
        self.historico_saude = []
        self.mae = None
        self.pai = None
        self.filhotes = []

    def adicionar_alergia(self, ingrediente):
        self.alergias.append(ingrediente)
        print(f"Atenção: Alergia a {ingrediente} registrada para {self.nome}.")

    def registrar_medicamento(self, remedio, data, tipo):
        registro = {"medicamento": remedio, "data": data, "tipo": tipo}
        self.historico_saude.append(registro)
        print(f"{tipo} ({remedio}) registrado para {self.nome} na data {data}.")

    def registrar_parentesco(self, pai=None, mae=None):
        self.pai = pai
        self.mae = mae

    def adicionar_filhote(self, nome_filhote):
        self.filhotes.append(nome_filhote)