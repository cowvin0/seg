import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer, IterativeImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('ldw-base_relacionamento_atual.csv', delimiter=';', dtype={'cod_carteira': str})\
    .astype(
        {
            'cod_central': str,
            'cod_coop': str,
            'num_conta_principal': str,
            'cod_ua': str,
            'num_cpf_cnpj': str,
            'cod_cnae': str,
            'ano_mes': str,
            'num_ano_mes': str
        }
    )\
    .assign(
        ultimo_contato=lambda x: pd.to_datetime(x.ultimo_contato),
        faixa_principalidade=lambda x: x.faixa_principalidade.replace('MISSING', np.nan)
    )\
    .query('status_associado == "ATIVO"')\
    .drop(
        columns=[
            'desc_cnae', 'desc_cbo', 'fat_ano',
            'cod_cbo', 'dat_renovacao_cadastral',
            'ultimo_contato', 'nom_gestor_carteira',
            'mc_domicilio', 'mc_cred_moeda', 'mc_seg_elementares',
            'sld_cred_moeda', 'qt_cred_moeda', 'qt_seg_elementares',
            'sld_seg_elementares', 'mc_cred_moeda', 'qt_cred_moeda',
            'sld_cred_sicredi_sas_180_2m', 'qt_seg_agricola',
            'vlr_prej_coobrigacoes', 'vlr_prej_outros', 'mc_seguro_agricola',
            'sld_seg_agricola', 'sld_cred_scr_180_2m', # 'prod_seguro_agricola',
            #'prod_pagto_forn', 'prod_folha_pagamento', 'prod_cambio',
            #'prod_custodia_cheque', 'prod_seguro_rural', 'prod_consorcio_servicos',
            #'prod_lci', 'prod_cred_financ', 'prod_consorcio_pesados', 'prod_desc_reb',
            #'prod_consorcio_motos', 'prod_desc_reb', 'prod_consorcio_motos', 'prod_credito_rural',
            #'prod_cobranca', 'prod_adq', 'prod_seguro_patr', 'prod_consorcio_imoveis',
            #'prod_domicilio', 'prod_seguro_residencial', 'prod_consorcio_automoveis',
            #'prod_seguro_automovel', 'prod_seguro_automovel', 'prod_lca', 'prod_previdencia',
            #'prod_fundos', 'prod_seguro_prestamista', 'prod_debito_conta', 'prod_seguro_vida',
            #'prod_poupanca', 'prod_cheque_especial', 'prod_deposito_a_prazo', 'prod_ctasal'
        ]
    )\
    .dropna(
        subset=[
            'municipio', 'publico_estrategico', 'score_principalidade',
            'renda_mensal', 'nivel_risco', 'faixa_principalidade']
    )\
    .reset_index(drop=True)

colunas = (df.columns[~df.columns.str.contains('prod')].tolist() +
           df.columns[df.columns.isin(['prod_cartao_credito', 'prod_cartao_debito'])].tolist())
df = df[colunas]
df = df\
    .astype(
        {
            col: str
            for col in df.loc[:,df.columns.str.startswith(
                ('prod', 'flg', 'digital',
                 'possui', 'ib', 'mobi', 'fone')
            )].columns
        }
    )

df = df\
    .set_index(
        df.columns[~df.columns.str.startswith('prod')].tolist()
    )\
    .stack()\
    .reset_index()
