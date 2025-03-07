from concurrent.futures import ThreadPoolExecutor
from .core.common_config import config, logging
from typing import Generator
import datetime

def apply_leet_transformations(word: str) -> Generator[str, None, None]:
    yield word
    for char, replacement in config.leet_mappings.items():
        if char in word:
            yield word.replace(char, replacement)
            yield word.replace(char, replacement.upper())

def enhanced_dictionary_attack(output_file: str = "enhanced_dict.txt") -> None:
    transformations = [
        lambda x: x,
        lambda x: x.capitalize(),
        lambda x: x.upper(),
        lambda x: x + "123",
        lambda x: x + "!",
        lambda x: "!" + x,
        lambda x: x + str(datetime.datetime.now().year)[2:]
    ]

    try:
        with ThreadPoolExecutor() as executor, open(output_file, "w") as f:
            for word in config.base_words:
                variants = set()
                for transform in transformations:
                    transformed = transform(word)
                    variants.update(apply_leet_transformations(transformed))
                
                executor.submit(lambda w: [f.write(v + '\n') for v in w], variants)
        
        logging.info(f"Dicionário aprimorado finalizado: {output_file}")
    except Exception as e:
        logging.error(f"Erro no dicionário aprimorado: {str(e)}")

if __name__ == "__main__":
    enhanced_dictionary_attack()