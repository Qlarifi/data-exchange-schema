# EUR-based Scenarios

For each scenario, we created a JSON & JSONL file with all the events, as well as the corresponding CSV files for each event type in that scenario.

Also provided are a set of CSV files (one for each event type) of all the aggregated scenarios.

## Scenario 1-EUR
Transaction of €150 with 3 installments, all paid on time.

| Effective Timestamp | Type               | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |
| ------------------- | ------------------ |----------------| -------------- | ---------- | ---------------- | ------------------- |------|
| 2025-02-03 00:00:00 | transactionIssued |                |                | 150.00 EUR | PayIn3           |                     |      |
| 2025-02-03 00:00:00 | installmentPaidOff | transaction-1  | installment-1  | 50 EUR     |                  |                     | 0    |
| 2025-03-05 00:00:00 | installmentPaidOff | transaction-1  | installment-2  | 50 EUR     |                  |                     | 1    |
| 2025-04-04 00:00:00 | installmentPaidOff | transaction-1  | installment-3  | 50 EUR     |                  |                     | 2    |

## Scenario 2-EUR
Transaction of €150 with 3 installments, postponed (with fee) just before 2nd installment, all paid on time.

| Effective Timestamp | Type                 | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                                   |
| ------------------- | -------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | ------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued    |                |                | 150.00 EUR | PayIn3           |                     |       |                    |                                                   |
| 2025-02-03 00:00:00 | installmentPaidOff   | transaction-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                                   |
| 2025-03-04 00:00:00 | installmentPostponed | transaction-1  | installment-2  |            |                  | 2025-03-12 00:00:00 |       | Consumer-initiated | Consumer postponed the 2nd installment by 7 days. |
| 2025-03-04 00:00:00 | installmentPostponed | transaction-1  | installment-3  |            |                  | 2025-04-11 00:00:00 |       | Consumer-initiated | 3rd installment due date is also pushed 7 days.   |
| 2025-03-04 00:00:00 | feeIssued            | transaction-1  | installment-2  | 2.00 EUR   |                  |                     |       | Postponed Fee      | Fee associated with a single postpone request     |
| 2025-03-12 00:00:00 | installmentPaidOff   | transaction-1  | installment-2  | 50 EUR     |                  |                     |       |                    |                                                   |
| 2025-03-12 00:00:00 | feePaidOff           | transaction-1  | installment-2  | 2.00 EUR   |                  |                     |       |                    | Postponed fee being paid.                         |
| 2025-04-11 00:00:00 | installmentPaidOff   | transaction-1  | installment-3  | 50 EUR     |                  |                     |       |                    |                                                   |

## Scenario 3-EUR
Transaction of €150 with 3 installments, 2nd installment late (with fee), others paid on time.

| Effective Timestamp | Type               | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                                                 |
| ------------------- | ------------------ |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | --------------------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued  |                |                | 150.00 EUR | PayIn3           |                     |       |                    |                                                                 |
| 2025-02-03 00:00:00 | installmentPaidOff | transaction-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                                                 |
| 2025-03-08 00:00:00 | feeIssued          | transaction-1  | installment-2  | 3 EUR      |                  | 2025-03-05 00:00:00 |       | Late Fee           | Late fee is applied after the installment is late for > 3 days. |
| 2025-03-11 00:00:00 | installmentPaidOff | transaction-1  | installment-2  | 50 EUR     |                  |                     |       |                    |                                                                 |
| 2025-03-11 00:00:00 | feePaidOff         | transaction-1  | installment-2  | 3 EUR      |                  |                     |       |                    | Late fee is being paid.                                         |
| 2025-04-04 00:00:00 | installmentPaidOff | transaction-1  | installment-3  | 50 EUR     |                  |                     |       |                    |                                                                 |

## Scenario 4-EUR
Transaction of €150 with 3 installments, with €65 refund, all paid on time.

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 150.00 EUR | PayIn3           |                     |       |                    |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50 EUR     |                  |                     |       |                    |
| 2025-02-05 00:00:00 | transactionRefunded   |                |                | 65 EUR     |                  |                     |       |                    |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-3  | 0 EUR      |                  |                     |       | Refunded           |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-2  | 35 EUR     |                  |                     |       | Refunded           |
| 2025-03-05 00:00:00 | installmentPaidOff    | transaction-1  | installment-2  | 35 EUR     |                  |                     |       |                    |

## Scenario 5-EUR
Transaction of €150 with 1 installment (PayIn30Days), paid on time.

