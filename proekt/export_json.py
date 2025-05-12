# export_json.py
# Скрипт для экспорта договоров из базы данных в JSON-файл для отчёта

import sqlite3
import json

def export_to_json(db_path="stroBuh.db", output_path="report_data.json"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT contracts.number, clients.name, contracts.amount, contracts.start_date, contracts.status
        FROM contracts
        JOIN clients ON contracts.client_inn = clients.inn
    """)
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "number": row[0],
            "client": row[1],
            "amount": row[2],
            "start_date": row[3],
            "status": row[4]
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"[✓] Данные успешно экспортированы в {output_path}")

if __name__ == "__main__":
    export_to_json()
