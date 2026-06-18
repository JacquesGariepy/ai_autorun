# Unfinished Work Audit

Search for unfinished or suspicious work.

Signals:
- TODO
- FIXME
- HACK
- WIP
- NotImplemented
- NotImplementedException
- throw new Error("not implemented")
- console.log
- debugger
- return null
- return undefined
- return ""
- return []
- mock
- fake
- temporary
- placeholder
- sample data
- test data in production
- commented-out code
- skipped tests
- only tests
- empty methods
- empty catch blocks
- unreachable branches
- dead services
- registered but unused commands
- UI buttons without handlers
- endpoints without implementation
- configuration never used
- model configured but never called
- prompt defined but never tested
- AI response parsed without validation

Output:
| file | line | type | finding | impact | recommended fix | priority |
