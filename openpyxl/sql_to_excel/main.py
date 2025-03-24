import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import argparse

load_dotenv()

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

def load_queries_from_csv(csv_file):
    """從 CSV 檔案讀取查詢並轉成字典"""
    df = pd.read_csv(csv_file, sep='|')
    return dict(zip(df['tab_name'], df['query']))

def run_queries_and_export_to_excel(queries, output_file='query_results.xlsx'):
    engine = create_engine(DB_CONNECTION_STRING)

    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for idx, (sheet_name, query) in enumerate(queries.items(), start=1):
            try:
                df = pd.read_sql(query, engine)
                
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                print(f"查詢結果已成功寫入標籤頁：{sheet_name}")
            except Exception as e:
                print(f"無法執行查詢 '{sheet_name}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="將 SQL 查詢結果匯出至 Excel 檔案的多個標籤頁")
    parser.add_argument("input_csv", help="包含查詢和標籤名稱的 CSV 檔案")
    parser.add_argument("output_excel", help="輸出的 Excel 檔案名稱")
    
    args = parser.parse_args()

    queries = load_queries_from_csv(args.input_csv)
    
    run_queries_and_export_to_excel(queries, args.output_excel)
