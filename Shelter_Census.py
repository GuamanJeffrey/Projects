#Name: Jeffrey Guaman
#Email: JEFFREY.GUAMAN18@myhunter.cuny.edu
#Date: October 16th, 2023
#This program calculates a fraction of children over total number of individuals. 
import pandas as pd
import matplotlib.pyplot as plt

message = input("Enter name of input file: ")
message1 = input("Enter name of output file: ")

pop = pd.read_csv(message)

pop["Fraction Children"] = pop["Total Children in Shelter"] / pop["Total Individuals in Shelter"]
s = pop.plot.line(x = "Date of Census", y = "Fraction Children")
fig = plt.gcf()
fig.savefig(message1)
