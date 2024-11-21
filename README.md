# Repositório de Exercícios e Notebooks de Python

Este repositório contém uma série de exercícios e notebooks para aprender e praticar Python, cobrindo conceitos de fundamentos, controle de fluxo, estrutura de dados e programação intermediária. A estrutura do repositório está organizada em pastas por aula, cada uma contendo exercícios e notebooks ilustrativos.

## Estrutura do Repositório

```plaintext
.
├── LICENSE
├── README.md
├── aula_1
│   ├── exercicios
│   │   ├── README.md
│   │   ├── py1_ex1.py
│   │   ├── py1_ex10.py
│   │   ├── py1_ex2.py
│   │   ├── py1_ex3.py
│   │   ├── py1_ex4.py
│   │   ├── py1_ex5.py
│   │   ├── py1_ex6.py
│   │   ├── py1_ex7.py
│   │   ├── py1_ex8.py
│   │   └── py1_ex9.py
│   └── notebooks
│       ├── condicional.ipynb
│       ├── estrutura_dados.ipynb
│       └── tipos_python.ipynb
├── aula_2
│   └── exercicios
│       ├── README.md
│       ├── py2_ex1.py
│       ├── py2_ex2.py
│       ├── py2_ex3.py
│       ├── py2_ex4.py
│       └── py2_ex5.py
└── aula_3
    └── exercicios
        ├── README.md
        ├── py3_ex1.py
        ├── py3_ex2.py
        ├── py3_ex3.py
        └── py3_ex4.py
```

## Descrição das Aulas

### Aula 1
A primeira aula aborda conceitos básicos de Python e introduz exercícios para consolidar o aprendizado. Os principais tópicos cobertos incluem tipos de dados, estruturas condicionais e manipulação de estruturas de dados fundamentais.

- **Notebooks**:
  - `tipos_python.ipynb`: Apresenta os tipos de dados em Python, como inteiros, floats, strings e listas.
  - `condicional.ipynb`: Aborda o uso de estruturas condicionais (`if`, `elif`, `else`) para controle de fluxo.
  - `estrutura_dados.ipynb`: Introduz as principais estruturas de dados como listas, dicionários, tuplas e sets.

- **Exercícios**:
  - `py1_ex1.py` a `py1_ex10.py`: Cada arquivo implementa exercícios específicos, abordando temas como:
    - Operações em listas e strings.
    - Manipulação de variáveis e controle de fluxo.
    - Estruturas de dados e cálculos matemáticos simples.

### Aula 2
A segunda aula avança para conceitos intermediários de Python, incluindo o uso de decoradores, argumentos variáveis e métodos privados. Os exercícios focam em práticas comuns na criação de funções avançadas e classes mais robustas.

- **Exercícios**:
  - `py2_ex1.py` a `py2_ex5.py`: Exercícios de nível intermediário abordando:
    - Funções com número variável de argumentos (`*args` e `**kwargs`).
    - Criação e manipulação de arquivos com a classe `FileManager`.
    - Uso de decoradores (`log_function_calls` e `cache_results`) para registro e cache de funções.
    - Encapsulamento e controle de acesso em classes com a classe `ContaBancaria`.

### Aula 3
A terceira aula explora técnicas avançadas de cálculo numérico, gradiente descendente e backpropagation. Os exercícios são mais desafiadores e ideais para quem já possui uma boa base de Python e deseja praticar habilidades matemáticas e computacionais.

- **Exercícios**:
  - `py3_ex1.py`: Encontrar o mínimo de um polinômio de segundo grau utilizando o método do gradiente descendente.
  - `py3_ex2.py`: Soma dos elementos de uma matriz \( N \times M \) utilizando broadcasting e loops.
  - `py3_ex3.py`: Cálculo e visualização gráfica de um polinômio de terceiro grau e sua derivada.
  - `py3_ex4.py`: Implementação de backpropagation em uma função de ativação ReLU para aprendizado de redes neurais simples.

## Como Executar

1. Clone o repositório:
   ```sh
   git clone https://github.com/usuario/repositorio_exercicios_python.git
   cd repositorio_exercicios_python
   ```

2. Navegue até a pasta de um exercício específico e execute o script:
   ```sh
   python aula_3/exercicios/py3_ex1.py
   ```

3. Explore os notebooks interativos utilizando Jupyter Notebook ou JupyterLab:
   ```sh
   jupyter notebook
   ```