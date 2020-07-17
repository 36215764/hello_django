from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}!</h1>'.format(nome))


def somar(request, num1, num2):
    soma = num1 + num2

    return HttpResponse('<h1>Resultado da Soma:</h1>\n'
                        '<h2>{} + {}</h2>\n'
                        '<h3>O resultado foi: {}</h3>'.format(num1, num2, soma))

def dividir(request, num1, num2):
    try:
        div = num1 / num2
    except ZeroDivisionError:
        return HttpResponse('<h3>Não é possivel divisão por 0</h3>')

    else:
        return HttpResponse('<h1>Resultado da Divisão:</h1>\n'
                            '<h2>{} / {}</h2>\n'
                            '<h3>O resultado foi: {}</h3>'.format(num1, num2, int(div)))

def multiplicar(request, num1, num2):
    mult = num1 * num2

    return HttpResponse('<h1>Resultado da Multiplicação:</h1>\n'
                        '<h2>{} x {}</h2>\n'
                        '<h3>O resultado foi: {}</h3>'.format(num1, num2, mult))

def subtrair(request, num1, num2):
    sub = num1 - num2

    return HttpResponse('<h1>Resultado da Subtração:</h1>\n'
                        '<h2>{} - {}</h2>\n'
                        '<h3>O resultado foi: {}</h3>'.format(num1, num2, sub))