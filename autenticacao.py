import sqlite3
import hashlib

def criar_conexao():
    return sqlite3.connect('gostoso_pra_cachorro.db')

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def registrar_usuario(nome, email, senha, papel):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    senha_segura = criptografar_senha(senha)
    
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha, papel)
            VALUES (?, ?, ?, ?)
        ''', (nome, email, senha_segura, papel))
        conexao.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conexao.close()

def fazer_login(email, senha):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    senha_segura = criptografar_senha(senha)
    
    cursor.execute('''
        SELECT id, nome, papel FROM usuarios
        WHERE email = ? AND senha = ?
    ''', (email, senha_segura))
    
    usuario = cursor.fetchone()
    conexao.close()
    
    if usuario:
        print(f"\nLOGIN APROVADO! Bem-vinda(o), {usuario[1]}.")
        return {"id": usuario[0], "nome": usuario[1], "papel": usuario[2]}
    else:
        print("\nACESSO NEGADO: E-mail ou senha incorretos.")
        return None