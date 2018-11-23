import pandas as pd

def ends_in_csv_extension(name):
    return name[-4:] == ".csv"

def dict_to_csv(dict, csv_name, key_name, value_name):
    if not ends_in_csv_extension(csv_name):
        csv_name += ".csv"

    s = pd.Series(dict, name=value_name)
    s = s.sort_values()
    s.to_csv(csv_name, header=True, index_label=key_name)
