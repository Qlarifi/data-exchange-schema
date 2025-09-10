# USD-based Scenarios

## Scenario 1-USD
Transaction of \$200 with 4 installments, all paid on time.

| Effective Timestamp | Type                | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |
| ------------------- | ------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- |
| 2025-02-03 00:00:00 | transactionIssued   |                |                | 200.00 USD | PayIn4           | \-                  | \-    |
| 2025-02-03 00:00:00 | installmentPaidOff  | transaction-1  | installment-1  | 50.00 USD  | \-               | \-                  | \-    |
| 2025-02-17 00:00:00 | installmentPaidOff  | transaction-1  | installment-2  | 50.00 USD  | \-               | \-                  | \-    |
| 2025-03-03 00:00:00 | installmentPaidOff  | transaction-1  | installment-3  | 50.00 USD  | \-               | \-                  | \-    |
| 2025-03-17 00:00:00 | installmentPaidOff  | transaction-1  | installment-4  | 50.00 USD  | \-               | \-                  | \-    |

## Scenario 2-USD
Transaction of \$200 with 4 installments, postponed (with fee) just before 3rd installment, all paid on time.

| Effective Timestamp | Type                 | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                                   |
| ------------------- | -------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | ------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued    |                |                | 200.00 USD | PayIn4           | \-                  | \-    | \-                 |                                                   |
| 2025-02-03 00:00:00 | installmentPaidOff   | transaction-1  | installment-1  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                   |
| 2025-02-17 00:00:00 | installmentPaidOff   | transaction-1  | installment-2  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                   |
| 2025-03-02 00:00:00 | installmentPostponed | transaction-1  | installment-3  | \-         | \-               | 2025-03-10 00:00:00 | \-    | Consumer-initiated | Consumer postponed the 3rd installment by 7 days. |
| 2025-03-02 00:00:00 | installmentPostponed | transaction-1  | installment-4  | \-         | \-               | 2025-03-24 00:00:00 | \-    | Consumer-initiated | 4th installment due date is also pushed 7 days.   |
| 2025-03-02 00:00:00 | feeIssued            | transaction-1  | installment-2  | 2.00 USD   | \-               | \-                  | \-    | Postponed Fee      | Fee associated with a single postpone request     |
| 2025-03-10 00:00:00 | installmentPaidOff   | transaction-1  | installment-3  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                   |
| 2025-03-10 00:00:00 | feePaidOff           | transaction-1  | installment-2  | 2.00 USD   | \-               | \-                  | \-    | \-                 | Postponed fee being paid.                         |
| 2025-03-24 00:00:00 | installmentPaidOff   | transaction-1  | installment-4  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                   |

## Scenario 3-USD
Transaction of \$200 with 4 installments, 2nd installment late (with fee), others paid on time.

| Effective Timestamp | Type                | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                                                 |
| ------------------- | ------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | --------------------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued   |                |                | 200.00 USD | PayIn4           | \-                  | \-    | \-                 |                                                                 |
| 2025-02-03 00:00:00 | installmentPaidOff  | transaction-1  | installment-1  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                                 |
| 2025-02-20 00:00:00 | feeIssued           | transaction-1  | installment-2  | 3.00 USD   | \-               | \-                  | \-    | Late Fee           | Late fee is applied after the installment is late for > 3 days. |
| 2025-02-21 00:00:00 | installmentPaidOff  | transaction-1  | installment-2  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                                 |
| 2025-02-21 00:00:00 | feePaidOff          | transaction-1  | installment-2  | 3.00 USD   | \-               | \-                  | \-    | \-                 | Late fee is being paid.                                         |
| 2025-03-03 00:00:00 | installmentPaidOff  | transaction-1  | installment-3  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                                 |
| 2025-03-17 00:00:00 | installmentPaidOff  | transaction-1  | installment-4  | 50.00 USD  | \-               | \-                  | \-    | \-                 |

## Scenario 4-USD
Transaction of \$200 with 4 installments, with \$65 refund, all paid on time.

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                                                                                                                                                               |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 200.00 USD | PayIn4           | \-                  | \-    | \-                 |                                                                                                                                                                               |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                                                                                                                                               |
| 2025-02-05 00:00:00 | transactionRefunded   |                |                | 65.00 USD  |                  | \-                  | \-    |                    | The $65 refund is applied from the last installment backwards.<br>It means the 3rd installment is fully refunded ($50) and<br>the 2nd installment is partialy refunded ($15). |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-4  | 0.00 USD   | \-               | \-                  | \-    | Refunded           |                                                                                                                                                                               |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-3  | 35.00 USD  | \-               | \-                  | \-    | Refunded           | The amount in the rebalanced event represents the new amount due.                                                                                                             |
| 2025-02-17 00:00:00 | installmentPaidOff    | transaction-1  | installment-2  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                                                                                                                                                               |
| 2025-03-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-3  | 35.00 USD  | \-               | \-                  | \-    | \-                 |                                                                                                                                                                               |

## Scenario 5-USD
Transaction of \$150 with 1 installment (PayIn30Days), paid on time.

| Effective Timestamp | Type               | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |                                                                   |
| ------------------- | ------------------ |----------------| -------------- |------------| ---------------- | ------------------- | ----- |-------------------------------------------------------------------|
| 2025-02-03 00:00:00 | transactionIssued  |                |                | 150.00 USD | PayIn30Days      |                     |       | Here this is a payment plan that only contains 1 installment.     |
| 2025-03-05 00:00:00 | installmentPaidOff | transaction-1  | installment-1  | 150.00 USD |                  |                     |       |                                                                   |

