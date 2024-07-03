from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from .models import Transfer
from accounts.models import Account
from decimal import Decimal

@api_view(['POST'])
@transaction.atomic
def transfer_create_view(request):
    origin_account_id = request.data.get('origin_account')
    destination_account_id = request.data.get('destination_account')
    transfer_amount = Decimal(request.data.get('transfer_amount', '0.00'))

    try:
        origin_account = Account.objects.select_for_update().get(pk=origin_account_id)
        destination_account = Account.objects.select_for_update().get(pk=destination_account_id)
    except Account.DoesNotExist:
        return Response({"error": "One of the accounts does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if transfer_amount <= Decimal('0.00'):
        return Response({"error": "Transfer amount must be greater than zero"}, status=status.HTTP_400_BAD_REQUEST)

    if origin_account.balance < transfer_amount:
        return Response({"error": "Insufficient funds in the origin account"}, status=status.HTTP_400_BAD_REQUEST)

    
    origin_account.balance -= transfer_amount
    destination_account.balance += transfer_amount

    try:
        with transaction.atomic():
            origin_account.save()
            destination_account.save()

            
            transfer = Transfer.objects.create(
                origin_account=origin_account,
                destination_account=destination_account,
                transfer_amount=transfer_amount,
                transfer_type=request.data.get('transfer_type', ''),
                transfer_code=request.data.get('transfer_code', ''),
                transfer_charge=request.data.get('transfer_charge', Decimal('0.00')),
                status=request.data.get('status', '')
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"message": "Transfer successful", "transfer_id": transfer.id}, status=status.HTTP_201_CREATED)