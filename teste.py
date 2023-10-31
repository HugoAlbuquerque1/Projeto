def converterDolares(Real):
    dolar = Real/4.99

    return dolar


print("Conversor de dolares")
Real= float(input("coloque os valores em reais"))
resp = converterDolares(Real)
print(resp)