# Data Exchange Schema

## Events
### [TransactionCreated](./events/transactionCreated.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the transaction was issued from the lender's perspective.

**transactionId**: A unique identifier for the transaction.

**accountId**: A unique identifier for the account this transaction is associated with.

**consumerId**: A unique identifier for the consumer who owes this transaction (as defined by the lender).

**amount.number**: The monetary amount of this transaction.

**amount.currency**: The currency of the amount.

**transactionType**: The type of transaction product, Possible values are: `PayIn3`, `PayIn4`, `PayIn30Days`.

### [InstallmentIssued](./events/installmentIssued.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the instalment was issued from the lender's perspective.

**installmentId**: A unique identifier for this specific instalment.

**transactionId**: A unique identifier for the transaction this instalment belongs to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId**: A unique identifier for the consumer who owes this instalment (as defined by the lender).

**amount.number**: The monetary amount due for this instalment.

**amount.currency**: The currency of the amount.

**dueTimestamp**: The date and time (UTC) when this instalment is due.

**index**: The sequential order of this instalment within the transaction.

### [InstallmentPaid](./events/installmentPaid.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the payment was made from the lender's perspective.

**installmentId**: The unique identifier of the instalment that received the payment.

**transactionId**: The unique identifier of the transaction the instalment belongs to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId** [optional]: The unique identifier of the consumer who made the payment.

**amount.number**: The amount paid towards the instalment.

**amount.currency**: The currency of the payment.

### [InstallmentPostponed](./events/installmentPostponed.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the installment was postponed from the lender's perspective.

**installmentId**: The unique identifier of the instalment postponed.

**transactionId**: The unique identifier of the transaction the instalment belongs to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId**: The unique identifier of the consumer the instalment belongs to.

**feeAmount.number**: The amount of the fee.

**feeAmount.currency**: The currency of the fee.

**postponedType**: The type of postponed action. Possible values are `ConsumerRequest`, `LenderCommercial`, `LenderTechnical`.

### [FeeIssued](./events/feeIssued.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the penalty was assessed from the lender's perspective.

**installmentId**: The unique identifier of the instalment with the assessed penalty.

**transactionId**: The unique identifier of the transaction the instalment belongs to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId**: The unique identifier of the consumer who incurred the penalty.

**penaltyAmount.number**: The amount of the penalty assessed.

**penaltyAmount.currency**: The currency of the penalty.

**penaltyType**: The type of penalty fee that was added to the transaction amount. Possible values are: `LateFee`, `PostponedFee`, `Interest`, `Other`.

### [FeePaid](./events/feePaid.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the fee was paid from the lender's perspective.

**installmentId** [optional]: The unique identifier of the instalment associated with the fee.

**transactionId**: The unique identifier of the transaction associated with the fee.

**accountId**: A unique identifier for the account this fee is associated with.

**consumerId**: The unique identifier of the consumer who incurred the fee.

**amount.number**: The amount paid.

**amount.currency**: The currency of the payment.

### [RefundIssued](./events/refundIssued.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the refund was issued from the lender's perspective.

**installmentId**: The unique identifier of the instalment that was refunded.

**transactionId**: The unique identifier of the transaction the instalment belongs to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId**: The unique identifier of the consumer who received the refund.

**refundAmount.number**: The amount of the refund issued.

**refundAmount.currency**: The currency of the refund.

### [InstallmentRebalanced](./events/installmentRebalanced.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the rebalance occurred from the lender's perspective.

**installmentId**: The unique identifier of the instalment that was rebalanced.

**transactionId**: The unique identifier of the transaction the instalment belongs to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId** [optional]: The unique identifier of the consumer affected by the rebalance.

**newAmountDue.number**: The new amount due on the instalment after the rebalance.

**newAmountDue.currency**: The currency of the new amount due.

### [InstallmentWrittenOff](./events/installmentWrittenOff.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the write-off occurred from the lender's perspective.

**installmentId**: The unique identifier of the instalment that was written off.

**transactionId**: The unique identifier of the transaction the instalment belongs to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId**: The unique identifier of the consumer whose instalment was written off.

**reason**: The reason for the write-off. Possible values are: `ConsumerDefault` (sent to collections), `LenderCommercial`, `LenderTechnical`.

### [InstallmentCanceled](./events/installmentCanceled.json)

**type**: Indicates the event type.

**effectiveTimestamp**: The timestamp (UTC) when the cancellation occurred from the lender's perspective.

