# WhatsApp Bot

Este projeto é um bot de automação para o WhatsApp Web, desenvolvido em Python, que envia mensagens promocionais e fotos automaticamente para um grupo específico em horários agendados.

## Funcionalidades

- **Login no WhatsApp Web:** Faz login na conta do usuário via escaneamento do QR Code.
- **Encontrar Grupo:** Busca e acessa um grupo específico pelo nome.
- **Enviar Mensagem:** Envia mensagens de texto para o grupo.
- **Enviar Foto:** Envia fotos para o grupo.
- **Enviar Mensagens Promocionais:** Envia mensagens promocionais em horários pré-definidos.
- **Enviar Mensagens Horárias:** Envia mensagens com horários calculados automaticamente a cada hora.

## Pré-requisitos

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (deve estar instalado e no PATH)
- Bibliotecas Python:
  - `selenium`
  - `pyperclip`
  - `schedule`
  - `pytz`

## Instalação

1. **Clone o repositório:**

    ```sh
    git clone https://github.com/seu-usuario/whatsapp-automation-bot.git
    cd whatsapp-automation-bot
    ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências:**

    ```sh
    pip install selenium pyperclip schedule pytz
    ```

4. **Baixe o [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) e adicione ao PATH.**

## Configuração

Antes de executar o script, certifique-se de configurar corretamente o caminho para o ChromeDriver e a foto a ser enviada.

```python
# Configuração do WebDriver (certifique-se de ter o chromedriver instalado e no PATH)
driver = webdriver.Chrome()

# Caminho para a foto a ser enviada
photo_path = "C:/Users/dn/Pictures/sorteio.jpeg"
