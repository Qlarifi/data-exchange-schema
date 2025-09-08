# Event Field Reference

## Qlarifi Identity Events

### ConsumerIdentityCreated
* **type**: Indicates the event type. Always consumerIdentityCreated.
* **effectiveTimestamp**: The timestamp when the consumer identity was created.
* **consumerId**: Unique identifier for the consumer (from the lender).
* **name.type**: The type of name object. Always "WesternName".
* **name.first**: The consumer's first name.
* **name.last**: The consumer's last name.
* **dateOfBirth**: The consumer's date of birth.
* **phone**: The consumer's phone number.
* **email**: The consumer's email address.
* **address.type**: The type of address. Always "USAddress" for now.
* **address.streetAddress1**: The first line of the street address.
* **address.streetAddress2**: The second line of the street address (if any).
* **address.city**: The city of the address.
* **address.state**: The state or region of the address.
* **address.zipCode**: The postal code of the address.

### ConsumerIdentityVerified
* **type**: Indicates the event type. Always consumerIdentityVerified.
* **effectiveTimestamp**: The timestamp when the consumer identity was verified.
* **consumerId**: Unique identifier for the consumer (from the lender).
* **verificationType**: Type of verification done by the third party. The final list of possible values are still to be finalized and discussed with the lenders.

### ConsumerPhoneChanged
* **type**: Indicates the event type. Always consumerPhoneChanged.
* **effectiveTimestamp**: The timestamp when the phone number was changed.
* **consumerId**: Unique identifier for the consumer.
* **phone**: The consumer's updated phone number.

### ConsumerEmailChanged
* **type**: Indicates the event type. Always consumerEmailChanged.
* **effectiveTimestamp**: The timestamp when the email address was changed.
* **consumerId**: Unique identifier for the consumer.
* **email**: The consumer's updated email address.

### ConsumerAddressChanged
* **type**: Indicates the event type. Always consumerAddressChanged.
* **effectiveTimestamp**: The timestamp when the address was changed.
* **consumerId**: Unique identifier for the consumer.
* **address.type**: The type of address. Always "USAddress" for now.
* **address.streetAddress1**: The first line of the street address.
* **address.streetAddress2**: The second line of the street address (if any).
* **address.city**: The city of the address.
* **address.state**: The state or region of the address.
* **address.zipCode**: The postal code of the address.

### ConsumerDateOfBirthChanged
* **type**: Indicates the event type. Always consumerDateOfBirthChanged.
* **effectiveTimestamp**: The timestamp when the date of birth was changed.
* **consumerId**: Unique identifier for the consumer.
* **dateOfBirth**: The consumer's updated date of birth.

### ConsumerNameChanged
* **type**: Indicates the event type. Always consumerNameChanged.
* **effectiveTimestamp**: The timestamp when the name was changed.
* **consumerId**: Unique identifier for the consumer.
* **name.type**: The type of name object. Always "WesternName".
* **name.first**: The consumer's first name.
* **name.last**: The consumer's last name.

## Qlarifi Credit Events

### AccountOpened
* **type**: Indicates the event type; in this case, accountOpened.
* **effectiveTimestamp**: The timestamp (UTC) when the account was opened from the lender's perspective.
* **accountId**: A unique identifier for this account.
* **consumerId**: A unique identifier for the consumer who owns this account (as defined by the lender).

### AccountClosed
* **type**: Indicates the event type; in this case, accountClosed.
* **effectiveTimestamp**: The timestamp (UTC) when the account was closed from the lender's perspective.
* **accountId**: A unique identifier for this account.
* **consumerId**: A unique identifier for the consumer who owns this account (as defined by the lender).

### TransactionIssued
* **type**: Indicates the event type; in this case, transactionIssued.
* **effectiveTimestamp**: The timestamp (UTC) when the transaction was issued from the lender's perspective.
* **transactionId**: A unique identifier for the transaction.
* **accountId**: A unique identifier for the account this transaction is associated with.
* **consumerId**: A unique identifier for the consumer who owes this transaction (as defined by the lender).
* **amount.number**: The monetary amount of this transaction.
* **amount.currency**: The currency of the amount.
* **transactionType**: The type of transaction product, Possible values are: PayIn3, PayIn4, PayIn30Days.

### InstallmentIssued
* **type**: Indicates the event type; in this case, installmentIssued.
* **effectiveTimestamp**: The timestamp (UTC) when the instalment was issued from the lender's perspective.
* **installmentId**: A unique identifier for this specific instalment.
* **transactionId**: A unique identifier for the transaction this instalment belongs to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId**: A unique identifier for the consumer who owes this instalment (as defined by the lender).
* **amount.number**: The monetary amount due for this instalment.
* **amount.currency**: The currency of the amount.
* **dueTimestamp**: The date and time (UTC) when this instalment is due.
* **index**: The sequential order of this instalment within the transaction.

