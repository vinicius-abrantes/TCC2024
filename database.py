import mysql.connector 
from datetime import datetime

def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ponto'
        )
        if connection.is_connected():
            print("Conexão estabelecida com sucesso.")
        return connection
    except mysql.connector.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

def inserir_dados(connection, nome, email):
    try:
        cursor = connection.cursor()

        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO registro_ponto (Nome, Email, Data_hora) VALUES (%s, %s, %s)"


        cursor.execute(query, (email,nome, data_hora))
        connection.commit()
        print("Dados inseridos com sucesso.")
    except mysql.connector.Error as err:
        print(f"Erro ao executar comando: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão fechada.")