**installmentId**: The unique identifier of the cancelled instalment.

**transactionId**: The unique identifier of the transaction the instalment belonged to.

**accountId**: A unique identifier for the account this instalment is associated with.

**consumerId**: The unique identifier of the consumer affected by the cancellation.

## Scenarios
We have put together a few scenarios to align on the data exchange schema. These scenarios are based on the payment plan types and the possible transactions that can occur within them. The scenarios are not exhaustive but should cover the most common cases.

### Scenario 1
Transaction with 3 installments, all paid on time.

| Effective Timestamp | Type               | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |
| ------------------- | ------------------ | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- |
| 2025-02-03 00:00:00 | transactionCreated |          |                | 150.00 EUR | PayIn3           |                     |       |
| 2025-02-03 00:00:00 | installmentIssued  | order-1  | installment-1  | 50 EUR     |                  | 2025-02-03 00:00:00 | 0     |
| 2025-02-03 00:00:00 | installmentIssued  | order-1  | installment-2  | 50 EUR     |                  | 2025-03-05 00:00:00 | 1     |
| 2025-02-03 00:00:00 | installmentIssued  | order-1  | installment-3  | 50 EUR     |                  | 2025-04-04 00:00:00 | 2     |
| 2025-02-03 00:00:00 | installmentPaid    | order-1  | installment-1  | 50 EUR     |                  |                     |       |
| 2025-03-05 00:00:00 | installmentPaid    | order-1  | installment-2  | 50 EUR     |                  |                     |       |
| 2025-04-04 00:00:00 | installmentPaid    | order-1  | installment-3  | 50 EUR     |                  |                     |       |

### Scenario 2
Transaction with 3 installments, postponed (with fee) just before 2nd installment, all paid on time.

| Effective Timestamp | Type                 | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                                   |
| ------------------- | -------------------- | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | ------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionCreated   |          |                | 150.00 EUR | PayIn3           |                     |       |                    |                                                   |
| 2025-02-03 00:00:00 | installmentIssued    | order-1  | installment-1  | 50 EUR     |                  | 2025-02-03 00:00:00 | 0     |                    |                                                   |
| 2025-02-03 00:00:00 | installmentIssued    | order-1  | installment-2  | 50 EUR     |                  | 2025-03-05 00:00:00 | 1     |                    |                                                   |
| 2025-02-03 00:00:00 | installmentIssued    | order-1  | installment-3  | 50 EUR     |                  | 2025-04-04 00:00:00 | 2     |                    |                                                   |
| 2025-02-03 00:00:00 | installmentPaid      | order-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                                   |
| 2025-03-04 00:00:00 | installmentPostponed | order-1  | installment-2  |            |                  | 2025-03-12 00:00:00 |       | Consumer-initiated | Consumer postponed the 2nd installment by 7 days. |
| 2025-03-04 00:00:00 | installmentPostponed | order-1  | installment-3  |            |                  | 2025-04-11 00:00:00 |       | Consumer-initiated | 3rd installment due date is also pushed 7 days.   |
| 2025-03-04 00:00:00 | feeIssued            | order-1  | installment-2  | 2.00 EUR   |                  |                     |       | Postponed Fee      | Fee associated with a single postpone request     |
| 2025-03-12 00:00:00 | installmentPaid      | order-1  | installment-2  | 50 EUR     |                  |                     |       |                    |                                                   |
| 2025-03-12 00:00:00 | feePaid              | order-1  | installment-2  | 2.00 EUR   |                  |                     |       |                    | Postponed fee being paid.                         |
| 2025-04-11 00:00:00 | installmentPaid      | order-1  | installment-3  | 50 EUR     |                  |                     |       |                    |                                                   |

### Scenario 3
Transaction with 3 installments, 2nd installment late (with fee), others paid on time.

