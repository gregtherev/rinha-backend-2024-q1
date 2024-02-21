from asgiref.sync import sync_to_async
from datetime import datetime
from ninja import Router
from .schemas import StatementSchema, PostTransactionSchema
from .models import Customer, Transaction
from .services import validate_transaction, get_all_transactions

router = Router()

def user_exists(user_id: int) -> bool:
    u = Customer.objects.get(pk=user_id)
    return u if u else False


@router.get('/{user_id}/extrato')
def get_data(request, user_id: int) -> StatementSchema:
    u = user_exists(user_id)
    if not u:
        return 404, {'message': 'User does not exists'}
    statement = get_all_transactions(u)
    return 200, statement.dict()


@router.post('/{user_id}/transaction')
def post_transaction(request, user_id: int, data: PostTransactionSchema) -> dict:
    u = user_exists(user_id)
    if not u:
        return 404, {'message': 'User does not exists'}
    transaction_data = data.dict()
    transaction_data['realizada_em'] = datetime.now()
    transaction_data['cliente'] = u

    new_transaction = Transaction(**transaction_data)
    new_transaction.save()

    status = validate_transaction(new_transaction)

    if 'error' in status:
        return 404, status

    return 200, status
