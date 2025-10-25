
-----

# Apolo IA ✒️

**Apolo IA** é um agente de inteligência artificial criado para ser um poeta. Ele utiliza LangChain para orquestração de IA e FastAPI para servir um endpoint de API, permitindo a geração de poesias sob demanda.

-----

## 🎯 Sobre o Projeto (A Motivação)

Este projeto nasceu de uma necessidade... romântica. Eu costumava escrever poesias para minha namorada, mas minhas habilidades como poeta eram, na melhor das hipóteses, cômicas. 😅

Para resolver isso (e continuar impressionando), decidi criar o Apolo IA: um "eu" poético digital que realmente sabe como usar as palavras. O projeto que começou como uma brincadeira se tornou um estudo fascinante sobre como integrar LLMs (Modelos de Linguagem) em uma aplicação real com backend e frontend.

A interface visual foi prototipada e construída usando a plataforma **Lovable**.

## 🚀 Tecnologias Utilizadas

  * **Backend:** [Python](https://www.python.org/) & [FastAPI](https://fastapi.tiangolo.com/)
  * **IA & Orquestração:** [LangChain](https://www.langchain.com/)
  * **Frontend:** [Lovable](https://lovable.vc/)

## ✨ Funcionalidades

  * Geração de poesias originais com base em um tema ou prompt.
  * Endpoint de API robusto e rápido construído com FastAPI.
  * Uso de Agentes LangChain para garantir respostas mais criativas e coesas.
  * Interface de usuário limpa e interativa.

## 🏁 Começando (Getting Started)

Siga estas instruções para obter uma cópia do projeto rodando em sua máquina local para desenvolvimento e testes.

### Pré-requisitos

  * [Python 3.9+](https://www.python.org/downloads/)
  * [Git](https://git-scm.com/)
  * Uma chave de API da OpenAI (ou outro provedor de LLM que você usou com o LangChain).

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/hugocbb/apolo-ia.git
    cd apolo-ia
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**

    ```bash
    # Para Unix/MacOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação (Backend)

Com o ambiente virtual ativado e as dependências instaladas, inicie o servidor FastAPI:

```bash
fastapi dev main.py
```

O servidor estará disponível em `http://127.0.0.1:8000`.

## 📚 Como Usar (API)

Assim que o servidor estiver rodando, você pode acessar a documentação interativa do FastAPI (via Swagger UI) no seu navegador:

**➡️ `http://127.0.0.1:8000/docs`**

Lá, você pode testar todos os endpoints diretamente pelo navegador.

## 🖼️ Interface (Frontend)

O frontend foi construído na plataforma Lovable. Para usá-lo, acesse o link da aplicação:

**https://apolo-ia-wheat.vercel.app/**


## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo (LICENSE.md) para mais detalhes.

-----

Feito com ❤️ (e um pouco de IA) por **Hugo Carlos Barbosa Brandão**

[](https://www.linkedin.com/in/hugocbb/)
[](https://github.com/hugocbb])
