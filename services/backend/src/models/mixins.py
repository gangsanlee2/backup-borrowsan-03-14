from sqlalchemy import TIMESTAMP as Timestamp, Column, text


class TimestampMixin(object):
    created_at = Column(Timestamp, nullable=False, server_default=text('current_timestamp'))
    updated_at = Column(Timestamp, nullable=False, server_default=text('current_timestamp on update current_timestamp'))
