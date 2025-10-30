# ocr-email-parser
What does this project do?

## Assumptions
- fastAPI project
- some kind of model needs to be loaded

## Deployment
- fast deployment via `docker-compose up`
- prod config in `docker-compose.override.yml`
### Requirements

## Development
- Run tests with `make test`
- Lint with `lint`. Additional flake8 check via `lint-check`
### Devcontainer (recommended)
- VS Code required
- Needs the dev containers extension https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

### Local dev
- Set up by running `make setup-local && make setup-dev-local`