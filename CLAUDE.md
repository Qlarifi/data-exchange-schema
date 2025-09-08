# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a schema repository for the Qlarifi BNPL (Buy Now, Pay Later) Credit Bureau platform data exchange format. It defines event schemas, field specifications, and provides scenario examples for BNPL payment plan lifecycles.

## Architecture

### Core Components

- **Event Schemas**: JSON schema definitions in `events/` directory for different event types in the BNPL lifecycle
- **Field Reference**: Complete documentation of all event fields and their requirements in `EventFieldReference.md`
- **Scenario Examples**: Realistic payment scenarios with corresponding event sequences:
  - EUR scenarios: `scenariosEUR/` (9 scenarios) with documentation in `scenariosEUR.md`
  - USD scenarios: `scenariosUSD/` (9 scenarios) with documentation in `scenariosUSD.md`

### Event Types

The schema defines two main categories of events:

1. **Identity Events**: Consumer profile management (creation, verification, updates)
   - `consumerIdentityCreated`, `consumerIdentityVerified`
   - Profile updates: phone, email, address, date of birth, name changes

2. **Credit Events**: Payment plan lifecycle management
   - Account: `accountOpened`, `accountClosed`
   - Transaction: `transactionIssued`, `transactionWrittenOff`
   - Installment: `installmentIssued`, `installmentPaid`, `installmentRebalanced`, `installmentRefunded`, `installmentWrittenOff`, `installmentCanceled`, `installmentPostponed`
   - Fees: `feePaid`, `installmentPenaltyAssessed`

### Data Structure Patterns

- All events include: `type`, `effectiveTimestamp`, core identifiers (`consumerId`, `accountId`, `transactionId`, `installmentId`)
- Monetary amounts follow `{number, currency}` structure
- Transaction types: `PayIn3`, `PayIn4`, `PayIn30Days`
- Penalty types: `LateFee`, `PostponedFee`, `Interest`, `Other`
- Each scenario includes both JSON and JSONL formats for the same data

## Working with Schemas

- Event schemas are in JSON format with example data, not JSON Schema specification
- Scenarios demonstrate real-world event sequences including fees, postponements, refunds, and write-offs
- Cross-reference `EventFieldReference.md` for detailed field descriptions and requirements
- Both EUR and USD currencies are supported with region-specific scenarios

## File Organization

- Single event examples: `events/*.json`
- Complete scenarios: `scenarios{EUR,USD}/*.{json,jsonl}`
- Documentation: `*.md` files for human-readable specifications
- Excel files: `scenarios{EUR,USD}.xlsx` contain the same data as markdown tables