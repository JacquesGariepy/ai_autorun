# Testing and Validation

The AI must identify the real commands for the project.

Typical commands:

## Node
npm install
npm run build
npm test
npm run lint

## .NET
dotnet restore
dotnet build
dotnet test

## Python
python -m pip install -r requirements.txt
pytest

## Java
mvn test
gradle test

## AI Feature Validation
- prompt schema tests
- response schema tests
- model routing tests
- fallback tests
- rate-limit tests
- budget-stop tests
- cache tests
- prompt injection tests
- regression evals

Minimum validation if no tests exist:
- build or compilation
- local launch
- documented manual test
- one critical scenario
- console output capture
- explicit limitations
