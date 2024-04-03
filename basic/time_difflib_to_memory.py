from sqlalchemy import create_engine
import timeit
import difflib
import sys
from time_query_to_memory import get_data

def diff(lh, rh) -> str:
    diff = difflib.unified_diff(lh, rh, fromfile='source', tofile='sink', lineterm='', n=0)
    result = '\n'.join(diff)
    return result

def parse(result: str, pk_columns: set) -> tuple:
    pk_len = len(pk_columns)
    diff_output = result.strip().split("\n")[3:]
    unique_in_before = set()
    unique_in_after = set()
    differences = set()

    observed_pks = dict()

    for line in diff_output:
        if line.startswith('@@'):
            continue
        if line.startswith('-') or line.startswith('+'):
            action = line[0]
            pk = ','.join(line[1:].split(',')[0:pk_len])
            
            if pk in observed_pks.keys() and observed_pks[pk] != action:
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
            pk = ','.join(line.split(',')[0:pk_len])

    print("Unique in before.py:", unique_in_before)
    print("Unique in after.py:", unique_in_after)
    print("Differences in both:", differences)
    return unique_in_before, unique_in_after, differences

if __name__ == '__main__':
    engineMDM = create_engine(f"mssql+pymssql://datagov:datagov@localhost/MDM?charset=utf8")
    engineMDMCDC = create_engine(f"mssql+pymssql://datagov:datagov@localhost/MDM_CDC?charset=utf8")
    schema = 'dbo'
    tableName = 'MDM_CUSTOMER_MASTER'
    lh_data, pk_columns = get_data(engine=engineMDM, schema=schema, tableName=tableName)
    rh_data, _ = get_data(engine=engineMDMCDC, schema=schema, tableName=tableName)
    lh = lh_data.splitlines()
    rh = rh_data.splitlines()
    execution_time = timeit.timeit(lambda: diff(lh, rh), number=1)
    print()
    print(f"Function diff {tableName} executed in {execution_time} seconds.")
    res = diff(lh, rh)
    sys.stdout.writelines(res)
    print()
    unique_in_source, unique_in_sink, differences = parse(res, pk_columns)

