def receber_gabarito():
    print("Digite o gabarito")
    for i in range(quant_questoes):
        while True:
                resposta = input("Questão %d: " % (i + 1)).upper()
                if resposta in ("A","B","C","D","E"):
                    gabarito.append(resposta)
                    break
                else:
                    print("Resposta inválida. Digite apenas A,B,C,D,E.")
    print("Respostas do gabarito: ", gabarito)
def receber_respostas():
    n_alunos = int(input("Número de alunos da turma: "))
    for i in range(n_alunos):
        numero_do_aluno = int(input("Digite o número do(a) %dº aluno(a): " % (i + 1)))
        acertos = 0
        respostas = list(range(quant_questoes))
        for j in range(quant_questoes):
            while True:
                resposta = input("Digite a resposta da questão %d: " % (j + 1)).upper()
                if resposta in ("A","B","C","D","E"):
                    respostas[j] = resposta
                    break
                else:
                    print("Resposta inválida. Digite apenas A,B,C,D,E.")
            if respostas[j] == gabarito[j]:
                acertos += 1
        print("\n",gabarito)
        print("\n",respostas)
        print("O aluno de número %d teve %d acerto(s)." % (numero_do_aluno, acertos))

quant_questoes = 3
gabarito = []
respostas = []
receber_gabarito()
receber_respostas()
