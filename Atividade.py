from banco import criar_tabelas
from produto import (
    cadastrar_produto,
    consultar_produtos,
    alterar_produtos,
    excluir_produto,
    registrar_entrada,
    registrar_saida,
    consultar_historico,
    verificar_estoque_minimo,
    consultar_valores_estoque,
    gerar_relatorio

)


def menu():
    while True:
        print("\n" + "=" * 45)
        print("                           CONTROLE DE ESTOQUE")
        print("=" * 45)

        print("1 - Cadastrar produto")
        print("2 - Consultar produtos")
        print("3 - Alterar produto")
        print("4 - Excluir produto")
        print("5 - Registrar entrada")
        print("6 - Registrar saída")
        print("7 - Consultar histórico")
        print("8 - Verificar estoque mínimo")
        print("9 - Consultar valores de estoque")
        print("10 - Relatórios")
        print("0 - Sair")

        opcao = input("\nDigite uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            consultar_produtos()

        elif opcao == "3":
            alterar_produtos()

        elif opcao == "4":
            excluir_produto()

        elif opcao == "5":
            registrar_entrada()


        elif opcao == "6":
            registrar_saida()

        elif opcao == "7":
            consultar_historico()

        elif opcao == "8":
            verificar_estoque_minimo()


        elif opcao == "9":
            consultar_valores_estoque()

        elif opcao == "10":
            gerar_relatorio()

        elif opcao == "0":
           print("\n Programa encerrado.")
           break

        else:
            print("\n Opção inválida. Digite uma opção disponível.")

criar_tabelas()
menu()







