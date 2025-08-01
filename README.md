# 🧪 Python Data Validation

[![Pytest](https://github.com/ViniCordeiro/python-data-validation/actions/workflows/pytest.yml/badge.svg)](https://github.com/ViniCordeiro/python-data-validation/actions)

Projeto que simula validação de dados com testes unitários usando Python e Pytest

## 🚀 Funcionalidades testadas

- Validação de campos obrigatórios (nome, e-mail)
- Formato de e-mail válido
- Regras de negócio: valor do pedido ≥ 0
- Relacionamento: usuário deve existir no pedido

## 📦 Como executar localmente

```bash
git clone https://github.com/ViniCordeiro/python-data-validation.git
cd python-data-validation
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
pytest
```

## 📁 Estrutura

```
data/           # Dados simulados
tests/          # Testes unitários com Pytest
.github/        # Integração contínua com GitHub Actions
```