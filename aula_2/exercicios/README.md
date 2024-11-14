# Exercícios Python - Nível Intermediário

Este repositório contém uma coleção de exercícios em Python voltados para praticantes de nível intermediário. Cada exercício implementa conceitos como argumentos variáveis, decoradores, manipulação de arquivos e métodos privados, visando aprofundar o conhecimento em técnicas mais avançadas do Python. Cada exercício é separado em scripts distintos com descrições claras de suas funcionalidades.

## Índice
- [Exercícios Python - Nível Intermediário](#exercícios-python---nível-intermediário)
  - [Índice](#índice)
  - [1. Função para Soma de Argumentos Variáveis](#1-função-para-soma-de-argumentos-variáveis)
  - [2. Classe `FileManager` para Manipulação de Arquivos](#2-classe-filemanager-para-manipulação-de-arquivos)
  - [3. Decorador para Registro de Chamadas de Função](#3-decorador-para-registro-de-chamadas-de-função)
  - [4. Classe `ContaBancaria` com Métodos Privados](#4-classe-contabancaria-com-métodos-privados)
  - [5. Decorador para Cache de Resultados de Funções](#5-decorador-para-cache-de-resultados-de-funções)
  - [Como Executar](#como-executar)

## 1. Função para Soma de Argumentos Variáveis
**Arquivo:** `py2_ex1.py`  
Este script contém uma função que aceita um número variável de argumentos e retorna a soma deles. Esse exercício explora o uso de `*args` para capturar argumentos variáveis e somá-los. 

## 2. Classe `FileManager` para Manipulação de Arquivos
**Arquivo:** `py2_ex2.py`  
A classe `FileManager` permite abrir, ler e fechar arquivos. Ela utiliza métodos com `*args` e `**kwargs` para passar um número variável de argumentos, possibilitando a abertura de arquivos com diferentes modos e configurações. É ideal para entender a manipulação de arquivos com flexibilidade nos parâmetros.

## 3. Decorador para Registro de Chamadas de Função
**Arquivo:** `py2_ex3.py`  
Este script define um decorador chamado `log_function_calls`, que registra o nome da função chamada, seus argumentos e o valor retornado em um arquivo de log. Ele demonstra o uso de decoradores para monitorar e registrar o comportamento de funções, uma prática valiosa para depuração e análise de código.

## 4. Classe `ContaBancaria` com Métodos Privados
**Arquivo:** `py2_ex4.py`  
A classe `ContaBancaria` implementa métodos privados para manipular o saldo da conta. Os métodos públicos de depósito e saque acessam esses métodos privados usando a sintaxe `_nome_do_metodo`. Este exercício reforça o uso de métodos privados para encapsular a lógica de acesso direto aos dados da classe.

## 5. Decorador para Cache de Resultados de Funções
**Arquivo:** `py2_ex5.py`  
O decorador `cache_results` armazena os resultados de uma função em uma cache e reutiliza esses resultados caso a função seja chamada novamente com os mesmos argumentos. Este exercício demonstra o uso de cache para otimizar chamadas repetidas de funções com os mesmos dados de entrada, uma técnica importante para aumentar a eficiência de scripts.

## Como Executar
Para executar qualquer um desses exercícios, clone este repositório e execute os scripts usando o Python 3:

```sh
python py2_ex1.py
```
Substitua `py2_ex1.py` pelo nome do arquivo do script que deseja executar.