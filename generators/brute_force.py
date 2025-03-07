import itertools
from concurrent.futures import ThreadPoolExecutor
from .core.common_config import config, logging

def generate_length(length: int, output_file: str):
    with open(output_file, "a") as f:
        for combo in itertools.product(config.brute_charset, repeat=length):
            f.write("".join(combo) + "\n")

def brute_force_generator(output_file: str = "brute_force.txt") -> None:
    try:
        with ThreadPoolExecutor() as executor:
            executor.map(
                generate_length,
                range(config.min_length, config.max_length + 1),
                [output_file] * (config.max_length - config.min_length + 1)
            )
        logging.info(f"Força bruta finalizada: {output_file}")
    except Exception as e:
        logging.error(f"Erro na geração por força bruta: {str(e)}")

if __name__ == "__main__":
    brute_force_generator()