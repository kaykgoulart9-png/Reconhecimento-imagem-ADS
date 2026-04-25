# Erros em `debug.py` e correções aplicadas

## 1. Erro de sintaxe no prompt do `input`
- Linha com `item1 = float(input(Preço do item 1? ))` está sem aspas na mensagem.
- Causa: em Python, as strings do prompt devem estar entre aspas. Sem aspas, o interpretador tenta ler `Preço` como nome de variável.
- Correção aplicada: `item1 = float(input("Preço do item 1? "))`

## 2. Tipo errado para o valor do cupom
- A variável `desconto_cupom` estava sendo definida como string:
  ```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
  ```
- Causa: `input()` retorna uma string, e `desconto_cupom / 100` não funciona para strings.
- Correção aplicada: converter para `float` antes do cálculo:
  ```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
  ```

## 3. Impressão incorreta do valor do item 2
- A linha `print(" Item 2:        R$ {total_item2:.2f}")` não usa `f-string`.
- Causa: isso imprime literalmente `{total_item2:.2f}` em vez do valor.
- Correção aplicada: `print(f" Item 2:        R$ {total_item2:.2f}")`

## 4. Indentação incorreta no bloco `if`
- O `print` após `if desconto_cupom > 0:` não estava indentado.
- Causa: em Python, o conteúdo de um `if` deve estar recuado para indicar que faz parte do bloco.
- Correção aplicada:
  ```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
  ```

## Código corrigido

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

## Observação
- Com essas correções, `debug.py` está funcional e exibe os valores corretamente.
- Caso queira, posso também adicionar tratamento de erros para entradas inválidas (como texto no lugar de número).