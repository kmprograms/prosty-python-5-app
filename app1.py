from typing import Callable

"""
    Napisz program, w którym na podstawie listy napisów utworzysz nową kolekcję,
    zawierającą napisy, składające się tylko i wyłącznie ze znaków o parzystych
    kodach. Elementy tej listy zapisz do pliku tekstowego o wybranej przez Ciebie
    nazwie. 
"""

def has_only_even_codes_chars(text: str) -> bool:
    return len([t for t in text if ord(t) % 2 == 0]) == len(text)

def get_expressions_with_condition(expressions: list[str], condition: Callable[[str], bool]):
    return [e for e in expressions if condition(e)]

def save_to_file(filename: str, expressions: list[str]) -> None:
    with open(filename, 'w') as f:
        [f.write(f'{e}\n') if i < len(expressions) - 1 else f.write(e) for i, e in enumerate(expressions)]


def main() -> None:
    expressions = ['BBDD', 'ABCD', 'BBDDFFF', 'ABABABA']
    filtered_expressions = get_expressions_with_condition(expressions, has_only_even_codes_chars)
    print(filtered_expressions)
    save_to_file('data.txt', filtered_expressions)

if __name__ == '__main__':
    main()
