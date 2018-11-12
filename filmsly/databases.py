##
## Author: Sam McCaffrey
##
##

import os
import sqlite3

index_table_payload = """CREATE TABLE theatre_search_index 
					(
						theatre_chain_name text,
						theatre_chain_url text,
						theatre_location_name text,
						theatre_location_url text,
						movie_name text,
						movie_url text,
						movie_showtime_url_location text
					)
				"""

class sqllite(object):

	def __init__ (self, name = 'theatre_search_index.db'):
		self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
		self.db_path = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), name)

		if os.path.isfile(self.db_path): # if db exists create connection object
			self.conn_obj = sqlite3.connect('{}'.format(self.db_path))
			self.cur_obj = self.conn_obj.cursor()
			return

		# if db doesn't exist create db and connection object
		self.conn_obj = sqlite3.connect('{}'.format(self.db_path))
		self.cur_obj = self.conn_obj.cursor()
		self._create_index_table()
		return

	def query(self, q):
		return self.cur_obj.execute(q)

	def insert(self):
		return

	def list_index_table_columns(self):
		"""Returns tuple list of column names in the index column.
		"""
		columns = self.cur_obj.execute("PRAGMA table_info(theatre_search_index)").fetchall()
		print(columns)
		return [columns]

	def _create_index_table(self):
		"""Creates the theatre_search_index table
		"""
		return self.cur_obj.execute(index_table_payload)

	def close_and_commit(self):
		self.conn_obj.commit()
		self.conn_obj.close()

if __name__ == '__main__':

	test = sqllite()

	test.list_index_table_columns()

	test.close_and_commit()