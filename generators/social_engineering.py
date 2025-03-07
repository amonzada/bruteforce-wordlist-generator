from concurrent.futures import ThreadPoolExecutor
from .core.common_config import logging

def social_engineering_generator(output_file: str = "social_engineering.txt") -> None:
    personal_data = {
        'names': ["joao", "maria", "pedro", "ana"],
        'birthdays': ["0101", "1507", "2212", "0310"],
        'pets': ["bob", "luna", "max", "lady"],
        'hobbies': ["futebol", "musica", "viagem", "leitura"]
    }

    try:
        combinations = []
        for name in personal_data['names']:
            for birth in personal_data['birthdays']:
                combinations.extend([
                    f"{name}{birth}", f"{birth}{name}",
                    f"{name.capitalize()}{birth}", f"{birth}{name.upper()}"
                ])
        
        with ThreadPoolExecutor() as executor, open(output_file, "w") as f:
            executor.map(lambda x: f.write(x + "\n"), combinations)
        
        logging.info(f"Engenharia social finalizada: {output_file}")
    except Exception as e:
        logging.error(f"Erro na engenharia social: {str(e)}")

if __name__ == "__main__":
    social_engineering_generator()