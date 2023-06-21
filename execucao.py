class Socio:
    def __init__(self, nome, cpf, data, mes, ano):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = data
        self.mes = mes
        self.ano = ano


class Clube:
    def __init__(self):
        self.socios = []

    def associar(self, Socio):
        self.socios.append(Socio)

    def numero_de_socios(self):
        return len(self.socios)

    def mes_associacao(self, mes, ano):
        if mes not in range(1, 13):
            raise TypeError
        if len(str(ano)) != 4:
            raise ValueError
        soma = 0
        for pessoa in self.socios:
            if pessoa.mes == mes and pessoa.ano == ano:
                soma += 1
        return soma

    def expulsar(self, mes, ano):
        if mes not in range(1, 13):
            raise TypeError
        if len(str(ano)) != 4:
            raise ValueError
        lista1 = []
        lista2 = []
        for pessoa in self.socios:
            if pessoa.mes == mes and pessoa.ano == ano:
                lista1.append(pessoa.nome)
            else:
                lista2.append(pessoa)
        self.socios = lista2
        lista1.sort()
        return lista1
    