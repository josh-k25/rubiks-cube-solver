# Project Log

## 2026-09-07

### Worked on
- Cubie (one individual piece of a Rubix Cube) representation
- rotateLeft helper

### Learned
- Functions and enums (for Python)
- Moves are permutations of cubies plus orientation changes.

### Problems
- Still need to figure out how to make the move functions

### Next
- Work through U and F manually.
- Create and test move functions on cube model

## 2026-09-08

### Worked on
- Mapping for move function
- Mapping takes current cube and provides the next orientation and position of edges and corners based on move type

### Learned
- Kociembas way of describing cubies with a deeper understanding (Probably going to stick with this notation for now it should port to hardware well)

### Problems
- Still need to figure out how to write the move function

### Next
- Create and test move functions on cube model

## 2026-09-09

### Worked on
- Created `applyMove` method.
- Created identity test to prove that applying the same quarter-turn 4 times returns the cube to its original state.
- Added support for all 18 standard moves by representing double and prime moves as repeated applications of the 6 base moves.
- Created a `MOVE_DEFINITIONS` dictionary that maps a requested move to its base move and number of repetitions.
- Added a white-cross solved checker.
- Started planning the structure for the white-cross solving control logic.
- Decided to separate cube representation/move mechanics from solver logic into different files.


### Learned
- A dictionary uses a key to reference associated data.
- Tuple unpacking can assign multiple values from a tuple at once.
- Move.R, for example, is an enum member while Move is the enum class.
- The six base move tables only need to describe the fundamental quarter-turns. Prime and double moves can be built from repeated base moves.
- Cubie identity already contains color information. For example, Edge.UF represents the physical U-F edge, so an extra color field is unnecessary.
- Phase-checking logic and solving logic should be kept separate:
  - A checker asks whether a condition is currently satisfied.
  - The solver decides which moves should be performed next.
- Solving control logic will hasve the rough structure off the following (FSM will also look similar)
  - inspect cube state
  - classify current case
  - choose move
  - apply move
  - inspect state again

### Problems
- Need to design the control logic for actually solving the white cross.
- Need to decide how to classify the possible position/orientation cases for an individual white edge.
- Need a clean way for the solver to locate a specific cubie in the current state.

### Next
- Create a findEdge() helper that determines which position currently contains a requested edge cubie.
- Create an isEdgeSolved() helper for checking one target edge.
- Write down the manual solving process for that edge based on:
  - its current position
  - its current orientation
- Translate those decisions into white-cross control logic.
- Test solving one edge from several different locations before generalizing to all four white edges.
- Only after individual white-edge solving works, build `solveWhiteCross()`.