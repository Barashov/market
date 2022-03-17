
import sqlite3

class DATA:
    """getting information from database
        methods: get_catalog(style, type), get_id(id)"""

    
    def get_id(self, id):
        self.id = id
        cursor.execute("")
        result = cursor.fetchone(1)

    def get_catalog(self, style, type):
            conn = sqlite3.connect("data_base.db")
            cursor = conn.cursor()

            self.style = style
            self.type = type
            cursor.execute("SELECT img, name, price, id FROM item WHERE style=? and type=?;", (style, type))
            result = cursor.fetchmany(2)
            return result
            conn.close()



