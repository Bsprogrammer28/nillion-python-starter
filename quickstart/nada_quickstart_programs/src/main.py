from nada_dsl import *

def nada_main():
    # Define the Bank party
    bank_party = Party(name="Bank")

    # Define secret inputs for the Bank party
    loan_client2 = SecretInteger(Input(name="LoanClient2", party=bank_party))
    bank_balance = SecretInteger(Input(name="BankBalance", party=bank_party))

    # Perform banking operations
    new_bank_balance = bank_balance - loan_client2

    # Output the new bank balance to the Bank party
    return [
        Output(new_bank_balance, "NewBankBalance", bank_party),
    ]

# Example usage (assuming nillion client setup is elsewhere)
if __name__ == "__main__":
    result = nada_main()
    print(result)
