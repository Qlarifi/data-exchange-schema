# Event Field Reference

### ConsumerIdentityCreated
* **type**: Indicates the event type. Always consumerIdentityCreated.
* **effectiveTimestamp**: The timestamp when the consumer identity was created.
* **consumerId**: Unique identifier for the consumer (from the lender).
* **name**: Object containing the consumer's name. The type field indicates the name type (westernName in this example).
* **dateOfBirth**: The consumer's date of birth.
* **phone**: The consumer's phone number.
* **email**: The consumer's email address.
* **address**: Object containing the consumer's address. The type field indicates the address type (euAddress shown, but others are possible).

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
* **address**: Object containing the consumer's updated address. The type field indicates the address type.

### ConsumerDateOfBirthChanged
* **type**: Indicates the event type. Always consumerDateOfBirthChanged.
* **effectiveTimestamp**: The timestamp when the date of birth was changed.
* **consumerId**: Unique identifier for the consumer.
* **dateOfBirth**: The consumer's updated date of birth.

### ConsumerNameChanged
* **type**: Indicates the event type. Always consumerNameChanged.
* **effectiveTimestamp**: The timestamp when the name was changed.
* **consumerId**: Unique identifier for the consumer.
* **name**: Object containing the consumer's updated name. The type field indicates the name type.


## Lender Credit Events

## Transaction Events

### TransactionIssued
* **type**: Indicates the event type; always "transactionIssued".
* **transactionId**: A unique identifier for the transaction.
* **consumerId**: A unique identifier for the consumer who owes this transaction (from the lender).
* **amount.number**: The monetary amount of this transaction.
* **amount.currency**: The currency of the amount.
* **issuedInstallments**: Array of installments issued with the transaction.
  * **installmentId**: Unique identifier for the installment.
  * **amount.number**: The monetary amount due for this installment.
  * **amount.currency**: The currency of the amount.
  * **dueTimestamp**: ISO 8601 timestamp when this installment is due.
  * **index**: The sequential order of this installment within the transaction (0-based).
* **transactionType**: The type of transaction product. Possible values are: "PayIn3", "PayIn4", "PayIn30Days".
* **metadata**: Additional metadata about the transaction.
* **effectiveTimestamp**: ISO 8601 timestamp when the transaction was issued.

### TransactionApproved
* **type**: Indicates the event type; always "transactionApproved".
* **transactionId**: A unique identifier for the approved transaction.
* **consumerId**: A unique identifier for the consumer.
* **effectiveTimestamp**: ISO 8601 timestamp when the transaction was approved.
* **metadata**: Additional metadata about the approval.

### TransactionDeclined
* **type**: Indicates the event type; always "transactionDeclined".
* **transactionId**: A unique identifier for the declined transaction.
* **consumerId**: A unique identifier for the consumer.
* **effectiveTimestamp**: ISO 8601 timestamp when the transaction was declined.
* **metadata**: Additional metadata about the decline.

### TransactionCanceled
* **type**: Indicates the event type; always "transactionCanceled".
* **transactionId**: A unique identifier for the canceled transaction.
* **consumerId**: A unique identifier for the consumer.
* **effectiveTimestamp**: ISO 8601 timestamp when the transaction was canceled.
* **metadata**: Additional metadata about the cancellation.

### TransactionPaidOff
* **type**: Indicates the event type; always "transactionPaidOff".
* **transactionId**: A unique identifier for the paid off transaction.
* **consumerId**: A unique identifier for the consumer.
* **paymentId**: (Optional) The ID of the payment that paid off the transaction.
* **refundId**: (Optional) The ID of the refund that contributed to paying off the transaction.
* **effectiveTimestamp**: ISO 8601 timestamp when the transaction was paid off.
* **metadata**: Additional metadata about the payoff.

### TransactionRefunded
* **type**: Indicates the event type; always "transactionRefunded".
* **refundId**: A unique identifier for the refund.
* **transactionId**: A unique identifier for the refunded transaction.
* **consumerId**: A unique identifier for the consumer.
* **amount.number**: The monetary amount of the refund.
* **amount.currency**: The currency of the refund.
* **rebalancedInstallments**: Array of installments that were rebalanced due to the refund.
  * **installmentId**: Unique identifier for the rebalanced installment.
  * **amount.number**: The new amount owed on the installment.
  * **amount.currency**: The currency of the amount.
