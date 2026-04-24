# Explicação da Função is_prime em Python

## Código da Função

```python
def is_prime(number: int) -> bool:
    """Verifica se um número inteiro é primo."""
    if number <= 1:
        return False

    max_divisor = int(number**0.5)
    return all(number % divisor != 0 for divisor in range(2, max_divisor + 1))


if __name__ == "__main__":
    import sys

    try:
        value = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Uso: python num_primos.py <numero>")
    else:
        print(is_prime(value))
```

## Explicação Passo a Passo

1. **Definição da Função**: A função `is_prime(number: int) -> bool` aceita um número inteiro e devolve `True` se ele for primo, ou `False` caso contrário.

2. **Verificação Inicial**:
   - Se o valor for menor ou igual a 1, a função retorna `False` imediatamente, já que apenas inteiros maiores que 1 podem ser primos.

3. **Limite de Verificação**:
   - A variável `max_divisor` recebe a parte inteira da raiz quadrada de `number`.
   - Isso reduz a quantidade de divisões necessárias, pois divisores aparecem em pares e não é preciso verificar além da raiz quadrada.

4. **Verificação com Expressão Generator**:
   - A expressão `all(number % divisor != 0 for divisor in range(2, max_divisor + 1))` verifica se nenhum divisor válido divide `number` sem resto.
   - Se houver algum divisor, a função retorna `False`; caso contrário, retorna `True`.

5. **Execução Direta**:
   - O bloco `if __name__ == "__main__"` permite executar o arquivo diretamente no terminal.
   - Ele recebe um argumento de linha de comando e imprime o resultado da função.

## Por que esse Código está no padrão Clean Code?

- Usa nomes de variáveis claros e descritivos: `number`, `max_divisor`, `divisor`.
- Inclui uma docstring curta explicando o propósito da função.
- Evita loops e condições redundantes com uma expressão `all(...)` simples.
- Separa a lógica da função da parte de entrada/saída no bloco principal.

## Exemplos de Uso

- `python num_primos.py 7` imprime `True`.
- `python num_primos.py 4` imprime `False`.
- `python num_primos.py 1` imprime `False`.
