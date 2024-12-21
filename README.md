# AI_Interface
Interface local para IA

# Interface de IA

Este projeto implementa uma interface gráfica em Python que interage com uma API de IA para gerar respostas a perguntas feitas pelo usuário. As respostas podem ser exportadas como texto (.txt) ou áudio (.mp3).

## Funcionalidades

1. **Gerar Resposta**: Ao inserir uma pergunta no campo "Input" e pressionar o botão "Gerar Resposta", a aplicação obtém uma resposta da IA.
2. **Nova Pergunta**: Limpa os campos de entrada e saída para permitir uma nova pergunta.
3. **Exportar Texto**: Salva a resposta gerada em um arquivo `.txt`.
4. **Exportar Áudio**: Converte a resposta em áudio utilizando a voz configurada e salva como um arquivo `.mp3`.

## Requisitos

### Bibliotecas Necessárias

Instale as bibliotecas abaixo usando `pip`:

```bash
pip install edge-tts==6.1.14 google-generativeai==0.8.3
```

## Configuração
No início do código, substitua as variáveis conforme necessário:

API_KEY: Insira sua chave de API do Google Generative AI.
AI_MODEL: O modelo de IA a ser usado (ex.: "gemini-1.5-pro-latest").
VOICE: A voz para a conversão de texto para fala (ex.: "pt-BR-FranciscaNeural").
USER_NAME: Seu nome, que aparecerá na interface.

## Uso
Execute o código para abrir a interface.
Digite uma pergunta no campo "Input".
Pressione "Gerar Resposta" para obter a resposta da IA.
Use os botões para realizar ações adicionais:
Nova Pergunta: Limpa os campos.
Exportar Texto: Salva a resposta como .txt.
Exportar Áudio: Salva a resposta como .mp3.

## Estrutura do Código
- gerar_resposta: Gera a resposta da IA para a pergunta inserida.
- nova_pergunta: Limpa os campos de input e output.
- exportar_texto: Salva a resposta em um arquivo .txt com timestamp.
- exportar_audio_async: Função assíncrona que converte a resposta em áudio e salva em um arquivo .mp3.
- exportar_audio: Wrapper para chamar a função assíncrona exportar_audio_async.

## Observações
- Certifique-se de ter conexão com a internet ao gerar a resposta da IA, pois o processo depende da API do Google.
- Consulte a documentação oficial das bibliotecas usadas para maiores informações sobre personalização de modelos de IA e vozes.

## Bibliotecas
- https://github.com/rany2/edge-tts
- https://github.com/google-gemini/generative-ai-python
