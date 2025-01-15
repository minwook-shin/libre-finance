try:
    from sqlalchemy import create_engine, Table, Column, Integer, String, Index, Boolean, Float
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import MetaData
    from sqlalchemy.sql.functions import now
except ImportError:
    raise ImportError("You need to install \"libre-finance[sql]\"")

from libre_finance.database.spec import FinanceData


class MariaDBTable:
    def __init__(self, db_name, user, passwd, host, port, table_name='finance'):
        self.metadata = MetaData()
        self.main_table = Table(
            table_name,
            self.metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("product", String(50), nullable=False),
            Column("month", Integer, nullable=False),
            Column("origin_amount", Integer, nullable=False),
            Column("amount", Integer, nullable=False),
            Column("total_interest", Integer, nullable=False),
            Column("interest_rate", Float, nullable=False),
            Column("interest_tax", Float, nullable=False),
            Column("is_tax", Boolean, nullable=False),
            Column("currency", String(3), nullable=False, server_default="KRW"),
            Column("monthly_deposit", Integer, nullable=True),
            Column("created_at", String(20), nullable=False, server_default=now()),
        )
        self.engine = create_engine(
            f"mariadb+pymysql://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8mb4"
        )

        self.session = Session(bind=self.engine)

    def create_table(self):
        Index(
            "id_idx",
            self.main_table.c.id
        )

        Index(
            "currency_idx",
            self.main_table.c.currency
        )

        self.metadata.create_all(self.engine)

    def insert_data(self, data: FinanceData):
        with self.session as session:
            insert = self.main_table.insert().values(
                product=data.product,
                origin_amount=data.origin_amount,
                month=data.month,
                amount=data.amount,
                total_interest=data.total_interest,
                interest_rate=data.interest_rate,
                interest_tax=data.interest_tax,
                is_tax=data.is_tax,
                currency=data.currency,
                monthly_deposit=data.monthly_deposit,
            )
            session.execute(insert)
            session.commit()
