import re
from data.dataset import usuarios, pedidos

def test_usuarios_com_nome_ou_email_vazio():
    for u in usuarios:
        assert u['nome'], f"Usuário {u['id']} com nome vazio"
        assert u['email'] is not None and u['email'].strip() != '', f"Usuário {u['id']} com email vazio"

def test_formato_email():
    email_regex = r"^[^@]+@[^@]+\.[a-z]{2,}$"
    for u in usuarios:
        if u['email']:
            assert re.match(email_regex, u['email']), f"Email inválido: {u['email']}"

def test_pedidos_valor_positivo():
    for p in pedidos:
        assert p['valor'] >= 0, f"Pedido {p['id']} tem valor negativo: {p['valor']}"

def test_usuario_existente_nos_pedidos():
    usuario_ids = {u['id'] for u in usuarios}
    for p in pedidos:
        assert p['usuario_id'] in usuario_ids, f"Pedido {p['id']} com usuário inexistente: {p['usuario_id']}"