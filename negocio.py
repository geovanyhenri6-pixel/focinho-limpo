import urllib.parse

nome = "Focinho Limpo"

endereco = "Rua das Acácias, 128, Jardim Primavera"

#horarios =

email = "contato@focinholimpo.example"

instagram = "@focinholimpo.pet"

servicos = [
"banho: Shampoo e condicionador adequados ao tipo de pelo, secagem com calma e limpeza externa dos ouvidos. Inlcui corte de unhas. A partir de R$50,00",
"banho e tosa: O banho completo e a tosa do jeito que você preferir: na máquina, na tesoura ou no padrão da raça. Inclui o corte de unhas. A partir de R$ 80,00",
"tosa higiênica: Aparamos o pelo das áreas de higiene, das patinhas e da barriga, para o dia a dia ficar mais confortável. Não inclui banho. A partir de R$ 35,00",
"corte de unhas(avulso): Rápido e sem estresse, também para quem quer só as unhas. Já está inclusp no banho e banho + tosa. A partir de R$ 15,00",
"hidratação(extra): Máscara hidratante que deixa o pelo macio e brilhante. Só pode ser somada ao banho ou ao banho + tosa, apenas para cãos. A partir de R$ 25,00"
]

combinacao_com_hidratacao = [
"banho + hidratacao: a partir de R$ 75,00",
"banho + tosa + hidratacao: a partir de R$ 105,00"
]

def link_whatsapp(mensagem):
    mensagem_codificada = urllib.parse.quote(mensagem)
    return f"https://wa.me/NUMERO?text={mensagem_codificada}"