| Effective Timestamp | Type               | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |                                                                   |
| ------------------- | ------------------ |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- |-------------------------------------------------------------------|
| 2025-02-03 00:00:00 | transactionIssued  |                |                | 150.00 EUR | PayIn30Days      |                     |       | Here this is a payment plan that only contains 1 installment.     |
| 2025-03-05 00:00:00 | installmentPaidOff | transaction-1  | installment-1  | 150 EUR    |                  |                     |       |                                                                   |

## Scenario 6-EUR
Transaction of €150 that results in 2 orders of 3 installments, with pay on ship. Note: installments are now issued as part of the transactionIssued events.

| Effective Timestamp | Type                | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |                                                             |
| ------------------- | ------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ----------------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued   |                |                | 150.00 EUR | PayIn3           |                     |       |                                                             |
| 2025-02-04 00:00:00 | transactionIssued   | transaction-1  |                | 100.00 EUR | PayIn3           |                     |       | First shipment is made 1 day after the decision.            |
| 2025-02-04 00:00:00 | installmentPaidOff  | transaction-1  | installment-1  | 33.33 EUR  |                  |                     |       | 1st installment for order 1 is paid on the day of shipping. |
| 2025-02-08 00:00:00 | transactionIssued   | transaction-2  |                | 50.00 EUR  | PayIn3           |                     |       | Second shipment is made 5 days after the decision.          |
| 2025-02-08 00:00:00 | installmentPaidOff  | transaction-2  | installment-1  | 16.66 EUR  |                  |                     |       | 1st installment for order 2 is paid on the day of shipping. |
| 2025-03-06 00:00:00 | installmentPaidOff  | transaction-1  | installment-2  | 33.33 EUR  |                  |                     |       |                                                             |
| 2025-03-10 00:00:00 | installmentPaidOff  | transaction-2  | installment-2  | 16.66 EUR  |                  |                     |       |                                                             |
| 2025-04-05 00:00:00 | installmentPaidOff  | transaction-1  | installment-3  | 33.34 EUR  |                  |                     |       |                                                             |
| 2025-04-09 00:00:00 | installmentPaidOff  | transaction-2  | installment-3  | 16.67 EUR  |                  |                     |       |                                                             |

## Scenario 7-EUR
Transaction of €150 with 3 installments, and a refund greater than what the consumer already paid back.
Refund is applied from the last installment backwards.

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details | Column 1                             |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | ------------------------------------ |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 150.00 EUR | PayIn3           |                     |       |                    |                                      |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                      |
| 2025-02-05 00:00:00 | transactionRefunded   |                |                | 110 EUR    |                  |                     |       |                    |                                      |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-3  | 0 EUR      |                  |                     |       | Refunded           |                                      |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-2  | 0 EUR      |                  |                     |       | Refunded           |                                      |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-1  | 40 EUR     |                  |                     |       | Refunded           | Lender refunds the consumer card €10 |

## Scenario 8-EUR
Transaction of €150 with 3 installments, and a refund greater than what the consumer already paid back.
Refund is evenly split across the 3 installments.

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                         |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | --------------------------------------- |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 150.00 EUR | PayIn3           |                     |       |                    |                                         |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                         |
| 2025-02-05 00:00:00 | transactionRefunded   |                |                | 110 EUR    |                  |                     |       |                    |                                         |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-1  | 13.33 EUR  |                  |                     |       | Refunded           | Lender refunds the consumer card €36.67 |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-2  | 13.33 EUR  |                  |                     |       | Refunded           |                                         |
| 2025-02-05 00:00:00 | installmentRebalanced | transaction-1  | installment-3  | 13.34 EUR  |                  |                     |       | Refunded           |                                         |
| 2025-03-05 00:00:00 | installmentPaidOff    | transaction-1  | installment-2  | 13.33 EUR  |                  |                     |       |                    |                                         |
| 2025-04-04 00:00:00 | installmentPaidOff    | transaction-1  | installment-3  | 13.34 EUR  |                  |                     |       |                    |                                         |

## Scenario 9-EUR
Transaction of €150 with 3 installments. 2nd & 3rd installment late, then written off (sent to collections).

| Effective Timestamp | Type                  | Transaction ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |
| ------------------- | --------------------- |----------------| -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ |
| 2025-02-03 00:00:00 | transactionIssued     |                |                | 150.00 EUR | PayIn3           |                     |       |                    |
| 2025-02-03 00:00:00 | installmentPaidOff    | transaction-1  | installment-1  | 50 EUR     |                  |                     |       |                    |
| 2025-09-01 00:00:00 | installmentWrittenOff | transaction-1  | installment-2  | 50 EUR     |                  |                     |       | ConsumerDefault    |
| 2025-09-01 00:00:00 | installmentWrittenOff | transaction-1  | installment-3  | 50 EUR     |                  |                     |       | ConsumerDefault    |
