import sqlite3
from datetime import datetime

from banco import conectar

def cadastrar_produto():
    print("\n" + "=" * 45)
    print("                           CADASTRO DE PRODUTO")
    print("=" * 45)

    while True:
        codigo = input("Digite o código do produto: ").strip()

        if codigo == "":
            print("Erro: o código não pode ficar vazio.")

        elif not codigo.isdigit():
            print("Erro: o código deve conter apenas números.")
        else:
            break

    while True:
        nome = input("Digite o nome do produto: ").strip()

        if nome == "":
            print("Erro: o nome não pode ficar vazio.")
        else:
            break


    while True:
        categoria = input("Digite a categoria do produto: ").strip()

        if categoria == "":
            print("Erro: a categoria não pode ficar vazia.")
        else:
           break


    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))

            if quantidade < 0:
                print("Erro: a quantidade não pode ser negativa.")
            else:
                break


        except ValueError:
            print("Erro: digite um valor numérico válido.")




    while True:
        try:
            preco_compra = float(input("Digite o preço de compra: "))
            if preco_compra < 0:
                print("Erro: o preço de compra não pode ser negativo.")
            else:
                break

        except ValueError:
            print("Erro: digite um valor numérico válido. ")



    while True:
        try:
            preco_venda = float(input("Digite o preço de venda: "))
            if preco_venda < 0:
                print("Erro: o preço de venda não pode ser negativo.")
            else:
                break


        except ValueError:
            print("Erro: digite um valor numérico válido.")

    while True:
        try:
            estoque_minimo = int(input("Digite o estoque mínimo: "))
            if estoque_minimo < 0:
                print("Erro: o estoque mínimo não pode ser negativo.")
            else:
                break


        except ValueError:
            print("Erro: digite um número inteiro válido.")

    conexao = conectar()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
           INSERT INTO produtos (
               codigo,
               nome,
               categoria,
               quantidade,
               preco_compra,
               preco_venda,
               estoque_minimo
            )
            VALUES (?,?,?,?,?,?,?) 
               
        """,(

            codigo,
            nome,
            categoria,
            quantidade,
            preco_compra,
            preco_venda,
            estoque_minimo

        ))


        conexao.commit()
        print("\nProduto cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("\nErro: já existe um produto com esse código.")

    finally:
       cursor.close()
       conexao.close()



def consultar_produtos():
    print("\n" + "=" * 45)
    print("                           CONSULTAR PRODUTOS")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor. execute ("""
        SELECT codigo, nome, categoria, quantidade
        FROM produtos
        ORDER BY codigo
        """)


    produtos = cursor.fetchall()

    if not produtos:
        print("O estoque está vazio.")
    else:
        print("\nCódigo | Produto | Categoria | Quantidade ")
        print("-" * 50)

        for produto in produtos:
            codigo, nome, categoria, quantidade = produto

            print(f"{codigo} | {nome} | {categoria} | {quantidade}")

    cursor.close()
    conexao.close()



def alterar_produtos():
    print("\n" + "=" * 45)
    print("                           ALTERAR PRODUTOS")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        codigo = input("Digite o código do produto: ").strip()

        if codigo == "":
            print("Erro: o código não pode ficar vazio.")
            continue


        cursor.execute("""
            SELECT id, nome, categoria,preco_compra, preco_venda, estoque_minimo
            FROM produtos 
            WHERE codigo = ?
            """, (codigo,))
        produto = cursor.fetchone()

        if produto is None:
            print ("Erro: produto não encontrar.")
        else:
            break

    produto_id, nome, categoria,preco_compra, preco_venda, estoque_minimo = produto

    print("\nProduto cadastrado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Categoria: {categoria}")
    print(f"preço compra: R$ {preco_compra:.2f}")
    print(f"Preço venda:  R$ {preco_venda:.2f}")
    print(f"Estoque minimo: {estoque_minimo}")


    while True:
        print("\n O que deseja alterar ?")
        print("1 - Nome")
        print("2 - Categoria")
        print("3 - Preço compra")
        print("4 - Preço venda")
        print("5 - Estoque minimo")
        print("6 - Cancelar")

        opcao = input("Digite uma opção").strip()
        if opcao == "1":

            while True:
                novo_nome = input("Digite o novo nome: ").strip()
                if novo_nome == "":
                    print("Erro: o nome não pode ficar vazio.")

                else:
                    break


            cursor.execute("""
                UPDATE produtos
                SET nome = ?
                WHERE id = ?
            """, (novo_nome, produto_id))


            conexao.commit()
            print("\n Nome alterado com sucesso!")
            break

        elif opcao == "2":
            while True:
                nova_categoria = input("Digite a nova categoria: ").strip()

                if nova_categoria == "":
                    print ("Erro: a categoria não pode ficar vazia. ")
                else:
                    break

            cursor.execute("""
                UPDATE produtos
                SET categoria = ?
                WHERE id = ?
            """, (nova_categoria, produto_id))


            conexao.commit()
            print("\n categoria alterada com sucesso!")
            break

        elif opcao == "3":
            while True:
                try:
                    novo_preco_compra = float(input("Digite o novo preço de compra: "))

                    if novo_preco_compra < 0:
                        print("Erro: o preço não pode ser negativo.")
                    else:
                        break


                except ValueError:
                    print("Erro: digite um valor numérico válido.")


            cursor.execute("""
                UPDATE produtos
                SET preco_compra = ?
                WHERE id = ?
            """, (novo_preco_compra, produto_id))

            conexao.commit()
            print("\n Preço de compra alterada com sucesso!")
            break

        elif opcao == "4":
            while True:
                try:
                    novo_preco_venda = float(input("Digite o novo preço de venda: "))

                    if novo_preco_venda < 0:
                        print("Erro: o preço não pode ser negativo.")
                    else:
                        break


                except ValueError:
                    print("Erro: digite um valor numérico válido.")

            cursor.execute("""
                           UPDATE produtos
                           SET preco_venda = ?
                           WHERE id = ?
                       """, (novo_preco_venda, produto_id))

            conexao.commit()
            print("\n Preço de venda alterada com sucesso!")
            break


        elif opcao == "5":
            while True:
                try:
                    novo_estoque_minimo= int(input("Digite o novo estoque minimo: "))

                    if novo_estoque_minimo < 0:
                        print("Erro: o estoque minimo não pode ser negativo.")
                    else:
                        break


                except ValueError:
                    print("Erro: digite um valor numérico inteiro válido.")

            cursor.execute("""
                           UPDATE produtos
                           SET estoque_minimo= ?
                           WHERE id = ?
                       """, (novo_estoque_minimo, produto_id))

            conexao.commit()
            print("\n Estoque mínimo alterado com sucesso!")
            break

        elif opcao == "6":
            print("\n  Operação cancelada.")
            break


        else:
            print("erro: opção inválida.")


    cursor.close()
    conexao.close()


def excluir_produto():
    print("\n" + "=" * 45)
    print("                           EXCLUIR PRODUTO")
    print("=" * 45)


    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        codigo = input ("Digite o código do produto: ")

        if not codigo:
            print("O codígo não pode ficar vazio.")
            continue

        cursor.execute("""
            SELECT id,codigo, nome, categoria, quantidade  
            from produtos
            WHERE codigo = ?
        """, (codigo,))

        produto = cursor.fetchone()

        if not produto :
            print("produto não encontrado.")
            continue

        break


    produto_id, codigo, nome, categoria, quantidade = produto

    print("\n Produto encontrado:")
    print(f"Código: {codigo}")
    print(f"Nome: {nome}")
    print(f"Categoria: {categoria}")
    print(f"Quantidade: {quantidade}")


    while True:
        confirmacao = input("\n Deseja realmente excluir este produto ? (S/N): ").strip().upper()
        if confirmacao == "S":
            break
        elif confirmacao == "N":
            print("\n Exclusão cancelada.")
            cursor.close()
            conexao.close()
            return
        else:
            print("Opção inválida. Digite S para sim ou N para não.")

    cursor.execute("""
        SELECT id
        FROM movimentacoes
        WHERE produto_id = ?
    """, (produto_id,))

    movimentacao = cursor.fetchone()

    if movimentacao:
        print("Não é possivel excluir este produto, pois ele possui movimentações.")

    else:
        cursor.execute("""
            DELETE FROM produtos
            WHERE id = ?
        """, (produto_id,))

        conexao.commit()
        print("Produto excluido com sucesso.")

    cursor.close()
    conexao.close()


def registrar_entrada():
    print("\n" + "=" * 45)
    print("                           REGISTRAR ENTRADA")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        codigo = input("Digite o código do produto: ").strip()

        if not codigo:
            print ("O código não pode ficar vazio.")
            continue

        cursor.execute("""
            SELECT id, nome, quantidade
            FROM produtos
            where codigo = ?
         """, (codigo,))

        produto = cursor.fetchone()

        if not produto:
            print("Produto não encontrado.")
            continue

        break


    produto_id, nome, quantidade_atual = produto
    print(f"\n Produto : {nome}")
    print(f"Quantidade atual: {quantidade_atual}")


    while True:
        try:
            quantidade_entrada = int(input("Digite a quantidade do produto: "))

            if quantidade_entrada  <= 0:
                print("A quantidade deve ser maior que zero.")
                continue

            break

        except ValueError:
            print("Digite uma quantidade válida.")


    nova_quantidade = quantidade_atual + quantidade_entrada

    cursor.execute("""
        UPDATE produtos
        SET quantidade = ?
        WHERE id = ?
    """, (nova_quantidade, produto_id))

    data = datetime.now().strftime("%m/%d/%Y %H:%M:%S")


    cursor.execute("""
        INSERT INTO movimentacoes (produto_id, tipo,  quantidade, data)
        VALUES (?, 'ENTRADA', ?, ?)
    """, (produto_id,quantidade_entrada, data))


    conexao.commit()


    print("\n Entrada registrada com sucesso!")
    print(f"Quantidade adicionada:  {quantidade_entrada}")
    print(f"Novo estoque: {nova_quantidade}")

    cursor.close()
    conexao.close()




def registrar_saida():
    print("\n" + "=" * 45)
    print("                           REGISTRAR SAIDA")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()

    while True:
        codigo = input("Digite o codigo do produto: ").strip()

        if not codigo:
            print("O codigo não pode ficar vazio.")
            continue


        cursor.execute("""
            SELECT id, nome, quantidade
            FROM produtos
            where codigo = ?
        """, (codigo,))

        produto = cursor.fetchone()

        if not produto:
            print("Produto não encontrado.")
            continue

        break
    produto_id, nome, quantidade_atual = produto

    print(f"\n Produto : {nome}")
    print(f"Quantidade atual: {quantidade_atual}")

    while True:
        try:
            quantidade_saida = int(input("Digite a quantidade de saida: "))

            if quantidade_saida <= 0:
                print("A quantidade deve ser maior que zero.")
                continue


            if quantidade_saida > quantidade_atual:
                print("Quantidade insuficiente em estoque.")
                print(f"Estoque disponivel: {quantidade_atual}")
                continue

            break

        except ValueError:
            print("Digite uma quantidade válida.")

    nova_quantidade = quantidade_atual - quantidade_saida

    cursor.execute("""
        UPDATE produtos
        set quantidade = ?
        WHERE id = ?
    """, (nova_quantidade, produto_id))

    data = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    cursor.execute("""
        INSERT INTO movimentacoes (produto_id, tipo,  quantidade, data)
        VALUES (?, 'SAIDA', ?, ?)
    """, (produto_id, quantidade_saida, data))

    conexao.commit()

    print("\n Saída registrada com sucesso!")
    print(f"Quantidade retirada: {quantidade_saida}")
    print(f"Novo estoque: {nova_quantidade}")

    cursor.close()
    conexao.close()


def consultar_historico():
    print("\n" + "=" * 45)
    print("                           HISTORICO DE MOVIMENTAÇÔES")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT 
            movimentacoes.data,
            produtos.nome,
            movimentacoes.tipo,
            movimentacoes.quantidade
        FROM movimentacoes
        JOIN produtos
            ON movimentacoes.produto_id = produtos.id 
        ORDER BY movimentacoes.data
        """)

    movimentacoes = cursor.fetchall()

    if not movimentacoes:
        print("\n NEnhuma movimentação registrada.")

    else:
        print("\n Data | Produto | Tipo | Quantidade")
        print("-" * 70)


        for movimentacao in movimentacoes:
            data, nome, tipo, quantidade = movimentacao

            print(f"{data} | {nome} | {tipo} | {quantidade}")



    cursor.close()
    conexao.close()


