import csv
import ast
from datetime import date,timedelta
from guibible.net import Bible

def calc_verse_count_per_day(b,a=365):
    # print(b / a, b // a, b % a)
    d = {}
    r = b % a
    for i in range(1, a + 1):
        d[i] = b // a
        if r > 0:
            d[i] += 1
            r -= 1
    return d

file = open('bible.csv')
csvreader = csv.reader(file)
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
total_no_of_verses_OT=total_no_of_verses_OT-Proverbs-Psalms
OT_count=calc_verse_count_per_day(total_no_of_verses_OT)
NT_count=calc_verse_count_per_day(total_no_of_verses_NT)
Pr_count=calc_verse_count_per_day(Proverbs)
Ps_count=calc_verse_count_per_day(Psalms)



data={}
today = date.today()
end=date(today.year + 1, today.month, today.day)
difference=int(str(end-today).split()[0])
for i in range(1,difference+1):
    data[i]={}
    data[i]['date']=(today+timedelta(days=i-1)).strftime("%d/%m/%Y")

    data[i]['verses']=[]

# print(data)
print(Pr_count[1],Ps_count[1])
# Calculating the count of messages to send in single text
# 7,4,2,1 are consecutive hours and 3 times an hours
# that is every 20 minutes on 14 hour span on the whole
# say 8 AM to 10 PM as default span
OT_per_text=calc_verse_count_per_day(OT_count[1],7*3)
NT_per_text=calc_verse_count_per_day(NT_count[1],4*3)
Ps_per_text=calc_verse_count_per_day(Ps_count[1],2*3)
Pr_per_text=calc_verse_count_per_day(Pr_count[1],1*3)

# now = datetime.datetime.now()
# now_plus_10 = now + datetime.timedelta(minutes = 10)
# chapter number , verse from, verse till
file = open('bible.csv')
todays_verses={}
todays_verses['OT']=[]
todays_verses['NT']=[]
todays_verses['PS']=[]
todays_verses['PR']=[]
today_OT_limit=OT_count[1]
today_NT_limit=NT_count[1]
today_PR_limit=Pr_count[1]
today_PS_limit=Ps_count[1]
csvreader = csv.reader(file)
sent_so_far=0
for row in csvreader:
    if row[0]=='1':
        print(ast.literal_eval((row[1])))
        print(today_OT_limit)
        sample=Bible(ast.literal_eval((row[1]))["BOOK"],1,1,OT_per_text[1]+sent_so_far)
        check=sample.read()
        todays_verses['OT'].append(check)
    if row[0]=='40':
        print(ast.literal_eval((row[1])))
        sample = Bible(ast.literal_eval((row[1]))["BOOK"], 1, 1, NT_per_text[1] + sent_so_far)
        check = sample.read()
        print("check",check)
        todays_verses['NT'].append(check)
