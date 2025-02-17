Aqui está o arquivo `README.md` em Markdown para o código que você forneceu:

---

```markdown
# Envio Automático de Arquivos no WhatsApp

Este script automatiza o envio de arquivos para um grupo específico no WhatsApp Web em um dia e horário pré-definidos. Ele utiliza o Selenium para controlar o navegador e realizar as ações necessárias.

## Funcionalidades

- **Automatização do WhatsApp Web**: O script abre o WhatsApp Web, faz login manualmente (aguarda 20 segundos para isso) e envia um arquivo para um grupo específico.
- **Agendamento Semanal**: O envio é programado para ocorrer em um dia e horário específicos (por exemplo, todas as segundas-feiras às 9:00).
- **Envio de Arquivos**: O script permite enviar arquivos de qualquer tipo (por exemplo, `.mp4`, `.pdf`, etc.) para o grupo selecionado.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Selenium**: Biblioteca para automação de navegadores.
- **WebDriver**: Utilizado para controlar o navegador (por exemplo, ChromeDriver para o Google Chrome).

## Como Usar

### Pré-requisitos

1. **Python 3.x**: Certifique-se de ter o Python instalado.
2. **Selenium**: Instale a biblioteca Selenium:
   ```bash
   pip install selenium
   ```
3. **WebDriver**: Baixe o WebDriver correspondente ao seu navegador (por exemplo, [ChromeDriver](https://sites.google.com/chromium.org/driver/) para o Google Chrome) e defina o caminho no script.

### Configuração

1. **Defina o Caminho do WebDriver**:
   No script, substitua `'/caminho/para/chromedriver'` pelo caminho do seu WebDriver.

2. **Defina o Grupo e o Arquivo**:
   - Substitua `'Nome do Grupo'` pelo nome exato do grupo no WhatsApp.
   - Substitua `'/caminho/do/arquivo.mp4'` pelo caminho completo do arquivo que deseja enviar.

3. **Defina o Dia e Horário de Envio**:
   - No script, altere `dia_envio` para o dia da semana desejado (por exemplo, `'Monday'` para segunda-feira).
   - Altere `horario_envio` para o horário desejado (por exemplo, `'09:00'`).

### Executando o Script

1. Navegue até o diretório do script.
2. Execute o script:
   ```bash
   python enviar_whatsapp.py
   ```
3. Faça login manualmente no WhatsApp Web dentro dos 20 segundos iniciais.
4. O script aguardará até o dia e horário programados para enviar o arquivo.

### Exemplo de Uso

- **Dia de Envio**: Segunda-feira (`'Monday'`).
- **Horário de Envio**: 9:00 (`'09:00'`).
- **Arquivo**: Um arquivo `.mp4` localizado em `'/caminho/do/arquivo.mp4'`.
- **Grupo**: Um grupo chamado `'Nome do Grupo'`.

O script aguardará até a próxima segunda-feira às 9:00 e enviará o arquivo para o grupo especificado.

## Estrutura do Código

- **`enviar_arquivo_whatsapp`**: Função que realiza o envio do arquivo para o grupo no WhatsApp.
- **`executar_envio_semanal`**: Função principal que configura o agendamento e executa o envio.

## Observações

1. **Login Manual**: O script aguarda 20 segundos para que você faça login manualmente no WhatsApp Web.
2. **Precisão do Agendamento**: O script calcula o tempo restante até o próximo horário de envio e aguarda esse período.
3. **Compatibilidade**: Testado com o Google Chrome e ChromeDriver. Certifique-se de usar versões compatíveis.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`).
3. Commit suas mudanças (`git commit -m 'Adicionando NovaFeature'`).
4. Push para a branch (`git push origin feature/NovaFeature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Desenvolvido por

[Seu Nome]  
[GitHub](https://github.com/seu-usuario)
```
