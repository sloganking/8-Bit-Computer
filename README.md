# 8-Bit CPU Documentation

This project aims to document how my 8-bit CPU works, to provide example programs that is can run, and to provide visual examples of those programs running.

## Inspiration
The design of this CPU was heavily inspired by ideas from both Ben Eater's ["Building an 8-bit breadboard computer!" Youtube series](https://www.youtube.com/watch?v=HyznrdDSSGM&list=PLowKtXNTBypGqImE405J2565dvjafglHU) and Marco Schweighauser's [Online Assembler-Simulator](https://schweigi.github.io/assembler-simulator/index.html)

## Block Diagram
![Diagram](https://i.imgur.com/lU1ykk9.png)

### Colors
```
Blue:     component
Red:      register controlled by micro code which saves data from bus, and constantly outputs it into the component to it's right
Green:    input label
Purple:   resticts or allows data to flow from a component, to the central bus
Yellow:   8-Bit data bus
```
