def calcular_consumo():
    print("=== Calculadora de Consumo Elétrico ===\n")

    aparelho = input("Digite o nome do aparelho: ")
    potencia = float(input("Digite a potência (em watts): "))
    horas_dia = float(input("Digite o tempo de uso diário (em horas): "))

    consumo_mensal = (potencia * horas_dia * 30) / 1000

    custo_total = consumo_mensal * 0.75

    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo_total:.2f}")

calcular_consumo()