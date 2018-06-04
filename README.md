# Missing_Data_Imputer
## Detect and Replace Missing Values

### Process
1) User manually selects a target csv file via visual file search interface
```Python3
class MissingDataImputer(object):
    
    #Allow User to Select File via tkinter, returns file_path
    def getFilePath(self):
    """Get Name and Location of User's CSV file
        Args:
            None
        Returns:
            File Path of Target CSV.
       """
        root = tk.Tk()
        messagebox.showinfo("Missing Data Imputer", "Click OK to Choose your File.")
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path
```
2) Program builds a Pandas DataFrame from csv file 

```Python3

    def get_file(self, filename):
    """ Extract csv file contents, sep on semi-colon
    Args:
        filename: Path to target CSV
    Returns:
        raw data of csv file
    """
        raw = pd.read_csv(filename, sep=';')
        return raw

    #Convert Raw File to DataFrame
    def make_dataframe(self, filecontents):
        """ Create Pandas DataFrame of raw file contents
        Args:
            filecontents: Raw Contents
        Returns:
            Dataframe of csv file
       """
        dataframe = pd.DataFrame(filecontents)
        return dataframe
```

3) Program inspects rows for missing data 
```Python3
    def check_integrity(self, input_df):
       """  Check if values missing, generate list of cols with NaN indices
        Args:
            filecontents: input_df
        Returns:
            List containing column names containing missing data
       """
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
```
4) Imputes missing numeric values based on interpolation methodology

```Python3
    
    def impute(self, input_df, missing):
       """ Imputes missing values of detected cols with interpolation methodology
        Args:
              input_df : dataframe
              missing  : columns labels associated with missing observations
        Returns:
              dataframe with interpolated values
       """
        for each in missing:
            input_df[each] = input_df[each].interpolate()
        return input_df
```

