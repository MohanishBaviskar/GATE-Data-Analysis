import pandas as pd 

can=pd.read_csv("gate_applicants.csv",index_col=0)
cutoff=pd.read_csv("gate_cutoff.csv",index_col=0)

left= can.set_index(["Paper Code",'Paper Name','Year'])
right= cutoff.set_index(["Paper Code",'Paper Name','Year'])

analysed_data= left.join(right,lsuffix=" ",rsuffix=" ",)
analysed_data.drop('Sr No', axis=1, inplace=True)
analysed_data.sort_values(by='Applied')
analysed_data.to_csv("Gate_Analysed(Join4).csv")
print(analysed_data.head())

# analyse_data= pd.concat([can,cutoff])
# analyse_data.groupby(['Paper Code','Year'])
# analyse_data.GEN.fillna("Not Known")
# analyse_data.OBC.fillna("Not Known")
# analyse_data['SC/ST'].fillna("Not Known")
# analyse_data.to_csv("Gate_Analysis.csv")