import csv
import datetime
import sys
import glob

def parse_date(date_str):
    """嘗試多種格式來解析日期字串"""
    if not date_str:
        return ""
    # 所有可能的日期格式
    formats = [
        '%d-%b-%y',  # 23-Jun-25
        '%Y/%m/%d',  # 2024/7/16
        '%Y-%m-%d',  # 2024-07-16
        '%Y-%-m-%-d', # 2024-7-6 (處理無前導零的情況)
        '%m/%d/%Y',  # 07/16/2024
    ]
    for fmt in formats:
        try:
            # 解析成功後，統一格式化為 YYYY-MM-DD
            return datetime.datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    # 如果所有格式都失敗，返回原值並在終端提示
    print(f"警告：無法解析日期 '{date_str}'，將保留原值。")
    return date_str

def process_csv(input_file, output_file):
    """讀取、處理並寫入 CSV 檔案"""
    try:
        with open(input_file, mode='r', encoding='utf-8', errors='ignore') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # 讀取並寫入標頭
            header = next(reader)
            writer.writerow(header)
            
            # 尋找 'date' 欄位的位置
            try:
                date_index = header.index('date')
            except ValueError:
                print(f"錯誤：在檔案 {input_file} 中找不到 'date' 欄位。")
                return

            # 逐行處理
            for row in reader:
                if len(row) > date_index:
                    row[date_index] = parse_date(row[date_index])
                writer.writerow(row)
        print(f"處理完成：'{input_file}' -> '{output_file}'")

    except FileNotFoundError:
        print(f'錯誤：找不到檔案 {input_file}。')
    except Exception as e:
        print(f'處理 {input_file} 時發生錯誤: {e}')

if __name__ == "__main__":
    # 自動尋找當前資料夾中所有符合條件的 CSV 檔案
    # 例如：Income-*.csv, Expense-*.csv
    csv_files = glob.glob('Income-*.csv') + glob.glob('Expense-*.csv')
    
    # 過濾掉已經是 -fixed 的檔案
    source_files = [f for f in csv_files if '-fixed.csv' not in f]

    if not source_files:
        print("找不到需要處理的 Income 或 Expense CSV 檔案。")
    else:
        for file_path in source_files:
            output_path = file_path.replace('.csv', '-fixed.csv')
            print(f"正在處理檔案: {file_path}")
            process_csv(file_path, output_path)
        print("\n所有檔案處理完畢。請使用檔名包含 '-fixed' 的檔案進行匯入。")