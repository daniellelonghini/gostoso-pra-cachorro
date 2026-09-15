import sqlite3

def iniciar_banco():
    # Conecta ao arquivo do banco de dados (ele cria o arquivo automaticamente se não existir)
    conexao = sqlite3.connect('gostoso_pra_cachorro.db')
    cursor = conexao.cursor()

    # 1. Criando a Tabela de Usuários (preparando para o sistema de login)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            papel TEXT NOT NULL
        )
    ''')

    # 2. Criando a Tabela de Cachorros (ligada ao usuário que é o dono)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cachorros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            porte TEXT NOT NULL,
            dono_id INTEGER,
            FOREIGN KEY (dono_id) REFERENCES usuarios (id)
        )
    ''')

    # Salva as alterações e fecha a caixa-forte
    conexao.commit()
    conexao.close()
    
    print("\n--- SUCESSO ---")
    print("Banco de dados 'gostoso_pra_cachorro.db' criado e configurado!")
    print("Tabelas de Usuários e Cachorros prontas para receber os dados.")

# Executa a função quando rodamos o arquivo
if __name__ == '__main__':
    iniciar_banco()
