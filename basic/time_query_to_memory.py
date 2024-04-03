from sqlalchemy import create_engine, inspect
import timeit
import pandas as pd
from io import StringIO

def genertate_query(inspector, schema: str, tableName: str) -> tuple:
    pk_constraint = inspector.get_pk_constraint(tableName, schema)
    pk_columns = pk_constraint['constrained_columns']

    all_columns = [col['name'] for col in inspector.get_columns(tableName, schema)]

    for pk in pk_columns:
        all_columns.remove(pk)

    select_columns = pk_columns + all_columns

    select_statement = "SELECT " + ", ".join(select_columns) + f" FROM {schema}.{tableName}"

    return select_statement, pk_columns

def get_data(engine, schema: str, tableName: str) -> tuple:
    inspector = inspect(engine)
    sql, pk_columns = genertate_query(inspector=inspector, schema=schema, tableName=tableName)
    df = pd.read_sql_query(sql, engine)
    data = []
    for i in df.values.tolist():
        data.append(tuple(str(j).strip().split('.')[0] for j in i))
    output = StringIO()
    df.to_csv(output, header=False, index=False)
    result =  output.getvalue()
    output.close()
    return result, pk_columns


if __name__ == '__main__':
    engine = create_engine(f"mssql+pymssql://datagov:datagov@localhost/MDM?charset=utf8")
    schema = 'dbo'
    tableName = 'MDM_CUSTOMER_MASTER'
    execution_time = timeit.timeit(lambda: get_data(engine=engine, schema=schema, tableName=tableName), number=10)
    print(f"Function query {tableName} to memory executed in {execution_time} seconds.")
