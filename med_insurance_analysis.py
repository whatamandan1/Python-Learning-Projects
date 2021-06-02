import csv

with open('insurance.csv') as xfile:
    fhand = csv.DictReader(xfile)
    lst_by_key = {}
    lst_of_inds = []
    for row in fhand:
        for k, v in row.items():
            try:
                lst_by_key[k].append(v)
            except:
                lst_by_key[k] = [v]
        lst_of_inds.append(row)

# What is the average charge by region?

northeast_charges = []
southeast_charges = []
southwest_charges = []
northwest_charges = []

for row in lst_of_inds:
    if row['region'] == 'northeast':
        northeast_charges.append(round(float(row['charges']), 2))
    elif row['region'] == 'southeast':
        southeast_charges.append(round(float(row['charges']), 2))
    elif row['region'] == 'southwest':
        southwest_charges.append(round(float(row['charges']), 2))
    elif row['region'] == 'northwest':
        northwest_charges.append(round(float(row['charges']), 2))

def average_charge(lst):
    return round(sum(lst) / len(lst), 2)

northeast_ave_charge = round(average_charge(northeast_charges), 2)
southeast_ave_charge = round(average_charge(southeast_charges), 2)
southwest_ave_charge = round(average_charge(southwest_charges), 2)
northwest_ave_charge = round(average_charge(northwest_charges), 2)

print('''
The average charge for the northeast is ${}
The average charge for the southeast is ${}
The average charge for the southwest is ${}
The average charge for the northwest is ${}
'''.format(northeast_ave_charge, southeast_ave_charge, southwest_ave_charge, northwest_ave_charge))



# Do females with children have higher charges than those without?

no_children_charges = []
children_charges = []

for row in lst_of_inds:
    if row['children'] == '0' and row['sex'] == 'female':
        no_children_charges.append(round(float(row['charges']), 2))
    elif row['children'] != '0' and row['sex'] == 'female':
        children_charges.append(round(float(row['charges']), 2))

print('The average charge for females with no children is $'+str(average_charge(no_children_charges))+', from a total of', len(no_children_charges), 'records.')
print('The average charge for females with children is $'+str(average_charge(children_charges))+', from a total of', len(children_charges), 'records.')


# What is the average charge by number of children?

children_zero = []
children_one = []
children_two = []
children_three = []
children_four = []
children_five_plus = []


for row in lst_of_inds:
    if row['children'] == '0':
        children_zero.append(round(float(row['charges']), 2))
    elif row['children'] == '1':
        children_one.append(round(float(row['charges']), 2))
    elif row['children'] == '2':
        children_two.append(round(float(row['charges']), 2))
    elif row['children'] == '3':
        children_three.append(round(float(row['charges']), 2))
    elif row['children'] == '4':
        children_four.append(round(float(row['charges']), 2))
    else:
        children_five_plus.append(round(float(row['charges']), 2))

print('''
The average charge for people with no children is ${}, from a total of {} records.
The average charge for people with 1 child is ${}, from a total of {} records.
The average charge for people with 2 children is ${}, from a total of {} records.
The average charge for people with 3 children is ${}, from a total of {} records.
The average charge for people with 4 children is ${}, from a total of {} records.
The average charge for people with 5+ children is ${}, from a total of {} records.
'''.format(average_charge(children_zero), len(children_zero), average_charge(children_one), len(children_one), average_charge(children_two), len(children_two), average_charge(children_three), len(children_three), average_charge(children_four), len(children_four), average_charge(children_five_plus), len(children_five_plus)))



# Which region has the most smokers?
smokers_by_region = {'northeast': 0, 'southeast': 0, 'southwest': 0, 'northwest': 0}

for row in lst_of_inds:
    if row['region'] == 'northeast' and row['smoker'] == 'yes':
        smokers_by_region['northeast'] += 1
    elif row['region'] == 'southeast' and row['smoker'] == 'yes':
        smokers_by_region['southeast'] += 1
    elif row['region'] == 'southwest' and row['smoker'] == 'yes':
        smokers_by_region['southwest'] += 1
    elif row['region'] == 'northwest' and row['smoker'] == 'yes':
        smokers_by_region['northwest'] += 1

print('The region with the most smokers is', max(smokers_by_region), 'with a total of', smokers_by_region[max(smokers_by_region)], 'smokers.\n')

# What is the average bmi by age group?
bmis = {'18-30': [], '30-40': [], '40-50': [], '50-60': [], '60+': []}

for row in lst_of_inds:
    row['age'] = int(row['age'])
    row['bmi'] = float(row['bmi'])
    if 18 <= row['age'] <= 30:
        bmis['18-30'].append(row['bmi'])
    elif 30 < row['age'] <= 40:
        bmis['30-40'].append(row['bmi'])
    elif 40 < row['age'] <= 50:
        bmis['40-50'].append(row['bmi'])
    elif 50 < row['age'] <= 60:
        bmis['50-60'].append(row['bmi'])
    else:
        bmis['60+'].append(row['bmi'])

for key in bmis.keys():
    bmis[key] = average_charge(bmis[key])

print('The average bmi by age group is as follows: ')
for key, value in bmis.items():
    print(key, value)
print('The age group with the highest average bmi is', max(bmis))
