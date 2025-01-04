from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from config import db, ma

class Quote(db.Model):
    __tablename__ = 'quotes'
    id: Mapped[int] = mapped_column(primary_key=True)
    quote: Mapped[str]
    movie: Mapped[str] = mapped_column(String(50))
    keyword: Mapped[str]


class QuoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quote
        load_instance = True
        sqla_session = db.session

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)