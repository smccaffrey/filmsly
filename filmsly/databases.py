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
						movie_showtimes_url_location text,
						record_date datetime
					)
				"""

class sqllite(object):

	def __init__ (self, name = 'theatre_search_index.db'):
		self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
		self.db_path = os.path.join(os.path.join(os.path.dirname(__file__), 'data'), name)
		#print(os.path.isfile(self.db_path))

		if os.path.isfile(self.db_path): # if db exists create connection object
			self.conn_obj = sqlite3.connect('{}'.format(self.db_path))
			self.cur_obj = self.conn_obj.cursor()
			return

		# if db doesn't exist create db and connection object
		print(self.db_path)
		self.conn_obj = sqlite3.connect('{}'.format(self.db_path))
		self.cur_obj = self.conn_obj.cursor()
		self._create_index_table()
		return

	def query(self, q):
		return self.cur_obj.execute(q).fetchall()

	def insert_index_record(self, data: tuple) -> str:
		_query = '''INSERT INTO theatre_search_index(theatre_chain_name,theatre_chain_url,theatre_location_name, \
		theatre_location_url,movie_name,movie_showtimes_url_location,record_date) \
		VALUES(?,?,?,?,?,?,?)'''
		self.cur_obj.execute(_query, data)
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

	def delete_theatre_records(self, theatre_name):
		q = '''DELETE FROM theatre_search_index WHERE theatre_chain_name LIKE '%{}%' '''.format(theatre_name)
		return self.cur_obj.execute(q)

	def close_and_commit(self):
		self.conn_obj.commit()
		self.conn_obj.close()

if __name__ == '__main__':

	test = sqllite()

	test.list_index_table_columns()

	test.close_and_commit()