from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return db.session.scalars(db.select(cls)).all()

    @classmethod
    def get_by_id(cls, id):
        return db.get_or_404(cls, id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def simple_filter_one(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()
