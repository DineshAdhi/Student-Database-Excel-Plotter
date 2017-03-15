import dill as pickle
import json
import xlwt

with open('list.pkl','r') as src:
    mylist = pickle.load(src);

print json.dumps(mylist, indent=4, sort_keys=True)


for i in mylist:
    print i

book = xlwt.Workbook(encoding='utf-8')

sheet = book.add_sheet('Sheet 1');

sheet.write(0,0, "Register number");
sheet.write(0,1, "Name");

for i in range(1,9):
    sheet.write(0, i+1, "Sem "+str(i));

sheet.write(0, 10, "Total CGPA");


for index, i in enumerate(mylist):
    sheet.write(index+1, 0, i['reg_no'])
    sheet.write(index+1, 1, i['name'])
    sheet.write(index+1, 2, i['sem-1'])
    sheet.write(index+1, 3, i['sem-2'])
    sheet.write(index+1, 4, i['sem-3'])
    sheet.write(index+1, 5, i['sem-4'])
    sheet.write(index+1, 6, i['sem-5'])
    sheet.write(index+1, 7, i['sem-6'])
    sheet.write(index+1, 8, i['sem-7'])
    sheet.write(index+1, 9, i['sem-8'])
    sheet.write(index+1, 10, i['total_cgpa'])

book.save('diploma.xls')