### InstallmentPaid
* **type**: Indicates the event type; in this case, installmentPaid.
* **effectiveTimestamp**: The timestamp (UTC) when the payment was made from the lender's perspective.
* **installmentId**: The unique identifier of the instalment that received the payment.
* **transactionId**: The unique identifier of the transaction the instalment belongs to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId** [optional]: The unique identifier of the consumer who made the payment.
* **amount.number**: The amount paid towards the instalment.
* **amount.currency**: The currency of the payment.

### InstallmentRebalanced
* **type**: Indicates the event type; in this case, installmentRebalanced.
* **effectiveTimestamp**: The timestamp (UTC) when the rebalance occurred from the lender's perspective.
* **installmentId**: The unique identifier of the instalment that was rebalanced.
* **transactionId**: The unique identifier of the transaction the instalment belongs to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId** [optional]: The unique identifier of the consumer affected by the rebalance.
* **newAmountDue.number**: The new amount due on the instalment after the rebalance.
* **newAmountDue.currency**: The currency of the new amount due.

### InstallmentRefunded
* **type**: Indicates the event type; in this case, installmentRefunded.
* **effectiveTimestamp**: The timestamp (UTC) when the refund was issued from the lender's perspective.
* **installmentId**: The unique identifier of the instalment that was refunded.
* **transactionId**: The unique identifier of the transaction the instalment belongs to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId**: The unique identifier of the consumer who received the refund.
* **refundAmount.number**: The amount of the refund issued.
* **refundAmount.currency**: The currency of the refund.

### InstallmentWrittenOff
* **type**: Indicates the event type; in this case, installmentWrittenOff.
* **effectiveTimestamp**: The timestamp (UTC) when the write-off occurred from the lender's perspective.
* **installmentId**: The unique identifier of the instalment that was written off.
* **transactionId**: The unique identifier of the transaction the instalment belongs to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId**: The unique identifier of the consumer whose instalment was written off.

### InstallmentCanceled
* **type**: Indicates the event type; in this case, installmentCanceled.
* **effectiveTimestamp**: The timestamp (UTC) when the cancellation occurred from the lender's perspective.
* **installmentId**: The unique identifier of the cancelled instalment.
* **transactionId**: The unique identifier of the transaction the instalment belonged to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId**: The unique identifier of the consumer affected by the cancellation.

### InstallmentPostponed
* **type**: Indicates the event type; in this case, installmentPostponed.
* **effectiveTimestamp**: The timestamp (UTC) when the installment was postponed from the lender's perspective.
* **installmentId**: The unique identifier of the instalment postponed.
* **transactionId**: The unique identifier of the transaction the instalment belongs to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId**: The unique identifier of the consumer the instalment belongs to.
* **feeAmount.number**: The amount of the fee.
* **feeAmount.currency**: The currency of the fee.
* **postponedType**: The type of postponed action. Possible values are Customer, LenderCommercial, LenderTechnical.

### InstallmentPenaltyAssessed
* **type**: Indicates the event type; in this case, installmentPenaltyAssessed.
* **effectiveTimestamp**: The timestamp (UTC) when the penalty was assessed from the lender's perspective.
* **installmentId**: The unique identifier of the instalment with the assessed penalty.
* **transactionId**: The unique identifier of the transaction the instalment belongs to.
* **accountId**: A unique identifier for the account this instalment is associated with.
* **consumerId**: The unique identifier of the consumer who incurred the penalty.
* **penaltyAmount.number**: The amount of the penalty assessed.
* **penaltyAmount.currency**: The currency of the penalty.
* **penaltyType**: The type of penalty fee that was added to the transaction amount. Possible values are: LateFee, PostponedFee,Interest, Other.

### FeePaid
* **type**: Indicates the event type; in this case, feePaid.
* **effectiveTimestamp**: The timestamp (UTC) when the fee was paid from the lender's perspective.
* **installmentId** [optional]: The unique identifier of the instalment associated with the fee.
* **transactionId**: The unique identifier of the transaction associated with the fee.
* **accountId**: A unique identifier for the account this fee is associated with.
* **consumerId**: The unique identifier of the consumer who incurred the fee.
* **amount.number**: The amount paid.
* **amount.currency**: The currency of the payment.

### TransactionWrittenOff
* **type**: Indicates the event type; in this case, transactionWrittenOff.
* **effectiveTimestamp**: The timestamp (UTC) when the write-off occurred from the lender's perspective.
* **transactionId**: The unique identifier of the transaction written off.
* **accountId**: A unique identifier for the account this transaction is associated with.
* **consumerId**: The unique identifier of the consumer whose transaction was written off.
