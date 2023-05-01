# Create or replace Procedure edit
# (
# r_id int,
# r_name varchar,
# r_phone_number varchar
# )
# language 'plpgsql'
# as $$
# begin
# if (not exists (Select name from phonebook where name = r_name)) then
#          insert into phonebook(id, name, number)
#      values(r_id, r_name, r_phone_number);
# Else
#           update phonebook set number = r_phone_number where phonebook.name = r_name;
# end if;
# end;
# $$

import psycopg2
from psycopg2 import Error

connection = None

def edit(r_id, r_name, r_number):

    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="12345",
                                    host="localhost",
                                    port="5432",
                                    database="pp2")

        # Создайте курсор для выполнения операций с базой данных
        cursor = connection.cursor()

        cursor.callproc('call edit(%s, %s, %s)', (r_id, r_name, r_number))

        
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")

edit(11, "Adi", "87760228214")