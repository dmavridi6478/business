# /cs-renewal

Write a renewal email for a customer account.

## Usage
```
/cs-renewal [account name] [renewal date] [context: wins, issues, upsell opportunity]
```

## Example
```
/cs-renewal Acme Corp October 15 — strong ROI year, minor support issues resolved, expansion opportunity in EMEA
```

Invokes the `customer-success-claude` skill → Renewal Email prompt.

$ARGUMENTS
