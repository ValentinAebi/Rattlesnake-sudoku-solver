# Rattlesnake sudoku solver

A sudoku solver, written in [Rattlesnake](https://github.com/ValentinAebi/Rattlesnake)

The grid must be hardcoded in `src/main.rsn`. To run the solver, run `make` in cmd (the default target of the Makefile triggers the compiler via a Python script). Can also be done by manually running the compiler jar file:
```
java -jar Rattlesnake.jar run src/main.rsn src/solver.rsn src/grid.rsn src/grid_check.rsn src/util.rsn
```

`.vscode/settings.json` contains settings to (approximately) highlight Rattlesnake syntax using the [Highlight](https://github.com/fabiospampinato/vscode-highlight) Visual Studio Code extension.
