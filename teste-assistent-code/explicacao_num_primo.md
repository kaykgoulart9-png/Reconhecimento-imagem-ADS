# Explicação da Função is_prime em Python

## Código da Função

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

## Explicação Passo a Passo

1. **Definição da Função**: A função `is_prime(n)` recebe um número inteiro `n` como parâmetro e retorna `True` se o número for primo, ou `False` caso contrário.

2. **Verificação Inicial**: 
   - Se `n` for menor ou igual a 1, a função retorna `False` imediatamente. Isso porque números primos são definidos como maiores que 1.

3. **Loop de Verificação**:
   - O loop `for i in range(2, int(n**0.5) + 1)` itera de 2 até a raiz quadrada de `n` (arredondada para baixo).
   - Para cada `i`, verifica se `n` é divisível por `i` (usando `n % i == 0`).
   - Se encontrar um divisor, retorna `False`, pois o número não é primo.

4. **Retorno Final**:
   - Se nenhum divisor for encontrado no loop, a função retorna `True`, indicando que o número é primo.

## Por que essa Abordagem é Eficiente?

- Verificar apenas até a raiz quadrada de `n` é suficiente porque se `n` tem um divisor maior que sua raiz quadrada, o outro divisor correspondente será menor ou igual à raiz quadrada.
- Isso reduz significativamente o número de verificações necessárias, especialmente para números grandes.

## Exemplos de Uso

- `is_prime(7)` retorna `True` (7 é primo).
- `is_prime(4)` retorna `False` (4 não é primo, pois é divisível por 2).
- `is_prime(1)` retorna `False` (1 não é primo).