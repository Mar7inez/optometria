from ninja import Schema


class GenderIn(Schema):
    type: str


class GenderOut(Schema):
    id: int
    type: str