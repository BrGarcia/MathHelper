# 📐 MathHelper

**MathHelper** é uma ferramenta modular desenvolvida em Python projetada para auxiliar professores e educadores na criação automatizada de listas de exercícios de matemática. O sistema combina o poder da computação gráfica para gerar figuras precisas com a inteligência artificial para criar enunciados contextuais e desafiadores.



## 🚀 Funcionalidades

- **Módulo Visual (Visual Engine):** Geração de figuras geométricas (iniciando por triângulos e Teorema de Pitágoras) e gráficos de funções de 1º e 2º grau usando `Matplotlib`.
- **Módulo de IA (AI Engine):** Integração com a API do Gemini para criar problemas matemáticos dinâmicos e criativos.
- **Exportação (Export Engine):** Geração automática de arquivos PDF prontos para impressão com diagramação profissional.
- **Arquitetura Modular:** Fácil expansão para novos tipos de formas (círculos, polígonos) e temas matemáticos.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Matplotlib/Numpy:** Para renderização de geometria analítica e funções.
- **FPDF2:** Para a construção e formatação dos documentos PDF.
- **Google Generative AI:** Para a inteligência por trás dos enunciados.

## 📂 Estrutura do Projeto

```text
MathHelper/
├── main.py                 # Orquestrador central do sistema
├── modules/
│   ├── ai_engine/          # Lógica de integração com LLMs
│   ├── visual_engine/      # Classes de geometria e plotagem de gráficos
│   └── export_engine/      # Montagem e exportação de PDFs
└── output/                 # Exercícios gerados (PNGs e PDFs)
