from datetime import datetime
from ninja import Router
from .schemas import TransactionSchema, StatementSchema, PostTransactionSchema
from .models import Customer, Transaction
from .services import validate_transaction, get_all_transactions

router = Router()

def user_exists(user_id: int) -> bool:
    u = Customer.objects.get(pk=user_id)
    return u if u else False

@router.get('/{user_id}/extrato')
async def get_data(request, user_id: int) -> StatementSchema:
    if not user_exists(user_id):
        return 404, {'message': 'User does not exists'}
    statement = get_all_transactions()
    return 200, statement.dict()


@router.post('/{user_id}/Transaction')
async def post_transaction(request, user_id: int, data: PostTransactionSchema) -> dict:
    if not user_exists(user_id):
        return 404, {'message': 'User does not exists'}
    data['realizada_em'] = datetime.now()
    data['cliente'] = user_id

    new_transaction = Transaction(**data)
    new_transaction.save()

    status = validate_transaction(new_transaction)

    if 'error' in status:
        return 404, status

    return 200, status
