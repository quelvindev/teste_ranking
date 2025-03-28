import random
import pandas as pd
from faker import Faker

Faker.seed(0)
random.seed(0)
fake = Faker("pt_BR")


num_registros = 1000
caminho_arquivo = "../powerbi/dataset/dataset_ficticio.csv"


id = []
nome = []
valor_venda = []
valor_devolucao = []
qtd_nota = []
qtd_cliente = []


for i in range(1, num_registros + 1):
    id_code = f"ID{i:05d}"  
    nome = fake.name()
    valor_venda = round(random.uniform(100, 10000), 2) 
    valor_devolucao = round(random.uniform(0, valor_venda * 0.5), 2)  
    notas = random.randint(1, 1000)  
    clientes = random.randint(1, 5000) 

 
    id.append(id_code)
    nome.append(nome)
    valor_venda.append(valor_venda)
    valor_devolucao.append(valor_devolucao)
    qtd_nota.append(notas)
    qtd_cliente.append(clientes)


df = pd.DataFrame({
    "ID": id,
    "Nome": nome,
    "Valor Venda": valor_venda,
    "Valor Devolução": valor_devolucao,
    "Qtd Notas": qtd_nota,
    "Qtd Clientes": qtd_cliente
})


print(df.head())


df.to_csv(caminho_arquivo, index=False)

