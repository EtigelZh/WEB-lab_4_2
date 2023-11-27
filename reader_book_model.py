import pandas as pd
def get_reader(conn):
 return pd.read_sql("SELECT * FROM publisher", conn)
def get_book_reader(conn, year_pub, p_name):
    return pd.read_sql(f'''SELECT
 title AS Название,
 genre_name AS Жанр,
 publisher_name AS Издательство,
 year_publication AS Год_издания
 FROM book
 JOIN genre USING (genre_id)
 JOIN publisher USING (publisher_id)
 WHERE LENGTH(title) - LENGTH(REPLACE(title, ' ', '')) = 0 AND year_publication < {year_pub} AND publisher_name = '{p_name}'
 ORDER BY
    Год_издания ASC,
    Название ASC
''', conn)
def get_year(conn):
    return pd.read_sql("SELECT * FROM book", conn)