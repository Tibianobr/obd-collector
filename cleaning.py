import re
import configuration
from database import Database

raw_db = Database(configuration.get_db_name())
clean_db = Database(configuration.get_clean_db_name())

all_data = {}

for row in raw_db.get_cursor().execute('SELECT * FROM data ORDER BY timestamp'):
    if row[2] is not None and row[2] != 'None':
        sanitized_data = re.sub('[^\d\.\-]', '', row[2])
        list_tuple = list(row)
        list_tuple[2] = sanitized_data
        row = tuple(list_tuple)
        clean_db.copy_clean(row)
