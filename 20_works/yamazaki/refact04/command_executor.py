# command_executor.py
import csv
import importlib

def execute_commands(connection, wb, commands_csv):
    with open(commands_csv, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cmd = row['command']
            func_path = row['function']
            sheet = row['sheet']
            start_row = int(row['start_row'])

            # ワークシートを指定
            ws = wb[sheet]

            # 対応する関数を呼び出す
            module_name, func_name = func_path.rsplit('.', 1)
            module = importlib.import_module(module_name)
            func = getattr(module, func_name)
            ws, row = func(connection, cmd, ws, start_row)
