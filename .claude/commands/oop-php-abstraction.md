---
description: Abstraction in PHP OOP — hiding complexity behind abstract classes, with worked Report/SalesReport code examples and interface-vs-abstract-class guidance
argument-hint: [your own class pair to apply this to, or "compare" for interface vs abstract class]
---

# OOP in PHP — Abstraction (5/6)

Source: @alexxcodes, "OOP in PHP" carousel series. This series covers 6 OOP concepts in order — **Classes, Encapsulation, Inheritance, Polymorphism, Abstraction, Composition** — numbered as a "05/06" post with "Next up: Composition." Only the **Abstraction** chapter's slides were captured in this source; the other 5 topics are named above by title only and are not detailed here — they weren't shown, so they aren't guessed at.

## Core idea: hide the complexity

Abstraction shows what an object *does* and hides *how* it does it. "Expose the what, hide the how."

## Interface vs. abstract class

| | Interface | Abstract class |
|---|---|---|
| **Contains** | Only signatures | Signatures + code |
| **A class can** | Implement many | Extend just one |
| **Use it for** | Same ability, unrelated classes | Shared base, closely related classes |

## Worked example

Abstract classes share logic and force the rest:

```php
abstract class Report
{
    public function render(): string
    {
        return $this->title() . $this->body();
    }

    abstract protected function title(): string;
    abstract protected function body(): string;
}
```

Each child fills in the blanks:

```php
class SalesReport extends Report
{
    protected function title(): string
    {
        return 'Sales';
    }

    protected function body(): string
    {
        return '42 orders';
    }
}
```

You can't instantiate abstract — only concrete children can be created:

```php
new Report();      // Error
new SalesReport();  // OK
```

## Plain-text prompt to apply this to your own code

```
I have these related classes: [PASTE 2+ CLASSES THAT SHARE LOGIC BUT DIFFER
IN SOME DETAILS]. Refactor them using PHP abstraction: pull the shared
logic into an abstract base class with concrete methods, declare the
varying pieces as abstract protected methods each child must implement,
and show me the resulting abstract class plus one concrete child. Then
tell me whether an interface would fit better than an abstract class here,
and why.
```
