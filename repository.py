
from models import WeightResult


class Repository():

    def __init__(self, db):
        self.db = db

    def cursor_handler(func):
        def decorator(self, *args, **kwargs):
            if not self.db.is_connected():
                self.db.reconnect()
            cursor = self.db.cursor()
            result = func(self, cursor, *args, **kwargs)
            cursor.close()
            self.db.commit()
            return result
        return decorator
        
    @cursor_handler
    def add_weight(self, cursor, message, id_user):
        query = """INSERT INTO weight_user (id_user, weight) 
                                        VALUES (%s,%s)"""
        args = (id_user, message)
        cursor.execute(query, args)
        
    @cursor_handler
    def compare(self, cursor, id_user, period):
        weight_result = WeightResult()
        args = (id_user,)
        current_query = f"""SELECT AVG(weight) 
                            FROM weight_user 
                            WHERE id_user = %s AND {period}(date) = {period}(CURDATE())"""
        cursor.execute(current_query, args)
        weight_result.current_weight = cursor.fetchone()[0]

        last_query = f"""SELECT AVG(weight) 
                            FROM weight_user 
                            WHERE id_user = %s AND {period}(date) = {period}(CURDATE()) - 1"""
        cursor.execute(last_query, args)
        weight_result.last_weight = cursor.fetchone()[0]

        return weight_result