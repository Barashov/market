
import sqlite3

class DATA:
    """getting information from database
        methods: get_catalog(style, type), get_id(id)"""

    
    def get_id(self, id):
        self.id = id
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT img, name, price, type, gender, origin, size, material, style FROM item WHERE id=?;", (id,))
        result = cursor.fetchone()
        return result
        conn.close()

    def get_catalog(self, style, type):
            conn = sqlite3.connect("data_base.db")
            cursor = conn.cursor()

            self.style = style
            self.type = type
            cursor.execute("SELECT img, name, price, id FROM item WHERE style=? and type=?;", (style, type))
            result = cursor.fetchmany(2)
            return result
            conn.close()
a = DATA()
print(a.get_id("13"))
