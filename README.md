# Data Exchange Schema

This serves as the source of truth for the data exchange schema used to contribute data to the Qlarifi BNPL Credit Bureau platform.
It contains the definition of the events, fields, along with various scenario examples that help understand how the data is formatted.

## Events
We have defined a set of events that represent the different actions and states in the payment plan lifecycle. Each event has a specific structure and fields that need to be populated when the event is triggered.
The events are documented in the [Event Field Reference](./EventFieldReference.md) document.

## Scenarios
We have put together a few scenarios to align on the data exchange schema. These scenarios are based on the payment plan types and the possible transactions that can occur within them. The scenarios are not exhaustive but should cover the most common cases.

For European customers, we have listed the scenarios in the [EU Scenarios](./scenariosEUR.md) document.
For US customers, we have listed the scenarios in the [US Scenarios](./scenariosUSD.md) document.
