# Akshit Kobagapu — Personal Website

This is my personal website, built with Sphinx!
It is hosted on GitHub Pages and available at [akshitkobagapu.com](https://akshitkobagapu.com).

## Contributing

The project uses UV for dependencies management and [pypeline](https://github.com/cuinixam/pypeline) for streamlining the development workflow.
Use pipx (or your favorite package manager) to install the `pypeline` in an isolated environment:

```shell
pipx install pypeline-runner
```

To bootstrap the project and run all the steps configured in the `pypeline.yaml` file, execute the following command:

```shell
pypeline run
```

For those using [VS Code](https://code.visualstudio.com/) there are tasks defined for the most common commands:

- run tests
- run pre-commit checks (linters, formatters, etc.)
- generate documentation

See the `.vscode/tasks.json` for more details.
