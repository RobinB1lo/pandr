import os
import csv 

class Get:
    def get_data(data_dir: str) -> dict[str, int] : 
        csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

        population_dict = {}
        rent_dict = {}

        for filename in csv_files:
            full_path = os.path.join(data_dir, filename)
            with open(full_path, newline='', encoding='utf-8') as fp:
                reader = csv.reader(fp)
                header = next(reader) 
                for row in reader:
                    if row[len(row) - 1] == 'Total Population':
                        if 2001 <= int(row[3]) <= 2022:
                            population_dict[row[3]] = int(row[7])
                    elif row[0].find('October') == 5:
                        curr_year = row[0].split()[0]
                        if 2001 <= int(curr_year) <= 2022:
                            rent_dict[curr_year] = int(row[3].replace(",", ""))
        return population_dict, rent_dict