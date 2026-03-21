# wsBackend-Fabrica26.1
# 🔐 Secure

Sistema de segurança web desenvolvido como projeto acadêmico para a Fábrica de Software 2026.1.

## 📋 Funcionalidades

- 🕵️ **IP Finder** — Identifica a localização e informações de um endereço IPv4 usando a API IPInfo
- 🎣 **Link Checker** — Verifica se uma URL é maliciosa ou phishing usando a API VirusTotal
- 📋 **Histórico de Verificações** — Armazena e exibe todas as consultas realizadas com opção de editar e limpar

## 🛠️ Tecnologias

- Python 3.11
- Django
- HTML e CSS
- SQLite
- API VirusTotal v3
- API IPInfo

## ⚙️ Como instalar e rodar

**1. Clone o repositório**
```bash
git clone https://github.com/Jonathan-atlas0/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. As chaves de API nos  arquivos `virustotal.py e ipinfo.py`**


**5. Rode as migrations**
```bash
python manage.py migrate
```

**6. Inicie o servidor**
```bash
python manage.py runserver
```

Botão direto no link do terminal

## 🔑 APIs utilizadas

| API | Uso | Link |
|-----|-----|------|
| VirusTotal | Verificação de URLs maliciosas | [virustotal.com](https://www.virustotal.com) |
| IPInfo | Localização de endereços IP | [ipinfo.io](https://ipinfo.io) |

## 👨‍💻 Autor

Desenvolvido por *Jonathan* — Fábrica de Software 2026.1