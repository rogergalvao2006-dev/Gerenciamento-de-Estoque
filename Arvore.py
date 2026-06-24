class ArrayList: 
    def __init__(self):
        self.dados = []

    def adicionar(self, elementos):
        self.dados.append(elementos) 

    def tamanho(self):
        return len(self.dados)   
    
    def vazia(self):
        return len(self.dados) == 0 
    
    def pegar(self,posicao):
        if 0 <= posicao < self.tamanho():
            return self.dados[posicao]
        return None
        
    def remover(self,posicao):
        if 0 <= posicao < self.tamanho():
            return self.dados.pop(posicao)
        return None 
  
class No:
    def __init__(self, sku, nome, preco, qtd):
        self.sku = sku
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.esq = None
        self.dir = None

class Estoque:
    def __init__(self):
        self.raiz = None

    def inserir(self, sku, nome, preco, qtd):
        novo = No(sku, nome, preco, qtd)
        if not self.raiz:
            self.raiz = novo
            return
        atual = self.raiz
        while True:
            if sku < atual.sku:
                if atual.esq:
                    atual = atual.esq
                else:
                    atual.esq = novo
                    break
            else:
                if atual.dir:
                    atual = atual.dir
                else:
                    atual.dir = novo
                    break

    def buscar(self, sku):
        atual = self.raiz
        while atual:
            if sku == atual.sku:
                return atual
            elif sku < atual.sku:
                atual = atual.esq
            else:
                atual = atual.dir
        return None

    def remover(self, sku):
        def _remover(no, sku):
            if not no:
                return None
            if sku < no.sku:
                no.esq = _remover(no.esq, sku)
            elif sku > no.sku:
                no.dir = _remover(no.dir, sku)
            else:
                if not no.esq:
                    return no.dir
                if not no.dir:
                    return no.esq
                temp = no.dir
                while temp.esq:
                    temp = temp.esq
                no.sku, no.nome, no.preco, no.qtd = temp.sku, temp.nome, temp.preco, temp.qtd
                no.dir = _remover(no.dir, temp.sku)
            return no
        self.raiz = _remover(self.raiz, sku)

    def listar(self):
        resultado, pilha, atual = [], [], self.raiz
        while pilha or atual:
            while atual:
                pilha.append(atual)
                atual = atual.esq
            atual = pilha.pop()
            resultado.append(f"{atual.sku} - {atual.nome} - R${atual.preco:.2f} - {atual.qtd}un")
            atual = atual.dir
        return resultado

def main():
    estoque = Estoque()
    estoque.inserir(101, "Camiseta", 29.90, 10)
    estoque.inserir(205, "Calca", 89.90, 5)
    estoque.inserir(50, "Bone", 19.90, 15)
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE ESTOQUE")
        print("="*50)
        print("1 - Listar produtos")
        print("2 - Buscar produto")
        print("3 - Adicionar produto")
        print("4 - Remover produto")
        print("5 - Sair")
        print("="*50)
        
        opcao = input("Opcao: ")
        
        if opcao == "1":
            print("\nPRODUTOS:")
            print("-"*40)
            produtos = estoque.listar()
            if produtos:
                for p in produtos:
                    print(p)
            else:
                print("Estoque vazio")
            print("-"*40)
            
        elif opcao == "2":
            try:
                sku = int(input("SKU: "))
                prod = estoque.buscar(sku)
                if prod:
                    print(f"\nSKU: {prod.sku}")
                    print(f"Nome: {prod.nome}")
                    print(f"Preco: R${prod.preco:.2f}")
                    print(f"Qtd: {prod.qtd}")
                else:
                    print("Produto nao encontrado")
            except:
                print("Entrada invalida")
                
        elif opcao == "3":
            try:
                sku = int(input("SKU: "))
                if estoque.buscar(sku):
                    print("SKU ja existe")
                    continue
                nome = input("Nome: ")
                preco = float(input("Preco: "))
                qtd = int(input("Quantidade: "))
                estoque.inserir(sku, nome, preco, qtd)
                print("Produto adicionado")
            except:
                print("Entrada invalida")
                
        elif opcao == "4":
            try:
                print("\nESTOQUE ATUAL:")
                for p in estoque.listar():
                    print(p)
                print("-"*40)
                sku = int(input("SKU para remover: "))
                prod = estoque.buscar(sku)
                if not prod:
                    print("Produto nao encontrado")
                    continue
                print(f"Remover: {prod.nome} - R${prod.preco:.2f}")
                confirm = input("Confirmar? (s/n): ").lower()
                if confirm == "s":
                    estoque.remover(sku)
                    print("Produto removido")
                else:
                    print("Cancelado")
            except:
                print("Entrada invalida")
                
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opcao invalida")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()