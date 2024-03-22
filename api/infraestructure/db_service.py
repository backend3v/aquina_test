from infraestructure.connection import Connection


class DB_Services:
    def send_request(req, commit=False):
        connection = Connection.get_connection()
        cursor = connection.cursor()
        cursor.execute(req)
        if commit:
            connection.commit()
        result = cursor.fetchall()
        connection.close()
        return result