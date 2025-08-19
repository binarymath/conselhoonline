import pandas as pd

def tratar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Limpa colunas de porcentagem e converte dados numéricos."""
    # Filtra apenas registros com situação 'Ativo', se a coluna existir
    if "Situação" in df.columns:
        df = df[df["Situação"] == "Ativo"].copy()

    # Colunas que representam texto e não devem ser convertidas
    colunas_texto = ["Aluno", "Situação"]
    colunas_numericas = [col for col in df.columns if col not in colunas_texto]

    # Remove símbolo de porcentagem e converte para float
    for coluna in ["Frequência total em (%)", "Frequência anterior em (%)"]:
        if coluna in df.columns:
            df[coluna] = df[coluna].astype(str).str.replace("%", "", regex=False)

    # Converte todas as demais colunas numéricas
    df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors="coerce")

    return df
