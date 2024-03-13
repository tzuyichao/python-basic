import pymssql
from sqlalchemy import create_engine
import pandas as pd
import difflib
import sys
from io import StringIO

def get_data(tableName) -> str:
    engine = create_engine(f"mssql+pymssql://datagov:datagov!@localhost/MDM_CDC?charset=utf8")
    sql = f'SELECT TOP 20000 * FROM dbo.{tableName} ORDER BY EmployeeID'
    df = pd.read_sql_query(sql, engine)
    data = []
    for i in df.values.tolist():
        print(len(i))
        print(i)
        data.append(tuple(str(j).strip().split('.')[0] for j in i))
    output = StringIO()
    df.to_csv(output, header=False, index=False)
    result =  output.getvalue()
    output.close()
    return result

if __name__ == '__main__':
    lh = get_data('Employees_source').splitlines()
    rh = get_data("Employees_diff").splitlines()
    print(repr(lh))
    print(rh)
    diff = difflib.unified_diff(lh, rh, fromfile='before.py', tofile='after.py', lineterm='')
    result = '\n'.join(diff)
    sys.stdout.writelines(result)
    diff_output = result.strip().split("\n")[3:]
    unique_in_before = set()
    unique_in_after = set()
    differences = set()

    observed_pks = {}

    for line in diff_output:
        if line.startswith('-') or line.startswith('+'):
            action = line[0]
            pk = line[1:].split(',')[0]
            
            if pk in observed_pks and observed_pks[pk] != action:
                differences.add(pk)
                unique_in_before.discard(pk)
                unique_in_after.discard(pk)
            else:
                observed_pks[pk] = action
                if action == '-':
                    if pk not in differences:
                        unique_in_before.add(pk)
                else:  # action == '+'
                    if pk not in differences:
                        unique_in_after.add(pk)
        else:
            pk = line.split(',')[0]

    print("Unique in before.py:", unique_in_before)
    print("Unique in after.py:", unique_in_after)
    print("Differences in both:", differences)
