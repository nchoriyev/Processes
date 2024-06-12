import psycopg2 as psql


class Database:
    @staticmethod
    def connection(query: str, query_type: str):
        db = psql.connect(
            database='datas',
            user='postgres',
            password='Aa9022560',
            host='localhost',
            port='5432'
        )

        cursor = db.cursor()
        cursor.execute(query)
        data = ['create', 'delete', 'update', 'insert', 'alter', 'search']
        if query_type in data:
            db.commit()
            if query_type == "create":
                return f"created successfull"
            return f"{query_type} query successfull"
        else:
            return cursor.fetchall()