* **rebalancedFees**: Array of fees that were rebalanced due to the refund.
  * **feeId**: Unique identifier for the rebalanced fee.
  * **amount.number**: The new amount owed on the fee.
  * **amount.currency**: The currency of the amount.
* **effectiveTimestamp**: ISO 8601 timestamp when the refund was processed.
* **metadata**: Additional metadata about the refund.

### TransactionWrittenOff
* **type**: Indicates the event type; always "transactionWrittenOff".
* **transactionId**: A unique identifier for the written off transaction.
* **consumerId**: A unique identifier for the consumer.
* **amount.number**: The monetary amount that was written off.
* **amount.currency**: The currency of the written off amount.
* **effectiveTimestamp**: ISO 8601 timestamp when the transaction was written off.
* **metadata**: Additional metadata about the write-off.

## Installment Events

### InstallmentPaidOff
* **type**: Indicates the event type; always "installmentPaidOff".
* **installmentId**: A unique identifier for the paid off installment.
* **transactionId**: A unique identifier for the transaction the installment belongs to.
* **consumerId**: A unique identifier for the consumer.
* **paymentId**: (Optional) The ID of the payment that paid off the installment.
* **refundId**: (Optional) The ID of the refund that contributed to paying off the installment.
* **effectiveTimestamp**: ISO 8601 timestamp when the installment was paid off.
* **metadata**: Additional metadata about the payoff.

### InstallmentCanceled
* **type**: Indicates the event type; always "installmentCanceled".
* **installmentId**: A unique identifier for the canceled installment.
* **transactionId**: A unique identifier for the transaction the installment belongs to.
* **consumerId**: A unique identifier for the consumer.
* **effectiveTimestamp**: ISO 8601 timestamp when the installment was canceled.
* **metadata**: Additional metadata about the cancellation.

### InstallmentDefaulted
* **type**: Indicates the event type; always "installmentDefaulted".
* **installmentId**: A unique identifier for the defaulted installment.
* **transactionId**: A unique identifier for the transaction the installment belongs to.
* **consumerId**: A unique identifier for the consumer.
* **effectiveTimestamp**: ISO 8601 timestamp when the installment was marked as defaulted.
* **metadata**: Additional metadata about the default.

### InstallmentPostponed
* **type**: Indicates the event type; always "installmentPostponed".
* **installmentId**: A unique identifier for the postponed installment.
* **transactionId**: A unique identifier for the transaction the installment belongs to.
* **consumerId**: A unique identifier for the consumer.
* **newDueTimestamp**: ISO 8601 timestamp for the new due date of the installment.
* **postponedType**: (Optional) The type/reason for postponement (e.g., "Consumer").
* **effectiveTimestamp**: ISO 8601 timestamp when the postponement was applied.
* **metadata**: Additional metadata about the postponement.

### InstallmentRebalanced
* **type**: Indicates the event type; always "installmentRebalanced".
* **installmentId**: A unique identifier for the rebalanced installment.
* **transactionId**: A unique identifier for the transaction the installment belongs to.
* **consumerId**: A unique identifier for the consumer.
* **amount.number**: The new amount due on the installment after the rebalance.
* **amount.currency**: The currency of the new amount due.
* **reason**: (Optional) The reason for the rebalance.
* **effectiveTimestamp**: ISO 8601 timestamp when the rebalance occurred.
* **metadata**: Additional metadata about the rebalance.


### InstallmentWrittenOff
* **type**: Indicates the event type; always "installmentWrittenOff".
* **installmentId**: A unique identifier for the written off installment.
* **transactionId**: A unique identifier for the transaction the installment belongs to.
* **consumerId**: A unique identifier for the consumer.
* **amount.number**: The monetary amount that was written off.
* **amount.currency**: The currency of the written off amount.
* **effectiveTimestamp**: ISO 8601 timestamp when the installment was written off.
* **metadata**: Additional metadata about the write-off.

## Fee Events



### FeeIssued
* **type**: Indicates the event type; always "feeIssued".
* **feeId**: A unique identifier for the fee.
* **transactionId**: A unique identifier for the transaction the fee is associated with.
* **consumerId**: A unique identifier for the consumer who incurred the fee.
* **amount.number**: The monetary amount of the fee.
* **amount.currency**: The currency of the fee.
* **effectiveTimestamp**: ISO 8601 timestamp when the fee was issued.
* **metadata**: Additional metadata about the fee.

