from ninja import Schema


class RolIn(Schema):
    rol: str


class RolOut(Schema):
    id: int
    rol: str