## Scenario 6-USD
Transaction of \$200 that results in 2 orders of 4 installments, with pay on ship. Note: installments are now issued as part of the transactionIssued events.

| Effective Timestamp | Type                | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |                                                             |
| ------------------- | ------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ----------------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued   |                |                | 200.00 USD | PayIn4           | \-                  | \-    |                                                             |
| 2025-02-04 00:00:00 | transactionIssued   | transaction-1  |                | 133.32 USD | PayIn4           | \-                  | \-    | First shipment is made 1 day after the decision.            |
| 2025-02-04 00:00:00 | installmentPaidOff  | transaction-1  | installment-1  | 33.33 USD  | \-               | \-                  | \-    | 1st installment for order 1 is paid on the day of shipping. |
| 2025-02-08 00:00:00 | transactionIssued   | transaction-2  |                | 66.68 USD  | PayIn4           | \-                  | \-    | Second shipment is made 5 days after the decision.          |
| 2025-02-08 00:00:00 | installmentPaidOff  | transaction-2  | installment-1  | 16.66 USD  | \-               | \-                  | \-    | 1st installment for order 2 is paid on the day of shipping. |
| 2025-02-18 00:00:00 | installmentPaidOff  | transaction-1  | installment-2  | 33.33 USD  | \-               | \-                  | \-    |                                                             |
| 2025-02-22 00:00:00 | installmentPaidOff  | transaction-2  | installment-2  | 16.66 USD  | \-               | \-                  | \-    |                                                             |
| 2025-03-04 00:00:00 | installmentPaidOff  | transaction-1  | installment-3  | 33.34 USD  | \-               | \-                  | \-    |                                                             |
| 2025-03-08 00:00:00 | installmentPaidOff  | transaction-2  | installment-3  | 16.67 USD  | \-               | \-                  | \-    |                                                             |
| 2025-03-18 00:00:00 | installmentPaidOff  | transaction-1  | installment-4  | 33.34 USD  | \-               | \-                  | \-    |                                                             |
| 2025-03-22 00:00:00 | installmentPaidOff  | transaction-2  | installment-4  | 16.67 USD  | \-               | \-                  | \-    |                                                             |

## Scenario 7-USD
Transaction of \$200 with 4 installments, with \$110 refund before 3rd installment.
Refund is applied from the last installment backwards.

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                      |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | ------------------------------------ |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 200.00 USD | PayIn4           | \-                  | \-    | \-                 |                                      |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                      |
| 2025-02-17 00:00:00 | installmentPaidOff    | transaction-1  | installment-2  | 50.00 USD  | \-               | \-                  | \-    | \-                 |                                      |
| 2025-02-26 00:00:00 | transactionRefunded   |                |                | 110 USD    | \-               | \-                  | \-    | \-                 |                                      |
| 2025-02-26 00:00:00 | installmentRebalanced | transaction-1  | installment-4  | 0.00 USD   | \-               | \-                  | \-    | Refunded           |                                      |
| 2025-02-26 00:00:00 | installmentRebalanced | transaction-1  | installment-3  | 0.00 USD   | \-               | \-                  | \-    | Refunded           |                                      |
| 2025-02-26 00:00:00 | installmentRebalanced | transaction-1  | installment-2  | 40.00 USD  | \-               | \-                  | \-    | Refunded           | Lender refunds the consumer card $10 |

## Scenario 8-USD
Transaction of \$200 with 4 installments, with \$110 refund before 3rd installment.
Refund is evenly split across the 3 installments.

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 200.00 USD | PayIn4           | \-                  | \-    | \-                 |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50.00 USD  | \-               | \-                  | \-    | \-                 |
| 2025-02-17 00:00:00 | installmentPaidOff    | transaction-1  | installment-2  | 50.00 USD  | \-               | \-                  | \-    | \-                 |
| 2025-02-26 00:00:00 | transactionRefunded   |                |                | 110.00 USD | \-               | \-                  | \-    | \-                 |
| 2025-02-03 00:00:00 | installmentRebalanced | transaction-1  | installment-1  | 22.50 USD  | \-               | \-                  | \-    | Refunded           |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-2  | 22.50 USD  | \-               | \-                  | \-    | Refunded           |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-3  | 22.50 USD  | \-               | \-                  | \-    | Refunded           |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-4  | 22.50 USD  | \-               | \-                  | \-    | Refunded           |
| 2025-03-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-3  | 22.50 USD  | \-               | \-                  | \-    | \-                 |
| 2025-03-17 00:00:00 | installmentPaidOff    | transaction-1  | installment-4  | 22.50 USD  | \-               | \-                  | \-    | \-                 |

## Scenario 9-USD
Transaction of \$150 with 4 installments, with 3rd & 4th installment late, then written off (sent to collections).

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 150.00 USD | PayIn4           | \-                  | \-    | \-                 |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50.00 USD  | \-               | \-                  | \-    | \-                 |
| 2025-02-17 00:00:00 | installmentPaidOff    | transaction-1  | installment-2  | 50.00 USD  | \-               | \-                  | \-    | \-                 |
| 2025-09-01 00:00:00 | installmentWrittenOff | transaction-1  | installment-3  | 50.00 USD  | \-               | \-                  | \-    | ConsumerDefault    |
| 2025-09-01 00:00:00 | installmentWrittenOff | transaction-1  | installment-4  | 50.00 USD  | \-               | \-                  | \-    | ConsumerDefault    |
