import urllib.parse

nome = "Focinho Limpo"
endereco = "Rua das Acácias, 128, Jardim Primavera"
horarios =
email = "contato@focinholimpo.example"
instagram = "@focinholimpo.pet"
servicos = ["banho: a partir de R$ 50,00",
            "banho e tosa: a partir de R$ 80,00",
            "tosa higiênica: a partir de R$ 35,00",
            "corte de unhas(avulso): a partir de R$ 15,00",
            "hidratacao(extra): a partir de R$ 25,00"]
combinacao_com_hidratacao = ["banho + hidratacao: a partir de R$ 75,00",
                            "banho + tosa + hidratacao: a partir de R$ 105,00"]

def link_whatsapp(mensagem):
    mensagem_codificada = urllib.parse.quote(mensagem)
    return f"https://wa.me/NUMERO?text={mensagem_codificada}"
