from nada_dsl import *

def nada_main():
    # Define the parties (banks and central authority)
    bank1 = Party(name="Bank1")
    bank2 = Party(name="Bank2")
    bank3 = Party(name="Bank3")
    central_authority = Party(name="CentralAuthority")

    # Define secret inputs for each bank's transactions
    # Each bank provides the transaction amounts and flags indicating suspicious activity
    transactions_bank1 = [
        SecretInteger(Input(name="TransactionAmount_Bank1_1", party=bank1)),
        SecretInteger(Input(name="TransactionAmount_Bank1_2", party=bank1)),
        SecretInteger(Input(name="TransactionAmount_Bank1_3", party=bank1))
    ]
    flags_bank1 = [
        SecretBoolean(Input(name="Suspicious_Bank1_1", party=bank1)),
        SecretBoolean(Input(name="Suspicious_Bank1_2", party=bank1)),
        SecretBoolean(Input(name="Suspicious_Bank1_3", party=bank1))
    ]

    transactions_bank2 = [
        SecretInteger(Input(name="TransactionAmount_Bank2_1", party=bank2)),
        SecretInteger(Input(name="TransactionAmount_Bank2_2", party=bank2)),
        SecretInteger(Input(name="TransactionAmount_Bank2_3", party=bank2))
    ]
    flags_bank2 = [
        SecretBoolean(Input(name="Suspicious_Bank2_1", party=bank2)),
        SecretBoolean(Input(name="Suspicious_Bank2_2", party=bank2)),
        SecretBoolean(Input(name="Suspicious_Bank2_3", party=bank2))
    ]

    transactions_bank3 = [
        SecretInteger(Input(name="TransactionAmount_Bank3_1", party=bank3)),
        SecretInteger(Input(name="TransactionAmount_Bank3_2", party=bank3)),
        SecretInteger(Input(name="TransactionAmount_Bank3_3", party=bank3))
    ]
    flags_bank3 = [
        SecretBoolean(Input(name="Suspicious_Bank3_1", party=bank3)),
        SecretBoolean(Input(name="Suspicious_Bank3_2", party=bank3)),
        SecretBoolean(Input(name="Suspicious_Bank3_3", party=bank3))
    ]

    # Initialize lists to hold the combined transactions and flags
    all_transactions = transactions_bank1 + transactions_bank2 + transactions_bank3
    all_flags = flags_bank1 + flags_bank2 + flags_bank3

    # Define a threshold for detecting anomalies
    threshold = PublicInteger(10000)

    # Detect anomalies based on the transaction amounts and flags
    anomalies = []
    for transaction, flag in zip(all_transactions, all_flags):
        is_anomalous = (transaction > threshold) & flag
        anomalies.append(is_anomalous)

    # Output the detected anomalies to the central authority
    anomaly_outputs = [Output(anomaly, f"Anomaly_{i+1}", central_authority) for i, anomaly in enumerate(anomalies)]

    return anomaly_outputs

# The main function call
outputs = nada_main()
for output in outputs:
    print(f"Output Name: {output.name}, Output Value: {output.value}, Output Party: {output.party.name}")
