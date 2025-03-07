from concurrent.futures import ThreadPoolExecutor
from .brute_force import brute_force_generator
from .dictionary_attack import enhanced_dictionary_attack
from .keyboard_patterns import keyboard_patterns
from .date_generator import date_based_generator
from .social_engineering import social_engineering_generator

def main():
    generators = [
        brute_force_generator,
        enhanced_dictionary_attack,
        keyboard_patterns,
        date_based_generator,
        social_engineering_generator
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(gen) for gen in generators]
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()