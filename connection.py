from sqlalchemy import create_engine
import pandas as pd

# Crie o DataFrame
df = pd.DataFrame({
    'nome': ['João', 'Maria', 'Pedro'],
    'idade': [23, 78, 22],
    'cidade': ['Rio de Janeiro', 'São Paulo', 'Salvador']
})

# Crie a conexão com o banco de dados
engine = create_engine('postgresql://lagoaviva:l4g04uff@db.cid-uff.net:5432/lagoaviva')

# Exporte o DataFrame para uma tabela no banco de dados
df.to_sql('nome_da_tabela', engine, if_exists='replace', index=False)