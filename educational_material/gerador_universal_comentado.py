import itertools
import string
import datetime
from concurrent.futures import ThreadPoolExecutor
import logging
from typing import List, Generator

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PasswordGeneratorConfig:
    """Configurações para geração de wordlists"""
    def __init__(self):
        # Caracteres para força bruta
        self.brute_charset = string.ascii_letters + string.digits + string.punctuation
        
        # Parâmetros padrão
        self.min_length = 4
        self.max_length = 8
        self.base_words = ["admin", "senha", "password", "user", "qwerty"]
        self.leet_mappings = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'}
        self.common_years = [str(y) for y in range(1980, datetime.datetime.now().year + 1)]
        self.common_specials = ["!", "@", "#", "$", "%", "&", "*", "_", "-"]

config = PasswordGeneratorConfig()

def apply_leet_transformations(word: str) -> Generator[str, None, None]:
    """Aplica transformações leet speak a uma palavra"""
    yield word
    for char, replacement in config.leet_mappings.items():
        if char in word:
            yield word.replace(char, replacement)
            yield word.replace(char, replacement.upper())

def brute_force_generator(output_file: str = "brute_force.txt") -> None:
    """Gera combinações usando força bruta com multi-threading"""
    def generate_length(length: int):
        with open(output_file, "a") as f:
            for combo in itertools.product(config.brute_charset, repeat=length):
                f.write("".join(combo) + "\n")

    with ThreadPoolExecutor() as executor:
        executor.map(generate_length, range(config.min_length, config.max_length + 1))

    logging.info(f"Força bruta finalizada: {output_file}")

def enhanced_dictionary_attack(output_file: str = "enhanced_dict.txt") -> None:
    """Ataque de dicionário aprimorado com transformações complexas"""
    transformations = [
        lambda x: x,
        lambda x: x.capitalize(),
        lambda x: x.upper(),
        lambda x: x + "123",
        lambda x: x + "!",
        lambda x: "!" + x,
        lambda x: x + str(datetime.datetime.now().year)[2:]
    ]

    with ThreadPoolExecutor() as executor, open(output_file, "w") as f:
        for word in config.base_words:
            # Gera todas as variações possíveis
            variants = set()
            for transform in transformations:
                variants.update(apply_leet_transformations(transform(word)))
            
            # Escreve no arquivo usando multi-threading
            executor.submit(lambda w: [f.write(v + '\n') for v in w], variants)

    logging.info(f"Dicionário aprimorado finalizado: {output_file}")

def keyboard_patterns(output_file: str = "keyboard_patterns.txt") -> None:
    """Gera padrões comuns de teclado"""
    patterns = [
        "qwerty", "asdfgh", "zxcvbn", "1qaz2wsx", "1q2w3e4r",
        "qazwsx", "qweasdzxc", "poiuyt", "mnbvcxz", "!qaz@wsx#edc"
    ]
    
    with open(output_file, "w") as f:
        for p in patterns:
            f.write(p + "\n")
            f.write(p.upper() + "\n")
            f.write(p.capitalize() + "!\n")

def date_based_generator(output_file: str = "dates.txt") -> None:
    """Gera combinações baseadas em datas"""
    date_formats = [
        "%d%m%Y", "%m%d%Y", "%Y%m%d", "%d%m%y", "%m%d%y",
        "%H%M%S", "%d%m", "%m%Y", "%y%m", "%Y%m"
    ]
    
    dates = []
    for year in config.common_years:
        for month in range(1, 13):
            for day in range(1, 31):
                date_obj = datetime.date(int(year), month, day)
                for fmt in date_formats:
                    dates.append(date_obj.strftime(fmt))

    with open(output_file, "w") as f:
        for d in set(dates):
            f.write(d + "\n")

def social_engineering_generator(output_file: str = "social_engineering.txt") -> None:
    """Combina informações sociais com transformações complexas"""
    personal_data = {
        'names': ["joao", "maria", "pedro", "ana"],
        'birthdays': ["0101", "1507", "2212", "0310"],
        'pets': ["bob", "luna", "max", "lady"],
        'hobbies': ["futebol", "musica", "viagem", "leitura"]
    }

    combinations = []
    for name in personal_data['names']:
        for birth in personal_data['birthdays']:
            # Gera diferentes combinações de nome e aniversário:
            # - nome seguido de data de nascimento
            # - data de nascimento seguida de nome
            # - nome capitalizado seguido de data de nascimento
            # - data de nascimento seguida de nome em maiúsculas
            combinations.extend([
                f"{name}{birth}", f"{birth}{name}",
                f"{name.capitalize()}{birth}", f"{birth}{name.upper()}"
            ])
    
    # Usa múltiplas threads para escrever as combinações no arquivo
    # Cada linha processada é escrita com uma quebra de linha
    with ThreadPoolExecutor() as executor, open(output_file, "w") as f:
        executor.map(lambda x: f.write(x + "\n"), combinations)

    # Registra no log que o processo foi concluído com sucesso
    logging.info(f"Engenharia social finalizada: {output_file}")

def main():
    """Função principal para execução dos geradores"""
    # Lista de todos os geradores de senha implementados no programa
    # Cada função gera um tipo específico de wordlist e salva em um arquivo
    generators = [
        brute_force_generator,        # Gera senhas por força bruta
        enhanced_dictionary_attack,   # Gera variações de palavras comuns
        keyboard_patterns,            # Gera padrões de teclado
        date_based_generator,         # Gera senhas baseadas em datas
        social_engineering_generator  # Gera senhas usando dados pessoais
    ]

    # Executa todos os geradores em paralelo com no máximo 4 threads
    # Isso melhora significativamente o desempenho em sistemas multi-core
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(gen) for gen in generators]
        # Aguarda todos os geradores terminarem e captura qualquer exceção
        for future in futures:
            future.result()

if __name__ == "__main__":
    # Ponto de entrada do script quando executado diretamente
    # Inicia o processo de geração de todas as wordlists
    main()