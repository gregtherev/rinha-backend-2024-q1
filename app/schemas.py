from datetime import datetime
from ninja import ModelSchema, Schema
from typing import List
from .models import Transaction


class BalanceSchema(Schema):
    total: int
    data_extrato: datetime
    limite: int


class TransactionSchema(ModelSchema):
    class Config:
        model = Transaction
        exclude = ['cliente']


class StatementSchema(Schema):
    saldo: BalanceSchema
    ultimas_transacoes: List[Transaction]
    

class PostTransactionSchema(Schema):
    valor: int
    tipo: str
    descricao: str


class ResponseTransactionSchema(Schema):
    limite: int
    saldo: int