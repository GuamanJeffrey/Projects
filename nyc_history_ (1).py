#Name: Jeffrey Guaman
#Email: JEFFREY.GUAMAN18@myhunter.cuny.edu
#Date: October 5th, 2023
#This program gives a graph based on the borough the user wants. 
import matplotlib.pyplot as plt
import pandas as pd
stuff = input("Enter borough name: ")
Output = input("Enter output file name: ")
ny = pd.read_csv('nycHistPop.csv', skiprows = 5)
ny["Fraction"] = ny[stuff] / ny["Total"]
graph = ny.plot.line(x = "Year", y = "Fraction")
fig = plt.gcf()
fig.savefig(Output)
