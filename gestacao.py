class DiarioGestacao:
    def __init__(self, nome_mae):
        self.nome_mae = nome_mae
        self.exames = []
        self.historico_peso = []
        self.anotacoes = []

    def registrar_exame(self, data, tipo_exame, resultado):
        self.exames.append({"data": data, "tipo": tipo_exame, "resultado": resultado})

    def registrar_peso(self, data, peso):
        self.historico_peso.append({"data": data, "peso": peso})

    def adicionar_anotacao(self, data, nota):
        self.anotacoes.append({"data": data, "nota": nota})
