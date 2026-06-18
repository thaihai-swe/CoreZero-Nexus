# Example Domain — Anti-Patterns

Known failure modes for this domain. Replace with your domain's actual anti-patterns.

## **Anemic Domain Model**

**Why it fails:** Domain objects become data bags with no behavior. Business rules scatter
across services and utilities, making them impossible to enforce consistently.

**What to do instead:** Put behavior on domain objects. Validation and state transitions
belong on the entity, not on a service that wraps it.

**Citation:** Common failure mode in service-heavy architectures.

---

## **Leaking Infrastructure Concerns into the Domain**

**Why it fails:** Domain logic becomes coupled to database schemas, HTTP details, or
messaging formats. Changing infrastructure requires touching domain code.

**What to do instead:** Define domain interfaces (ports). Let infrastructure implement them
(adapters). The domain depends on abstractions, not implementations.

**Citation:** Common failure mode in layered architectures.
