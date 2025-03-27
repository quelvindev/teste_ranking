import random
import pandas as pd
from faker import Faker

Faker.seed(0)
random.seed(0)
fake = Faker("pt_BR")


num_registros = 1000
caminho_arquivo = "../powerbi/dataset/dataset_ficticio.csv"


ids = []
nomes = []
valores_venda = []
valores_devolucao = []
qtd_notas = []
qtd_clientes = []


for i in range(1, num_registros + 1):
    id_code = f"ID{i:05d}"  
    nome = fake.name()
    valor_venda = round(random.uniform(100, 10000), 2) 
    valor_devolucao = round(random.uniform(0, valor_venda * 0.5), 2)  
    notas = random.randint(1, 1000)  
    clientes = random.randint(1, 5000) 

 
    ids.append(id_code)
    nomes.append(nome)
    valores_venda.append(valor_venda)
    valores_devolucao.append(valor_devolucao)
    qtd_notas.append(notas)
    qtd_clientes.append(clientes)


df = pd.DataFrame({
    "ID": ids,
    "Nome": nomes,
    "Valor Venda": valores_venda,
    "Valor Devolução": valores_devolucao,
    "Qtd Notas": qtd_notas,
    "Qtd Clientes": qtd_clientes
})


print(df.head())


df.to_csv(caminho_arquivo, index=False)

