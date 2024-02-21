from datetime import datetime
from ninja import ModelSchema, Schema
from typing import List, Optional
from .models import Transaction


class BalanceSchema(Schema):
    total: int
    data_extrato: datetime
    limite: int


class TransactionSchema(ModelSchema):
    class Meta:
        model = Transaction
        exclude = ['cliente', 'status']


class StatementSchema(Schema):
    saldo: BalanceSchema
    ultimas_transacoes: Optional[List[TransactionSchema]]
    

class PostTransactionSchema(Schema):
    valor: int
    tipo: str
    descricao: str


class ResponseTransactionSchema(Schema):
    limite: int
    saldo: int
