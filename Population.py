#Name: Jeffrey Guaman
#Email: JEFFREY.GUAMAN18@myhunter.cuny.edu
#Date: October 5th, 2023
#This program calculates the average pop and max pop based off the nychistory.csv file info
import pandas as pd
ny = pd.read_csv("nycHistPop.csv", skiprows = 5)
x = input("Enter borough: ")
print("Average population:", ny[x].mean())
print("Maximum population:", ny[x].max())
