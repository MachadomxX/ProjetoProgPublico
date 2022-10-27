from hashlib import blake2b

# https://docs.python.org/3/library/hashlib.html

def cifrar(senha):
    h = blake2b()
    em_bytes = bytes(senha, encoding= 'utf-8')
    h.update(em_bytes)
    return h.hexdigest()

def validar_senha(cifrado, senha_fornecida):
    fornecida = cifrar(senha_fornecida)
    print(fornecida)
    print(cifrado)
    if cifrado == fornecida:
         return True
    return False

print(cifrar('senha'))