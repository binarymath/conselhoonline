import pandas as pd
from mapao import tratar_dataframe

def test_tratar_dataframe_remove_percentual_e_converte_para_float():
    df = pd.DataFrame({
        'Aluno': ['João', 'Maria'],
        'Situação': ['Ativo', 'Ativo'],
        'Frequência total em (%)': ['95%', '80%'],
        'Frequência anterior em (%)': ['90%', '85%'],
        'Média em Matemática': ['7', '8'],
    })

    df_tratado = tratar_dataframe(df)

    assert df_tratado['Frequência total em (%)'].tolist() == [95.0, 80.0]
    assert df_tratado['Frequência anterior em (%)'].tolist() == [90.0, 85.0]
    assert df_tratado['Média em Matemática'].dtype == float

    colunas_esperadas = {
        'Aluno', 'Situação', 'Frequência total em (%)',
        'Frequência anterior em (%)', 'Média em Matemática'
    }
    assert colunas_esperadas.issubset(df_tratado.columns)
