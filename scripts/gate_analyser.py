import pandas as pd 
import matplotlib.pyplot as plt

#Reading the CSV Files 
can=pd.read_csv("C:\\code\\Pandas\\GATE-Data-Analysis\\data\\raw\\gate_applicants.csv",index_col=0)
cutoff=pd.read_csv("C:\\code\\Pandas\\GATE-Data-Analysis\\data\\raw\\gate_cutoff.csv",index_col=0)

#Merging Both Read Files
left= can.set_index(["Paper Code",'Paper Name','Year'])
right= cutoff.set_index(["Paper Code",'Paper Name','Year'])
analysed_data= left.join(right,lsuffix=" ",rsuffix=" ",)

#Cleaning Data
analysed_data.drop('Sr No', axis=1, inplace=True)
analysed_data.sort_values(by='Applied')

#Resetting Indec to make Year Accessible
analysed_data_reset = analysed_data.reset_index()

#Plotting Graph
analysed_data_reset.plot(x="Year", y="Applied", kind="bar")

#Saving the graph in Processed directory
plt.title("GATE Applications by Year")
plt.tight_layout()
plt.savefig('C:\\code\\Pandas\\GATE-Data-Analysis\\data\\processed\\applicants_per_year.png')
plt.show()


analysed_data.to_csv("Gate_Analysed(Join4).csv")
print(analysed_data.head())
