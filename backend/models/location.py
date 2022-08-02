from sqlalchemy import Column, Integer
from sqlalchemy.sql import func
from database import Base

from sqlalchemy import func
from sqlalchemy.types import UserDefinedType


class Coordinates(UserDefinedType):
    def get_col_spec(self):
        return "GEOMETRY"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ST_AsText(col, type_=self)

    def bind_processor(self, dialect):
        def process(value):
            if value is None:
                return None
            assert isinstance(value, tuple)
            lat, lng = value
            return "POINT(%s %s)" % (lat, lng)

        return process

    def result_processor(self, dialect, coltype):
        def process(value):
            if value is None:
                return None
            # m = re.match(r'^POINT\((\S+) (\S+)\)$', value)
            # lng, lat = m.groups()
            # 'POINT(135.00 35.00)' => ('135.00', '35.00')
            lat, lng = value[6:-1].split()
            return (float(lat), float(lng))

        return process


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    points = Column(Coordinates, nullable=False)
