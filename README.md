# Gerador de Wordlists para Pentest

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Ethical](https://img.shields.io/badge/Use-Acadêmico%2FÉtico-success)

Repositório acadêmico para estudo de técnicas de quebra de senhas e desenvolvimento de defesas cibernéticas.

> **Aviso Importante:** Este projeto destina-se exclusivamente a fins educacionais e de pesquisa autorizada. Qualquer uso malicioso é estritamente proibido.

## 📚 Visão Geral

Conjunto de ferramentas para análise de segurança de senhas, contendo:
- Geradores de wordlists especializados
- Modelos de ataques controlados
- Framework para estudo de padrões de senhas
- Base de conhecimento em autenticação segura

### Padrões Comuns de Senhas Mapeados

| Categoria         | Exemplos Comuns         | Frequência |
|-------------------|-------------------------|------------|
| **Datas**         | 01011999, 12122012     | 23%        |
| **Sequências**    | 123456, qwerty         | 18%        |
| **Info. Pessoal** | nome+aniversario        | 15%        |
| **Padrões Complexos** | S3nh@!, P@ssw0rd       | 9%         |


## 🛠️ Módulos Principais

### Geradores de Wordlists
| Módulo | Descrição | Técnica | Saída |
|--------|-----------|---------|-------|
| `brute_force` | Combinações exaustivas | Força bruta paralelizada | `brute_force.txt` |
| `dictionary_attack` | Transformações léxicas avançadas | Leet speak + Capitalização | `enhanced_dict.txt` |
| `keyboard_patterns` | Padrões de teclado comuns | Sequências adjacentes | `keyboard_patterns.txt` |
| `date_generator` | Combinações temporais | Formatos de datas múltiplos | `dates.txt` |
| `social_engineering` | Dados pessoais combinados | Engenharia social | `social_engineering.txt` |

### Funcionalidades Chave
- Multi-threading nativo
- Configuração centralizada
- Geração modular
- Logging detalhado
- Tratamento de erros robusto

## 🚀 Começando

### Pré-requisitos
- Python 3.10+
- SSD para operações I/O intensivas
- Ambiente virtual (recomendado)

### Instalação
```bash
# Clone o repositório
git clone https://github.com/amonzada/bruteforce-wordlist-generator.git

# Acesse o diretório
cd bruteforce-wordlist-generator

# Instale as dependências
pip install -r requirements.txt  
```

## Execução
```bash
# Execução completa
python -m geradores.main

# Execução individual (exemplo)
python -m geradores.dictionary_attack --output custom_dict.txt
```

## 📈 Dados Técnicos

# Complexidade de Senhas
```bash
def calcular_entropia(tamanho, charset_size):
    return tamanho * math.log2(charset_size)

# Exemplo:
entropia = calcular_entropia(8, 94)  # 8 caracteres, 94 possíveis
print(f"Entropia: {entropia:.2f} bits")  # ≈ 52.00 bits
```

# Estatísticas de Geração

### Desempenho
| Técnica         | Senhas/min* | Tamanho Médio |
|-----------------|-------------|---------------|
| **Brute Force** | 1.2M        | 6 caracteres  |
| **Dictionary**  | 850K        | 10 caracteres |
| **Datas**       | 450K        | 8 caracteres  |
| **Padrões**     | 650K        | 9 caracteres  |

\*Testado em i7-11800H, 32GB RAM, SSD NVMe


## 🤝 Como Contribuir
Sinta-se à vontade para abrir issues e pull requests para melhorar este projeto!

- Faça um fork do projeto
- Crie sua branch (git checkout -b feature/nova-tecnica)
- Comite suas mudanças (git commit -m 'Adiciona nova técnica')
- Faça push para a branch (git push origin feature/nova-tecnica)
- Abra um Pull Request


## 🔮 Próximos Passos

- Suporte a GPU/CUDA
- Integração com hashcat
- Interface Web educativa
- Análise estatística integrada
- Suporte a regras personalizadas

## Licença
Este projeto é distribuído sob a licença MIT.