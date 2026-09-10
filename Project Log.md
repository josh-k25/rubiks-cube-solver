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

## 2026-09-010

### Worked on
- Created isEdgeSolved() which checks if an edge is in its solved state (first used for white cross)
- Created getEdgeData() which returns the edge position and orientation 
- Decided on an a solving solution that roughly follows this structure for the white cross edges (focusing on replicating my own human thought process while solving it) (o = 0 --> orientation = 0 or no flip relative to solved cube):
  1. Check if edge is already in the right position (isEdgeSolved())
  2. Retreive edge pos and ori (getEdgedata())
3. Follow flowchart for solving (using UF as the target edge):
I. If located at UF with o = 0:
   - Solved, do nothing.
II. If located at FL with o = 1:
   - Do F
   - Solved.
III. If located at FR with o = 1:
   - Do F'
   - Solved.
IV. If located at DF with o = 0:
   - Do F2
   - Solved.
V. If located at DL with o = 0:
   - Do D
   - This moves it to DF with o = 0.
   - Re-check.
VI. If located at DB with o = 0:
   - Do D2
   - This moves it to DF with o = 0.
   - Re-check.
VII. If located at DR with o = 0:
   - Do D'
   - This moves it to DF with o = 0.
   - Re-check.
VIII. If located at FL with o = 0:
   - Do L'
   - This moves it to UL with o = 0.
   - Re-check.
IX. If located at FR with o = 0:
   - Do R
   - This moves it to UR with o = 0.
   - Re-check.
X. If located at BL with o = 0:
   - Do L
   - This moves it to UL with o = 0.
   - Re-check.
XI. If located at BR with o = 0:
   - Do R'
   - This moves it to UR with o = 0.
   - Re-check.
XII. If located at UR with o = 0:
   - Do U
   - Solved.
XIII. If located at UL with o = 0:
   - Do U'
   - Solved.
XIV. If located at UB with o = 0:
   - Do U2
   - Solved.
XV. If located at DL with o = 1:
   - Do L'
   - This moves it to FL with o = 1.
   - Re-check.
XVI. If located at DR with o = 1:
   - Do R
   - This moves it to FR with o = 1.
   - Re-check.
XVII. If located at DB with o = 1:
   - Do D
   - This moves it to DL with o = 1.
   - Re-check.
XVIII. If located at DF with o = 1:
   - Do F
   - This moves it to FL with o = 0.
   - Re-check.
XIX. If located at UL with o = 1:
   - Do L
   - This moves it to FL with o = 1.
   - Re-check.
XX. If located at UR with o = 1:
   - Do R'
   - This moves it to FR with o = 1.
   - Re-check.
XXI. If located at UB with o = 1:
   - Do U
   - This moves it to UR with o = 1.
   - Re-check.
XXII. If located at UF with o = 1:
   - Do U
   - This moves it to UL with o = 1.
   - Re-check.
XXIII. If located at BL with o = 1:
   - Do L2
   - This moves it to FL with o = 1.
   - Re-check.
XXIV. If located at BR with o = 1:
   - Do R2
   - This moves it to FR with o = 1.
   - Re-check.