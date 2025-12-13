from sqlalchemy import create_engine, Table, Column, BigInteger, String, Text, MetaData, select, insert, update
from sqlalchemy.exc import IntegrityError

class UrlRepository:
    def __init__(self, db_url="mysql+pymysql://user:password@db:3306/shortenurl"):
        self.engine = create_engine(db_url, echo=False)
        self.metadata = MetaData()

        self.urls = Table(
            'urls', self.metadata,
            Column('id', BigInteger, primary_key=True, autoincrement=True),
            Column('long_url', Text, nullable=False),
            Column('url_hash', String(64), nullable=False, unique=True),
            Column('short_code', String(5), unique=True)
        )

        self.metadata.create_all(self.engine)

    def get_by_url_hash(self, url_hash):
        stmt = select(self.urls).where(self.urls.c.url_hash == url_hash)
        with self.engine.connect() as conn:
            result = conn.execute(stmt).mappings().first()
            return dict(result) if result else None

    def insert_new_url(self, long_url, url_hash):
        stmt = insert(self.urls).values(long_url=long_url, url_hash=url_hash)
        with self.engine.begin() as conn:
            try:
                result = conn.execute(stmt)
                return result.inserted_primary_key[0]
            except IntegrityError:

                existing = self.get_by_url_hash(url_hash)
                return existing['id']

    def update_short_code(self, record_id, short_code):
        stmt = update(self.urls).where(self.urls.c.id == record_id).values(short_code=short_code)
        with self.engine.begin() as conn:
            conn.execute(stmt)

    def get_by_id(self, record_id):
        stmt = select(self.urls).where(self.urls.c.id == record_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt).mappings().first()
            return dict(result) if result else None

    def get_by_short_code(self, short_code):
        stmt = select(self.urls).where(self.urls.c.short_code == short_code)
        with self.engine.connect() as conn:
            result = conn.execute(stmt).mappings().first()
            return dict(result) if result else None
