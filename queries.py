import sqlite3
import json

def search_cpf_by_exact_name(name, cursor):
    cursor.execute("SELECT * FROM cpf WHERE nome = ?", (name,))
    result = cursor.fetchall()
    json_result = []
    for row in result:
        json_dict = {
            'cpf': row[0],
            'nome': row[1],
            'sexo': row[2],
            'nasc': row[3]
            }
        json_result.append(json_dict)
    json_result = json.dumps(json_result)
    return json_result

def search_cpf_by_name(name, cursor):
    cursor.execute("SELECT * FROM cpf WHERE nome LIKE ?", ('%' + name + '%',))
    result = cursor.fetchall()
    json_result = []
    for row in result:
        json_dict = {
            'cpf': row[0],
            'nome': row[1],
            'sexo': row[2],
            'nasc': row[3]
            }
        json_result.append(json_dict)
    json_result = json.dumps(json_result)
    return json_result

def search_cpf_by_cpf(cpf, cursor):
    cursor.execute("SELECT * FROM cpf WHERE cpf = ?", (cpf,))
    result = cursor.fetchall()
    json_result = []
    for row in result:
        json_dict = {
            'cpf': row[0],
            'nome': row[1],
            'sexo': row[2],
            'nasc': row[3]
            }
        json_result.append(json_dict)
    json_result = json.dumps(json_result)
    return json_result

def check_person_cnpj(name, cursor):
    cursor.execute("SELECT * FROM socios WHERE nome LIKE ?", ('%' + name + '%',))
    result = cursor.fetchall()
    json_result = []
    for row in result:
        json_dict = {
            'cpf': row[3],
            'nome': row[2],
            'sexo': row[6],
            'nasc': row[7],
            'aaa': row[8],
            'b': row[9]
            }
        json_result.append(json_dict)
    json_result = json.dumps(json_result)
    return json_result