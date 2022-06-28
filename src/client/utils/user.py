import utils.db

class User:
    """
    retain user information for manipulation
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.visited = self.get_visited()
        self.wishlist = self.get_wishlist()

    def get_visited(self):
        vis = None
        # camps=['campA', 'campB']
        # conn = get_db_connection()

        # if conn is not None:
        #     cur = conn.cursor()
        #     cur.execute('SELECT * FROM users;')
        #     camps = cur.fetchall()
        #     cur.close()
        #     conn.close()
        return vis

    def get_wishlist(self):
        wish = None
        return wish

    def get_user(self):
        pass

    def update_visited(self):
        pass

    def update_wishlist(self):
        pass

    def delete_wishlist(self):
        pass