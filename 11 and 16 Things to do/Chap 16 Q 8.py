import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

meta = sa.MetaData()

books = sa.Table('books', meta,
     sa.Column('Title', sa.String, primary_key=True),
     sa.Column('Author', sa.String),
     sa.Column('Year', sa.Integer)
    )

meta.create_all(conn)

with conn.begin() as connection:
    r1 = connection.execute(books.select())
    connection.execute(books.insert(),{'Title':'The Weirdstone of Brisingamen', 'Author': 'Alan Garner', 'Year': 1960 })
    connection.execute(books.insert(),{'Title':'Perdido Street Station', 'Author': 'China Miéville', 'Year': 2000 })
    connection.execute(books.insert(),{'Title': 'Thud!', 'Author': 'Terry Pratchett', 'Year':2005 })
    connection.execute(books.insert(),{'Title': 'The Spellman Files', 'Author': 'Lisa Lutz', 'Year': 2007 })
    connection.execute(books.insert(),{'Title': 'Small Gods', 'Author': 'Terry Pratchett', 'Year':1992 })

    result = connection.execute(books.select())

rows = result.fetchall()
sort_rows = sorted(rows)

print(sort_rows)

##There has been some weird changes in the 2.x version of sqlalchemy that changes how the syntex and such works compared to how the book explains things.