def verificar_estoque_minimo():
    print("\n" + "=" * 45)
    print("                           VERIFICAR ESTOQUE MINIMO")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT codigo, nome, quantidade, estoque_minimo
        FROM produtos
        WHERE quantidade <= estoque_minimo
        ORDER BY quantidade
    """)


    produtos = cursor.fetchall()

    if not produtos:
        print("\n Nenhum produto precisa de reposição.")

    else:
        print("\n Produtos que precisam de reposição.")
        print("\n Codigo | Produto  | Estoque  | minimo .")
        print("-" * 45)


        for produto in produtos:
            codigo, nome, quantidade, estoque_minimo = produto

            print (f"{codigo} | {nome} | {quantidade} | {estoque_minimo}")

    cursor.close()
    conexao.close()


def consultar_valores_estoque ():
    print("\n" + "=" * 45)
    print("                           VALORES ESTOQUE")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome, quantidade, preco_compra
        FROM produtos
        ORDER BY nome
    """)

    produtos = cursor.fetchall()

    if not produtos:
        print("\n O estoque está vazio.")

    else:
        print("\n Produto | Quantidade | Preço de compra  | Valor em estoque")
        print("-" * 45)

        valor_total = 0

        for produto in produtos:
            nome, quantidade, preco_compra = produto

            valor_estoque = quantidade * preco_compra
            valor_total += valor_estoque

            print(
                f"{nome} | {quantidade} | "
                f"R$ {preco_compra:.2f} | "
                f"R$ {valor_estoque:.2f}"
            )

        print("-" * 65)
        print(f"Valor total: R$ {valor_total:.2f}")

    cursor.close()
    conexao.close()



