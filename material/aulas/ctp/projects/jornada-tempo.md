## Desafio: "A Jornada do Tempo"


### Objetivo:

Desenvolver um programa que, dada uma data inicial e uma quantidade de dias, calcule a data final e forneça algumas estatísticas sobre o período.

### Requisitos:

#### Entrada do Usuário:

O usuário deve inserir uma data inicial no formato "DD/MM/AAAA".
O usuário deve inserir uma quantidade de dias.

#### Processamento:

Calcular a data final adicionando a quantidade de dias à data inicial.
Determinar quantos finais de semana (sábados e domingos) estão incluídos nesse período.
Determinar quantos feriados nacionais brasileiros estão incluídos nesse período. (Para simplicidade, considere apenas feriados fixos: 1º de janeiro, 21 de abril, 1º de maio, 7 de setembro, 12 de outubro, 2 de novembro e 25 de dezembro).

#### Saída:

Mostrar a data final.
Mostrar o número de finais de semana.
Mostrar o número de feriados.


### Módulos a serem explorados:

datetime: para manipulação de datas.
calendar: para identificar se um dia é sábado ou domingo.

### Bônus (para usuários avançados):

Permitir que o usuário insira feriados adicionais.
Criar uma interface gráfica simples usando o módulo `tkinter`.


Aqui está uma estrutura básica do programa para começar:

```python
import datetime
import calendar
import csv

def ler_feriados_do_arquivo(arquivo):
    # Ler o arquivo txt e retorna a data dos feriados
    with open(arquivo, 'r') as f:
        feriados = [tuple(map(int, linha.strip().split('/'))) for linha in f.readlines()]
    return feriados

def calcular_data_final(data_inicial, dias):
    # Implementar função que retorna a data final
    return data_inicial + datetime.timedelta(days=dias)

def contar_finais_de_semana(data_inicial, dias):
    # Implementar função que retorna o número de finais de semana
    num_finais_de_semana = 0
    for i in range(dias):
        dia_da_semana = (data_inicial + datetime.timedelta(days=i)).weekday()
        if dia_da_semana == 5 or dia_da_semana == 6:  # 5 é sábado e 6 é domingo
            num_finais_de_semana += 1
    return num_finais_de_semana

def contar_feriados(data_inicial, dias):
    # Implementar função que retorna o número de feriados
    feriados_fixos = [(1, 1), (21, 4), (1, 5), (7, 9), (12, 10), (2, 11), (25, 12)]
    num_feriados = 0
    for i in range(dias):
        dia_atual = data_inicial + datetime.timedelta(days=i)
        if (dia_atual.day, dia_atual.month) in feriados_fixos:
            num_feriados += 1
    return num_feriados

def salvar_resultado_csv(data_inicial, data_final, dias, num_finais_de_semana, num_feriados):
    with open('resultado.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data Inicial", "Data Final", "Dias", "Finais de Semana", "Feriados"])
        writer.writerow([data_inicial.strftime('%d/%m/%Y'), data_final.strftime('%d/%m/%Y'), dias, num_finais_de_semana, num_feriados])


def main():
    data_inicial_str = input("Digite a data inicial (DD/MM/AAAA): ")
    dias = int(input("Digite a quantidade de dias: "))

    # Importa as datas de feriados
    feriados = ler_feriados_do_arquivo('feriados.txt')

    # Converter string de data para objeto datetime.date
    dia, mes, ano = map(int, data_inicial_str.split('/'))
    data_inicial = datetime.date(ano, mes, dia)

    data_final = calcular_data_final(data_inicial, dias)
    num_finais_de_semana = contar_finais_de_semana(data_inicial, dias)
    num_feriados = contar_feriados(data_inicial, dias)

    print(f"Data Final: {data_final.strftime('%d/%m/%Y')}")
    print(f"Número de finais de semana: {num_finais_de_semana}")
    print(f"Número de feriados: {num_feriados}")

    salvar_resultado_csv(data_inicial, data_final, dias, num_finais_de_semana, num_feriados)
    print("Resultado salvo em 'resultado.csv'.")


if __name__ == "__main__":
    main()

```

- `feriados.txt`

```bash
01/01
02/02
03/03
04/04
05/05
06/06
07/07
```

- `resultado.csv`

```bash
Data Inicial,Data Final,Dias, Finais de Semana,Feriados
10/01/2023,20/01/2023,10,2,1

```