| Effective Timestamp | Type               | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                                                 |
| ------------------- | ------------------ | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | --------------------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionCreated |          |                | 150.00 EUR | PayIn3           |                     |       |                    |                                                                 |
| 2025-02-03 00:00:00 | installmentIssued  | order-1  | installment-1  | 50 EUR     |                  | 2025-02-03 00:00:00 | 0     |                    |                                                                 |
| 2025-02-03 00:00:00 | installmentIssued  | order-1  | installment-2  | 50 EUR     |                  | 2025-03-05 00:00:00 | 1     |                    |                                                                 |
| 2025-02-03 00:00:00 | installmentIssued  | order-1  | installment-3  | 50 EUR     |                  | 2025-04-04 00:00:00 | 2     |                    |                                                                 |
| 2025-02-03 00:00:00 | installmentPaid    | order-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                                                 |
| 2025-03-08 00:00:00 | feeIssued          | order-1  | installment-2  | 3 EUR      |                  | 2025-03-05 00:00:00 |       | Late Fee           | Late fee is applied after the installment is late for > 3 days. |
| 2025-03-11 00:00:00 | installmentPaid    | order-1  | installment-2  | 50 EUR     |                  |                     |       |                    |                                                                 |
| 2025-03-11 00:00:00 | feePaid            | order-1  | installment-2  | 3 EUR      |                  |                     |       |                    | Late fee is being paid.                                         |
| 2025-04-04 00:00:00 | installmentPaid    | order-1  | installment-3  | 50 EUR     |                  |                     |       |                    |                                                                 |

### Scenario 4
Transaction with 3 installments, with €65 refund, all paid on time.

| Effective Timestamp | Type                  | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |
| ------------------- | --------------------- | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ |
| 2025-02-03 00:00:00 | transactionCreated    |          |                | 150.00 EUR | PayIn3           |                     |       |                    |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-1  | 50 EUR     |                  | 2025-02-03 00:00:00 | 0     |                    |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-2  | 50 EUR     |                  | 2025-03-05 00:00:00 | 1     |                    |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-3  | 50 EUR     |                  | 2025-04-04 00:00:00 | 2     |                    |
| 2025-02-03 00:00:00 | installmentPaid       | order-1  | installment-1  | 50 EUR     |                  |                     |       |                    |
| 2025-02-05 00:00:00 | refundIssued          |          |                | 65 EUR     |                  |                     |       |                    |
| 2025-02-05 00:00:00 | installmentRebalanced | order-1  | installment-3  | 0 EUR      |                  |                     |       | Refunded           |
| 2025-02-05 00:00:00 | installmentRebalanced | order-1  | installment-2  | 35 EUR     |                  |                     |       | Refunded           |
| 2025-03-05 00:00:00 | installmentPaid       | order-1  | installment-2  | 35 EUR     |                  |                     |       |                    |

### Scenario 5
Transaction with 1 installment (PayIn30Days), paid on time.

| Effective Timestamp | Type               | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |                                                                   |
| ------------------- | ------------------ | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- |-------------------------------------------------------------------|
| 2025-02-03 00:00:00 | transactionCreated |          |                | 150.00 EUR | PayIn30Days      |                     |       | Here this is a payment plan that only contains 1 installment.     |
| 2025-02-03 00:00:00 | installmentIssued  | order-1  | installment-1  | 150 EUR    |                  | 2025-03-05 00:00:00 | 0     | The installment is issued on Feb 3rd but it is pay 30 days later. |
| 2025-03-05 00:00:00 | installmentPaid    | order-1  | installment-1  | 150 EUR    |                  |                     |       |                                                                   |

### Scenario 6
Transaction that results in 2 orders of 3 installments, with pay on ship.

| Effective Timestamp | Type               | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index |                                                             |
| ------------------- | ------------------ | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- | ----------------------------------------------------------- |
| 2025-02-03 00:00:00 | transactionCreated |          |                | 150.00 EUR | PayIn3           |                     |       |                                                             |
| 2025-02-04 00:00:00 | installmentIssued  | order-1  | installment-1  | 33.33 EUR  |                  | 2025-02-04 00:00:00 | 0     | First shipment is made 1 day after the decision.            |
| 2025-02-04 00:00:00 | installmentIssued  | order-1  | installment-2  | 33.33 EUR  |                  | 2025-03-06 00:00:00 | 1     | 3 installments for order 1 are created.                     |
| 2025-02-04 00:00:00 | installmentIssued  | order-1  | installment-3  | 33.34 EUR  |                  | 2025-04-05 00:00:00 | 2     |                                                             |
| 2025-02-04 00:00:00 | installmentPaid    | order-1  | installment-1  | 33.33 EUR  |                  |                     |       | 1st installment for order 1 is paid on the day of shipping. |
| 2025-02-08 00:00:00 | installmentIssued  | order-2  | installment-1  | 16.66 EUR  |                  | 2025-02-08 00:00:00 | 0     | Second shipment is made 5 days after the decision.          |
| 2025-02-08 00:00:00 | installmentIssued  | order-2  | installment-2  | 16.66 EUR  |                  | 2025-03-10 00:00:00 | 1     | 3 installments for order 2 are created.                     |
| 2025-02-08 00:00:00 | installmentIssued  | order-2  | installment-3  | 16.67 EUR  |                  | 2025-04-09 00:00:00 | 2     |                                                             |
| 2025-02-08 00:00:00 | installmentPaid    | order-2  | installment-1  | 16.66 EUR  |                  |                     |       | 1st installment for order 2 is paid on the day of shipping. |
| 2025-03-06 00:00:00 | installmentPaid    | order-1  | installment-2  | 33.33 EUR  |                  |                     |       |                                                             |
| 2025-03-10 00:00:00 | installmentPaid    | order-2  | installment-2  | 16.66 EUR  |                  |                     |       |                                                             |
| 2025-04-05 00:00:00 | installmentPaid    | order-1  | installment-3  | 33.34 EUR  |                  |                     |       |                                                             |
| 2025-04-09 00:00:00 | installmentPaid    | order-2  | installment-3  | 16.67 EUR  |                  |                     |       |                                                             |