def gerar_relatorio():
    print("\n" + "=" * 45)
    print("                           RELATORIO GERAL DO ESTOQUE")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()


    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(quantidade), 0),
            COALESCE(SUM(
                CASE
                    WHEN quantidade <= estoque_minimo THEN 1
                    ELSE 0
                END 
            ),0),
            COALESCE(SUM(quantidade * preco_compra), 0)
        FROM produtos
    """)

    total_produtos, total_itens, produtos_baixo_estoque, valor_total = cursor.fetchone()


    cursor.execute("""
       SELECT
           COALESCE(SUM(CASE WHEN tipo = 'ENTRADA' THEN 1 ELSE 0 END), 0),
           COALESCE(SUM(CASE WHEN tipo = 'SAIDA' THEN 1 ELSE 0 END), 0)
       FROM movimentacoes
    """)



    total_entradas, total_saida = cursor.fetchone()

    print("\n PRODUTOS")
    print(f"Total de produtos cadastrados: {total_produtos}")
    print(f"Quantidade total de itens em estoque: {total_itens}")

    print("\n ESTOQUE")
    print(f"Produtos abaixo do estoque mínimo: {produtos_baixo_estoque}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    print("\n MOVIMENTAÇÔES")
    print(f"Total de entradas: {total_entradas}")
    print(f"Total de saídas: {total_saida}")


    cursor.close()
    conexao.close()









       




















