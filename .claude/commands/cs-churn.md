# /cs-churn

Analyze churn risk for an account and build a 30-day save plan.

## Usage
```
/cs-churn [account name] [paste health signals, usage data, or situation description]
```

## Example
```
/cs-churn Acme Corp — low login frequency last 30 days, champion left, renewal in 45 days
```

Invokes the `customer-success-claude` skill → Churn Risk Analysis prompt.

$ARGUMENTS
