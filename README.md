# Octave Coordinate Prime Visualizer

A harmonic reimagining of prime numbers — visualized within a single octave to reveal their hidden ratios and structures.

---

## Purpose

This project maps pure prime numbers into the space of one musical octave (1 to 2 in frequency ratio) by dividing out powers of two. The resulting value, the octave coordinate, reflects the unique harmonic identity of each prime, independent of scale.

---

## Core Concepts

### Octave Normalization:
Each prime number is divided by 2 repeatedly until it falls within the 1 to 2 range. The final decimal value becomes its coordinate on the graph.

### Prime-Only Visualization:
Only pure primes are shown — no composite numbers or factorizations. This isolates and emphasizes their distribution in the octave space.

### Ratio-Based Scale:
The display uses even pitch-ratio spacing, similar to a slide rule. Visual spacing is determined by each prime’s ratio within the octave.

---

## Display Requirements

* **Horizontal axis** represents the octave range (1 to 2).
* Each prime is represented by a **vertical line/band**:
    * Approximately ¼ inch wide at default zoom.
    * Fixed visual width (not shrinking at lower zoom).
* **Color Modes**:
    * **Neutral mode**: all bands are the same color (for density clarity).
    * **Gradient mode**: colors based on prime magnitude.
    * **Toggle** between modes.
* **Zoom**:
    * **Smooth or stepped zoom** reveals more primes.
    * Allows exploration of clustering behavior.
* **Prime Display Settings**:
    * **Toggle** how many primes are displayed.
    * Lightweight range supports up to 1,000 primes for basic hardware.
    * **Custom input option** to enter a specific number of primes to visualize.

---

## Minimal Feature Scope (for trial app)

* Efficient rendering of prime-only vertical bands.
* Responsive horizontal scaling with zoom.
* Color toggle between neutral and gradient.
* Toggle or input how many primes to display.
* Designed for low-resource environments (32GB RAM, modest GPU).
* Built to be extensible later, but focused now on lightweight core visualization.

---

## License

This project is licensed under the [BSD 3-Clause](https://github.com/TechRancher/Octave-Coordinate-Prime-Visualizer/blob/main/LICENSE) - see the [LICENSE](https://github.com/TechRancher/Octave-Coordinate-Prime-Visualizer/blob/main/LICENSE) file for details.

---

## Created By

**Concept and Original Visual Sketch:** Tylor Smith (posted on Math Forums)
