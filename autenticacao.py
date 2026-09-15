import sqlite3
import hashlib

def criar_conexao():
    # Cria a ponte de comunicação com o nosso banco de dados
    return sqlite3.connect('gostoso_pra_cachorro.db')

def criptografar_senha(senha):
    # Transforma a senha em um código ilegível (Hash SHA-256) para segurança profissional
    return hashlib.sha256(senha.encode()).hexdigest()

def registrar_usuario(nome, email, senha, papel):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    
    # Nunca salvamos a senha real, apenas o hash criptografado
    senha_segura = criptografar_senha(senha)
    
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha, papel)
            VALUES (?, ?, ?, ?)
        ''', (nome, email, senha_segura, papel))
        conexao.commit()
        print(f"SUCESSO: Usuário {nome} cadastrado com o perfil de {papel}.")
    except sqlite3.IntegrityError:
        print(f"ERRO: O e-mail {email} já está em uso no sistema.")
    finally:
        conexao.close()

def fazer_login(email, senha):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    senha_segura = criptografar_senha(senha)
    
    # Busca no banco de dados se existe a combinação exata de email e senha criptografada
    cursor.execute('''
        SELECT id, nome, papel FROM usuarios
        WHERE email = ? AND senha = ?
    ''', (email, senha_segura))
    
    usuario = cursor.fetchone()
    conexao.close()
    
    if usuario:
        # usuario é uma tupla contendo (id, nome, papel)
        print(f"\nLOGIN APROVADO! Bem-vinda(o), {usuario[1]}.")
        print(f"Nível de acesso concedido: {usuario[2]}")
        return {"id": usuario[0], "nome": usuario[1], "papel": usuario[2]}
    else:
        print("\nACESSO NEGADO: E-mail ou senha incorretos.")
        return None

# --- Área de Testes (Simulando o uso real) ---
if __name__ == '__main__':
    print("--- INICIANDO SISTEMA DE SEGURANÇA ---")
    
    # 1. Cadastrando a equipe
    registrar_usuario("Danielle", "dani@email.com", "senha_super_secreta", "Mestra (Proprietária)")
    registrar_usuario("Namorado", "colaborador@email.com", "senha_basica", "Colaborador")
    
    # 2. Testando um login correto (Deve ser aprovado e mostrar as permissões)
    print("\n--- Teste 1: Tentativa de login correto ---")
    usuario_logado = fazer_login("dani@email.com", "senha_super_secreta")
    
    # 3. Testando um login incorreto (Deve dar acesso negado)
    print("\n--- Teste 2: Tentativa de login com senha errada ---")
    fazer_login("dani@email.com", "senha_errada_123")
