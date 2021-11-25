import csv
import ast
file = open('bible.csv')
csvreader = csv.reader(file)
total_no_of_chapters=0
# 1189 - chapters
# 3.257 per day
# 31103 - verses
# 85.213 per day
total_no_of_verses_OT = 0
total_no_of_verses_NT = 0
Proverbs = 915
Psalms = 2461
for row in csvreader:
    verse=ast.literal_eval((row[1]))["VERSES"]
    if ast.literal_eval((row[1]))["OT/NT"]=='OT':
        total_no_of_verses_OT+=int(verse)
    else:
        total_no_of_verses_NT+=int(verse)
# Removing Psalms and Proverbs from OT count
total_no_of_verses_OT=total_no_of_verses_OT-Proverbs-Psalms

# print(total_no_of_chapters)
# print(total_no_of_chapters/365)
print("Total number of verses in Old Testament: ",total_no_of_verses_OT)
print("Total number of verses in New Testament: ",total_no_of_verses_NT)
print("Actual total number of verses in bible: ",total_no_of_verses_OT+total_no_of_verses_NT+Psalms+Proverbs)
year=365
per_day_OT=total_no_of_verses_OT/year
per_day_NT=total_no_of_verses_NT/year
per_day_Psalms=Psalms/year
per_day_Proverbs=Proverbs/year
per_day_total_estimated=per_day_Proverbs+per_day_Psalms+per_day_NT+per_day_OT
ap_OT=int(per_day_OT)*365
ap_NT=int(per_day_NT)*365
ap_PR=int(per_day_Proverbs)*365
ap_PS=int(per_day_Psalms)*365
ap_total=ap_PS+ap_PR+ap_OT+ap_NT
excess=ap_total-(total_no_of_verses_OT+total_no_of_verses_NT+Psalms+Proverbs)
# excess=ap_total-31103
print("Old Testament Count per day: ",per_day_OT)
print("New Testament Count per day: ",per_day_NT)
print("Psalms Count per day: ",per_day_Psalms)
print("Proverbs Count per day: ",per_day_Proverbs)
print("Total verses Per day: ",per_day_total_estimated)
print("Approximation")
print("Old Testament Count per day: ",int(per_day_OT))
print("New Testament Count per day: ",int(per_day_NT))
print("Psalms Count per day: ",int(per_day_Psalms))
print("Proverbs Count per day: ",int(per_day_Proverbs))
print("Total verses Per day: ",int(per_day_total_estimated))
print("OT: ",ap_OT)
print("NT: ",ap_NT)
print("PR: ",ap_PR)
print("PS: ",ap_PS)
print("Total: ",ap_total)
print("Excess: ",excess)
print("Excess Missig")
ex_OT=total_no_of_verses_OT-ap_OT
ex_NT=total_no_of_verses_NT-ap_NT
ex_PR=Proverbs-ap_PR
ex_PS=Psalms-ap_PS
ex_total=31103-ap_total
print("missed OT: ",ex_OT)
print("missed NT: ",ex_NT)
print("missed PR: ",ex_PR)
print("missed PS: ",ex_PS)
print("missed Total: ",ex_total)
print("Cross checking")
cr_OT=total_no_of_verses_OT%365
cr_NT=total_no_of_verses_NT%365
cr_PR=Proverbs%365
cr_PS=Psalms%365
cr_total=31103%365
print("Cross Check OT: ",cr_OT)
print("Cross Check NT: ",cr_NT)
print("Cross Check PR: ",cr_PR)
print("Cross Check PS: ",cr_PS)
print("Cross Check Total: ",cr_total)
# excess=ap_total-31103



# as referred from daily bible
# jan 1 - 28+23=51(OT) 17+12=29(NT) + 6 +6 = 92
# 26+23=49(OT) 11+6=17(NT) + 12 + 3 = 81

# Proverbs - 915
# Psalms - 2461
# OT - 19770 ( without Psalms and Proverbs)
# NT - 7957

a=365
b=total_no_of_verses_OT
print(b/a,b//a,b%a)
d={}
r=b%a
for i in range(1,a+1):
    d[i]=b//a
    if r>0:
        d[i]+=1
        r-=1
print(d)