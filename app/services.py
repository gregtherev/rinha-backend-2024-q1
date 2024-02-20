from .models import Transaction, Customer
from .schemas import TransactionSchema, StatementSchema


def has_limit(customer: Customer, transaction_value: int) -> bool:
    if customer.saldo - transaction_value < customer.limite*-1:
        return False
    return True


def process_credit_transaction(customer: Customer, transaction: Transaction):
    if customer.limite >= transaction.valor:
        customer.limite -= transaction.valor
        transaction.status = 'Sucesso'    
    else:
        transaction.status = 'Limite insuficiente'


def process_debit_transaction(customer: Customer, transaction: Transaction):
    if has_limit(customer, transaction.valor):
        customer.saldo -= transaction.valor
        transaction.status = 'Sucesso'
    else:
        transaction.status = 'Saldo e Limite insuficientes'


def validate_transaction(transaction: Transaction) -> dict:
    u = Customer.objects.get(pk=transaction.u)
    try:
        if transaction.tipo == 'c':
            process_credit_transaction(u, transaction)
        elif transaction.tipo == 'd':
            process_debit_transaction(u, transaction)
            
        u.save()
        transaction.save()
        
        return {"limite":f"{u.limite}", "saldo":f"{u.saldo}"}
    except:
        # exceçao generica
        return {"error": "call 911"}            


def get_all_transactions(customer: Customer) -> dict:
    last_transactions = Transaction.objects.filter(customer=customer).order_by('-realizada_em')[:10]
    transaction_dict = [TransactionSchema(transaction).dict() for transaction in last_transactions]

    balance_dict = {
        'total': customer.saldo,
        'data_extrado': datetime.now(),
        'limite': customer.limite
        }

    return StatementSchema(saldo=balance_dict, ultimas_transacoes=transaction_dict)
