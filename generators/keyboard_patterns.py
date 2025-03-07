from .core.common_config import logging

def keyboard_patterns(output_file: str = "keyboard_patterns.txt") -> None:
    patterns = [
        "qwerty", "asdfgh", "zxcvbn", "1qaz2wsx", "1q2w3e4r",
        "qazwsx", "qweasdzxc", "poiuyt", "mnbvcxz", "!qaz@wsx#edc"
    ]
    
    try:
        with open(output_file, "w") as f:
            for p in patterns:
                f.write(f"{p}\n{p.upper()}\n{p.capitalize()}!\n")
        logging.info(f"Padrões de teclado gerados: {output_file}")
    except Exception as e:
        logging.error(f"Erro nos padrões de teclado: {str(e)}")

if __name__ == "__main__":
    keyboard_patterns()