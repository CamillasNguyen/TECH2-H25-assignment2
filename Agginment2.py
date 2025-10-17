import pandas as pd
import matplotlib.pyplot as plt

# ----Part 1-----

# Reads file
df = pd.read_csv("SCF_10pct.csv", encoding="latin1")

# filters to ages between 25 and 89
df = df[(df['age'] >= 25) & (df['age'] <= 89)]

# college 3 or 4 = 1, else 0
df["college"] = df["educ"].isin([3, 4]).astype(int)

# networth in 1000s
df["networth"] = df["networth"] / 1000

#Numbers of observations
print(f"Number of observations: {len(df)}")

# ----Part 2 -----


#sort by level, then find average by level
avg = {}

for level in sorted(df["educ"].unique()):
    subset = df[df["educ"] == level]
    avg[level] = subset["networth"].mean()
    print(level, avg[level])


plt.bar(avg.keys(), avg.values())
plt.title("Average by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Average Net Worth")
plt.tight_layout()
plt.show()



#-----PArt 3_-------

avg_year = {}

#finds average by each year
for year in sorted(df["year"].unique()):
    subset = df[df["year"] == year]
    average = subset["networth"].mean()
    avg_year[year] = average

print(avg_year)

plt.plot(avg_year.keys(), avg_year.values(), marker='o')
plt.title("Average Net Worth by Year")
plt.xlabel("Year")
plt.ylabel("Average Net Worth")
plt.show()

#--------_ Part 4 ----------

avg_noncollege = {}
avg_college = {}

# Loop thorught each year
for year in sorted(df["year"].unique()):
    subset = df[df["year"] == year]
    avg_noncollege[year] = subset[subset["college"] == 0]["networth"].mean()
    avg_college[year] = subset[subset["college"] == 1]["networth"].mean()

#Line plot
plt.plot(avg_noncollege.keys(), avg_noncollege.values(), marker='o', label='Non-college')
plt.plot(avg_college.keys(), avg_college.values(), marker='o', label='College')

plt.title("Average networth by status")
plt.xlabel("Survey Year")
plt.ylabel("Average Net Worth")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
