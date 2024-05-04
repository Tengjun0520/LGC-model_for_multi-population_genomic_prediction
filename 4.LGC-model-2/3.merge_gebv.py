import pandas as pd

df = pd.read_csv('TA.lgc.sln', sep='\s+')
df_idox = pd.read_csv('../0.example_data/OX.fam', header=None, sep='\s+')
df_iduc = pd.read_csv('../0.example_data/UC.fam', header=None, sep='\s+')

##TA.OX
df_pop1 = df[(df['type']==3) & (df['traitNo']==1)]
df_pop1_merge = pd.DataFrame(columns=['id', 'gebv1', 'gebv2', 'gebv3', 'gebv_merge'])
df_pop1_merge['id'] = df_pop1[(df_pop1['traitNo']==1) & (df_pop1['term']=='1')]['levels']
df_pop1_merge['gebv1'] = df_pop1[(df_pop1['traitNo']==1) & (df_pop1['term']=='1')]['effect'].values
df_pop1_merge['gebv2'] = df_pop1[(df_pop1['traitNo']==1) & (df_pop1['term']=='2')]['effect'].values
df_pop1_merge['gebv3'] = df_pop1[(df_pop1['traitNo']==1) & (df_pop1['term']=='3')]['effect'].values
df_pop1_merge['gebv_merge'] = df_pop1_merge['gebv1'] + df_pop1_merge['gebv2'] + df_pop1_merge['gebv3']
df_pop1_merge = df_pop1_merge[df_pop1_merge['id'].apply(lambda x: x in df_idox[1].values)]
df_pop1_merge.to_csv('TA.OX.gebv', index=None, sep='\t')

##TA.UC
df_pop2 = df[(df['type']==3) & (df['traitNo']==2)]
df_pop2_merge = pd.DataFrame(columns=['id', 'gebv1', 'gebv2', 'gebv3', 'gebv_merge'])
df_pop2_merge['id'] = df_pop2[(df_pop2['traitNo']==2) & (df_pop2['term']=='1')]['levels']
df_pop2_merge['gebv1'] = df_pop2[(df_pop2['traitNo']==2) & (df_pop2['term']=='1')]['effect'].values
df_pop2_merge['gebv2'] = df_pop2[(df_pop2['traitNo']==2) & (df_pop2['term']=='2')]['effect'].values
df_pop2_merge['gebv3'] = df_pop2[(df_pop2['traitNo']==2) & (df_pop2['term']=='3')]['effect'].values
df_pop2_merge['gebv_merge'] = df_pop2_merge['gebv1'] + df_pop2_merge['gebv2'] + df_pop2_merge['gebv3']
df_pop2_merge = df_pop2_merge[df_pop2_merge['id'].apply(lambda x: x in df_iduc[1].values)]
df_pop2_merge.to_csv('TA.UC.gebv', index=None, sep='\t')