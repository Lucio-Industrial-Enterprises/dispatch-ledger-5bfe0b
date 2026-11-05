# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars. Zones are `local` and `regional`; weights must be positive.
Service is `"standard"` (default) or `"express"`. Express shipping costs $7
more than the equivalent standard quote.

The command-line entry point prints a quote for an order:

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
python -m warehouse.cli 2 local                    # $8.00
python -m warehouse.cli 2 local --service express  # $15.00
```
