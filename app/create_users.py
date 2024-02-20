from app.models import Customer

Customer.objects.create(nome='greg', saldo=0, limite=100000)
Customer.objects.create(nome='vagner', saldo=0, limite=80000)
Customer.objects.create(nome='valter', saldo=0, limite=1000000)
Customer.objects.create(nome='chaves', saldo=0, limite=10000000)
Customer.objects.create(nome='adolfo', saldo=0, limite=500000)