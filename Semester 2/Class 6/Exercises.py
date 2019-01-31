import csv

row_counter = 0
female_counter = 0

with open("biostats.csv") as csv_file:
    total_ages = 0

    reader = csv.reader(csv_file)
    next(reader)


    for row in reader:

        total_ages += int(row[2])
        row_counter += 1

        if row[1] == "F":

            female_counter += 1

percent_female = female_counter/row_counter
percent_male = 1 - percent_female


avg_age = (total_ages/row_counter)

print(round(avg_age,2))
print("Percentage Male =" + (str(percent_male * 100) + "%"))
print("Percentage Female =" + (str(percent_female * 100)) + "%")