### Scenario 7
Transaction with 3 installments, and a refund greater than what the consumer already paid back.
Refund is applied from the last installment backwards.

| Effective Timestamp | Type                  | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details | Column 1                             |
| ------------------- | --------------------- | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | ------------------------------------ |
| 2025-02-03 00:00:00 | transactionCreated    |          |                | 150.00 EUR | PayIn3           |                     |       |                    |                                      |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-1  | 50 EUR     |                  | 2025-02-03 00:00:00 | 0     |                    |                                      |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-2  | 50 EUR     |                  | 2025-03-05 00:00:00 | 1     |                    |                                      |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-3  | 50 EUR     |                  | 2025-04-04 00:00:00 | 2     |                    |                                      |
| 2025-02-03 00:00:00 | installmentPaid       | order-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                      |
| 2025-02-05 00:00:00 | refundIssued          |          |                | 110 EUR    |                  |                     |       |                    |                                      |
| 2025-02-05 00:00:00 | installmentRebalanced | order-1  | installment-3  | 0 EUR      |                  |                     |       | Refunded           |                                      |
| 2025-02-05 00:00:00 | installmentRebalanced | order-1  | installment-2  | 0 EUR      |                  |                     |       | Refunded           |                                      |
| 2025-02-03 00:00:00 | installmentRebalanced | order-1  | installment-1  | 40 EUR     |                  |                     |       | Refunded           | Lender refunds the consumer card €10 |

### Scenario 8
Transaction with 3 installments, and a refund greater than what the consumer already paid back
Refund is evenly split across the 3 installments.

| Effective Timestamp | Type                  | Order ID | Installment ID | Amount     | Transaction Type | Due Timestamp       | Index | Additional Details |                                         |
| ------------------- | --------------------- | -------- | -------------- | ---------- | ---------------- | ------------------- | ----- | ------------------ | --------------------------------------- |
| 2025-02-03 00:00:00 | transactionCreated    |          |                | 150.00 EUR | PayIn3           |                     |       |                    |                                         |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-1  | 50 EUR     |                  | 2025-02-03 00:00:00 | 0     |                    |                                         |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-2  | 50 EUR     |                  | 2025-03-05 00:00:00 | 1     |                    |                                         |
| 2025-02-03 00:00:00 | installmentIssued     | order-1  | installment-3  | 50 EUR     |                  | 2025-04-04 00:00:00 | 2     |                    |                                         |
| 2025-02-03 00:00:00 | installmentPaid       | order-1  | installment-1  | 50 EUR     |                  |                     |       |                    |                                         |
| 2025-02-05 00:00:00 | refundIssued          |          |                | 110 EUR    |                  |                     |       |                    |                                         |
| 2025-02-03 00:00:00 | installmentRebalanced | order-1  | installment-1  | 13.33 EUR  |                  |                     |       | Refunded           | Lender refunds the consumer card €36.67 |
| 2025-02-05 00:00:00 | installmentRebalanced | order-1  | installment-2  | 13.33 EUR  |                  |                     |       | Refunded           |                                         |
| 2025-02-05 00:00:00 | installmentRebalanced | order-1  | installment-3  | 13.34 EUR  |                  |                     |       | Refunded           |                                         |
| 2025-03-05 00:00:00 | installmentPaid       | order-1  | installment-2  | 13.33 EUR  |                  |                     |       |                    |                                         |
| 2025-04-04 00:00:00 | installmentPaid       | order-1  | installment-3  | 13.34 EUR  |                  |                     |       |                    |                                         |
