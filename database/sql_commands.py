import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREAT_ANKETA_TABLE_QUERY)
        try:
            self.connection.execute(sql_queries.CREATE_REFERENCE_TABLE_QUERY)
        except sqlite3.OperationalError:
            pass
        try:
            self.connection.execute(sql_queries.ALTER_USERS_TABLE)
        except sqlite3.OperationalError:
            pass
        self.connection.commit()

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name,):
        try:
            self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name, None,)
        )
        except sqlite3.OperationalError:
            pass
        self.connection.commit()

    def sql_select_all_user_query(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_QUERY,
        ).fetchall()

    def sql_insert_ban_user_query(self, telegram_id, username):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, telegram_id, username, 1)
        )
        self.connection.commit()

    def sql_update_ban_user_query(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_select_user_form_query(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_select_ban_users(self, telegram_id):
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USERS_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_insert_anketa_users(self, telegram_id, username, bio, photo):
        self.cursor.execute(
            sql_queries.INSERT_ANKETA_USERS_QUERY,
            (None, telegram_id, username, bio, photo)
        )
        self.connection.commit()

    def sql_update_reference_link_query(self, link, telegram_id):
        self.cursor.execute(
            sql_queries.SELECT_REFERENCE_LINK_QUERY,
            (link, telegram_id,)
        )
        self.connection.commit()

    def sql_insert_referal_query(self, owner, referal):
        self.cursor.execute(
            sql_queries.INSERT_REFERAL_QUERY,
            (None, owner, referal,)
        )
        self.connection.commit()

    def sql_select_all_user_form_query(self):
        # self.cursor.row_factory = lambda cursor, row: {
        #     'id': row[0],
        #     "telegram_id": row[1],
        #     "nickname": row[2],
        #     "bio": row[3],
        #     "age": row[4],
        #     "photo": row[5],
        # }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_FORM_USERS_QUERY
        ).fetchall()

    def sql_select_by_link_query(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchall()

    def sql_select_referal_by_owner_query(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "owner": row[1],
            "referal": row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_REFERANCE_BY_OWNER_QUERY,
            (owner,)
        ).fetchall()
