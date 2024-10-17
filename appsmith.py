import random

# Lista de palavras em inglês e suas traduções
words = {
    "variable": "variável",
    "function": "função",
    "loop": "laço",
    "conditional": "condicional",
    "array": "vetor",
    "dictionary": "dicionário",
    "string": "cadeia de caracteres",
    "integer": "inteiro",
    "float": "flutuante",
    "boolean": "booleano",
    "class": "classe",
    "object": "objeto",
    "method": "método",
    "module": "módulo",
    "package": "pacote",
    "library": "biblioteca",
    "syntax": "sintaxe",
    "compile": "compilar",
    "execute": "executar"
}

# Função para jogar uma fase
def play_round(word, translation, level):
    attempts = level + 2
    revealed_letters = ['_' for _ in word]
    
    print("\nAdivinhe a palavra em inglês para:", translation)
    
    while attempts > 0:
        print(f"Palavra: {' '.join(revealed_letters)}")
        guess = input("Digite uma letra ou a palavra completa: ").lower()
        
        if guess == word:
            print("Parabéns! Você acertou a palavra inteira!")
            return 1
        elif len(guess) == 1 and guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    revealed_letters[index] = guess
            if '_' not in revealed_letters:
                print(f"Parabéns! Você completou a palavra: {word}")
                return 1
        else:
            attempts -= 1
            print(f"Letra/Palavra incorreta. Tentativas restantes: {attempts}")
            if attempts == level:  # Fornece uma dica quando restarem tentativas iguais ao nível
                print(f"Dica: A palavra começa com '{word[0]}' e termina com '{word[-1]}'.")

    print(f"Você não adivinhou a palavra. A palavra correta era '{word}'.")
    return 0

# Jogo principal
def main():
    total_score = 0
    levels = 5
    
    print("Bem-vindo ao jogo de adivinhação de palavras!")
    
    for level in range(1, levels + 1):
        print(f"\nNível {level}:")
        word, translation = random.choice(list(words.items()))
        total_score += play_round(word, translation, level)
    
    print(f"\nSua pontuação total foi: {total_score} de {levels}")
    print("Obrigado por jogar!")

# Executar o jogo
if __name__ == "__main__":
    main()