### FeeCanceled
* **type**: Indicates the event type; always "feeCanceled".
* **feeId**: A unique identifier for the canceled fee.
* **transactionId**: A unique identifier for the transaction the fee was associated with.
* **consumerId**: A unique identifier for the consumer.
* **effectiveTimestamp**: ISO 8601 timestamp when the fee was canceled.
* **metadata**: Additional metadata about the cancellation.

### FeePaidOff
* **type**: Indicates the event type; always "feePaidOff".
* **feeId**: A unique identifier for the paid off fee.
* **transactionId**: A unique identifier for the transaction the fee was associated with.
* **consumerId**: A unique identifier for the consumer.
* **paymentId**: (Optional) The ID of the payment that paid off the fee.
* **effectiveTimestamp**: ISO 8601 timestamp when the fee was paid off.
* **metadata**: Additional metadata about the payoff.

### FeeRebalanced
* **type**: Indicates the event type; always "feeRebalanced".
* **feeId**: A unique identifier for the rebalanced fee.
* **transactionId**: A unique identifier for the transaction the fee is associated with.
* **consumerId**: A unique identifier for the consumer.
* **amount.number**: The new amount due on the fee after the rebalance.
* **amount.currency**: The currency of the new amount due.
* **effectiveTimestamp**: ISO 8601 timestamp when the rebalance occurred.
* **metadata**: Additional metadata about the rebalance.

### FeeWrittenOff
* **type**: Indicates the event type; always "feeWrittenOff".
* **feeId**: A unique identifier for the written off fee.
* **transactionId**: A unique identifier for the transaction the fee was associated with.
* **consumerId**: A unique identifier for the consumer.
* **amount.number**: The monetary amount that was written off.
* **amount.currency**: The currency of the written off amount.
* **effectiveTimestamp**: ISO 8601 timestamp when the fee was written off.
* **metadata**: Additional metadata about the write-off.

## Payment Events

### PaymentAuthorized
* **type**: Indicates the event type; always "paymentAuthorized".
* **paymentId**: A unique identifier for the payment.
* **transactionId**: A unique identifier for the transaction the payment is associated with.
* **consumerId**: A unique identifier for the consumer who made the payment.
* **amount.number**: The monetary amount of the payment.
* **amount.currency**: The currency of the payment.
* **paymentDetails**: Object containing payment method details.
  * **type**: The payment method type (e.g., "card").
  * **last4**: Last 4 digits of the payment method (for cards).
  * **brand**: Brand of the payment method (e.g., "visa", "mastercard").
* **effectiveTimestamp**: ISO 8601 timestamp when the payment was authorized.
* **metadata**: Additional metadata about the authorization.

### PaymentCaptured
* **type**: Indicates the event type; always "paymentCaptured".
* **paymentId**: A unique identifier for the payment.
* **transactionId**: A unique identifier for the transaction the payment is associated with.
* **consumerId**: A unique identifier for the consumer who made the payment.
* **amount.number**: The monetary amount of the payment.
* **amount.currency**: The currency of the payment.
* **paymentDetails**: Object containing payment method details.
  * **type**: The payment method type (e.g., "card").
  * **last4**: Last 4 digits of the payment method (for cards).
  * **brand**: Brand of the payment method (e.g., "visa", "mastercard").
* **effectiveTimestamp**: ISO 8601 timestamp when the payment was captured.
* **metadata**: Additional metadata about the capture.

### PaymentFailed
* **type**: Indicates the event type; always "paymentFailed".
* **paymentId**: A unique identifier for the failed payment.
* **transactionId**: A unique identifier for the transaction the payment was associated with.
* **consumerId**: A unique identifier for the consumer who attempted the payment.
* **amount.number**: The monetary amount of the attempted payment.
* **amount.currency**: The currency of the attempted payment.
* **reason**: The reason for the payment failure. Possible values include: "InsufficientFunds", "CardDeclined", "ExpiredCard", etc.
* **paymentDetails**: Object containing payment method details.
  * **type**: The payment method type (e.g., "card").
  * **last4**: Last 4 digits of the payment method (for cards).
  * **brand**: Brand of the payment method (e.g., "visa", "mastercard").
* **effectiveTimestamp**: ISO 8601 timestamp when the payment failed.
* **metadata**: Additional metadata about the failure.

