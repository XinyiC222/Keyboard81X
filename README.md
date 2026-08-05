# Keyboard81X

A custom 75% PCB keyboard with a rotary encoder and 81 keys.

## Build Notes

- PCB was designed in **KiCad** using a keyswitch plugin.
  - If you are trying to find it here are the ones I used:
    - **KLE Placer**  /Organize the keys and diodes automatically based on .json file
    - **JLCPCB tools** / used for BOM and Placement for JLC pcbs (**EDIT**: New version does not use JLCPCB assembly so this tool was no longer used in the final version. But this tool really do come in handy!)
- Case was modeled in **Fusion**.
## Tools I used
- Plate was generated with: <http://builder.swillkb.com/>
- Keyboard Layout Editor: <https://www.keyboard-layout-editor.com/>
- Keycaps used in the model: <https://github.com/anhthang/dsa-keycap>
- Footprint Library I used in Kicad: <https://github.com/daprice/keyswitches.pretty>

## How To Build Your Own! <h3>PCB</h3>

1. Build your layout with the layout editor I mentioned in the tools I used.
2. Download the .json file from there.
3. In KiCad schematics choose your microcontroller or just use a chip. I used a **Raspberry Pi Pico** for the final version and placed it under the space bar. Other option: you could use a RP2040 chip and build somewhat of a dev board inside the project. That includes the Flash Memory to store the code, Crystal Oscillator (it's like the conductor), USB for power with a voltage regulator, and some capacitors.
4. Then add the current amount of MX_SW_HS you need based on the layout you made.
5. Add the same amount of diodes so each key has one that includes any rotary encoders.
6. Then after that you can add some MX_Stab for the ones you want to stabilize. Some keys like the spacebar need stabilizers, so you can change them to different footprints from the other keys. If you decided to use plate mounted stabilizers instead, you can leave this part out, otherwise if you're using pcb mounted stabilizers then you should add MX_Stab.
7. Add footprint to all your components and don't forget to **Annotate the entire Schematics**
8. Now when designing the PCB, using the .json file and the KLE Placer plugin, you can easily place them all accordingly.
9. Remember to add a border around to create the edge of the PCB in the Edge.cut layer.
10. Organize all the components to your liking and route all of them to each other.
11. **Generate the Gerber Files!**
12. Then if you were to use JLCPCB assembly, you can use the JLCPCB tools to find all the components and create the correct BOM and CPL.
13. You can then upload those files into JLCPCB and order from there!!

<h3>Case</h3>

1. Go into Fusion and create a new project.
2. Download the 3D view of your keyboard from KiCad and upload it (for reference!)
3. Then make the case around it any way you like. If you are 3D printing remember that prints can shrink so you need to **account for tolerances especially holes**
4. you can add a plate and any type of mounting you want
5. If you are adding a plate, the plate generater I included above might be helpful
6. For the plate if you are 3D printing with PLA, having it at 1.5mm thick is usually not strong enough. Set it to **3mm** but leave the area around the stabilizers to be 1.5mm. Note that **prioritizing stability would cause your switches to not clip on correctly**, but will still be tight enough to hold them.

<h3>That's pretty much a good summary of how to build your own keyboard! Thanks for reading it and I hope you learned something new. This is my first big project and definitely my first keyboard build so I don't expect everything to be correct. So if you are building this based off of mine, it's not guaranteed to work. Have fun!!</h3>

## BOM
Everything under quantity is the amount they give for the price I payed for or if I own it then its the amount I'm using. Some come with more than I needed. Check out the components I used in the BOM.csv file.

