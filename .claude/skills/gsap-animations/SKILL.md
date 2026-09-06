# GSAP Animations (GreenSock Animation Platform)

Official GreenSock skill for Claude Code. Build professional, timeline-based animations with ScrollTrigger, text reveals, and React integration.

## Install

```bash
npm install gsap
```

## Core Concepts

### Timeline-based animations

```js
import { gsap } from "gsap";

const tl = gsap.timeline({ defaults: { ease: "power2.out", duration: 0.6 } });

tl.from(".hero-title", { y: 60, opacity: 0 })
  .from(".hero-sub", { y: 40, opacity: 0 }, "-=0.3")
  .from(".hero-cta", { scale: 0.8, opacity: 0 }, "-=0.2");
```

### ScrollTrigger support

```js
import { ScrollTrigger } from "gsap/ScrollTrigger";
gsap.registerPlugin(ScrollTrigger);

gsap.from(".card", {
  scrollTrigger: {
    trigger: ".card",
    start: "top 80%",
    toggleActions: "play none none reverse",
  },
  y: 80,
  opacity: 0,
  stagger: 0.15,
});
```

### Smooth text reveal effects

```js
import { SplitText } from "gsap/SplitText";
gsap.registerPlugin(SplitText);

const split = new SplitText(".headline", { type: "words,chars" });
gsap.from(split.chars, {
  opacity: 0,
  y: 20,
  stagger: 0.02,
  duration: 0.5,
  ease: "back.out(1.7)",
});
```

### Easy React integration

```jsx
import { useGSAP } from "@gsap/react";
import { useRef } from "react";

gsap.registerPlugin(useGSAP);

export function AnimatedCard() {
  const container = useRef(null);

  useGSAP(() => {
    gsap.from(".card", { y: 50, opacity: 0, stagger: 0.1 });
  }, { scope: container });

  return <div ref={container}><div className="card">Hello</div></div>;
}
```

## Prompt

```
Act as a GSAP animation expert. I need to animate [element/component].
Requirements:
- Timeline: [sequential / parallel / staggered]
- Trigger: [on load / on scroll / on hover / on click]
- Ease: [power2 / elastic / bounce / back]
- Duration: [fast 0.3s / normal 0.6s / slow 1s+]
- React: [yes / no]

Write clean GSAP code with comments explaining each tween.
```
