import pandas as pd


#Load File
def get_file(filename):
    raw = pd.read_csv(filename, sep=';')
    return raw

#Convert Raw File to DataFrame
def make_dataframe(filecontents):
    dataframe = pd.DataFrame(filecontents)
    return dataframe

#Check if values missing, generate list of cols with NaN indices 
def check_integrity(input_df):
    if input_df.isnull:
        print("Detected Missing Data\nSums:")
        num_rows = len(input_df.index)
        affected_cols = [col for col in input_df.columns if input_df[col].isnull().any()]
        missing_list = []
        for each_col in affected_cols:
            missing_list.append(each_col)
        print(missing_list)
        return missing_list
    else:
        print("No Missing Data Was Detected.")

#Imputes missing values of detected cols with interpolation methodology
def impute(input_df, missing):
    for each in missing:
        input_df[each] = input_df[each].interpolate()
    return input_df

if __name__ == "__main__":
file = get_file(your_file_path)
df = make_dataframe(file)
missing_list = check_integrity(df)
clean_df = impute(df, missing_list)
check_integrity(clean_df)
