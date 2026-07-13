# KeyboardX81

A custom 75% PCB keyboard with a rotary encoder and 81 keys.

## Build Notes

- PCB was designed in **KiCad** using a keyswitch plugin.
  - If you are trying to find it here are the ones I used:
    - **KLE Placer**  /Organize the keys and diodes automatically based on .json file
    - **JLCPCB tools** / used for BOM and Placement for JLC pcbs
- Case was modeled in **Fusion**.
## Tools I used
- Plate was generated with: <http://builder.swillkb.com/>
- Keyboard Layout Editor: <https://www.keyboard-layout-editor.com/>
- Keycaps used in the model: <https://github.com/anhthang/dsa-keycap>
- Footprint Library I used in Kicad: <https://github.com/daprice/keyswitches.pretty>

#:# How To Build Your Own! <h3>PCB</h3>

1. Build your layout with the layout editor I mentioned in the tools I used.
2. Download the .json file from there.
3. In KiCad schematics choose your microcontroller or just use a chip. For mine, I used a RP2040 chip and built somewhat of a dev board inside the project. That includes the Flash Memory to store the code, Crystal Oscillator (it's like the conductor), USB for power with a voltage regulator, and some capacitors.
4. Then add the current amount of MX_SW_HS you need based on the layout you made.
5. Add the same amount of diodes so each key has one.
6. Then after that you can add some MX_Stab for the ones you want to stabilize. Some keys like the spacebar need stabilizers, so you can change them to different footprints from the other keys.
7. Add footprint to all your components and don't forget to **Annotate the entire Schematics**
8. Now when designing the PCB, using the .json file and the KLE Placer plugin, you can easily place them all accordingly.
9. Remember to add a border around to create the edge of the PCB in the Edge.cut layer.
10. Organize all the components to your liking and route all of them to each other.
11. **Generate the Gerber Files!**
12. Then if you were to use JLCPCB, you can use the JLCPCB tools to find all the components and create the correct BOM and CPL.
13. You can then upload those files into JLCPCB!!

<h3>Case</h3>

1. Go into Fusion and create a new project.
2. Download the 3D view of your keyboard from KiCad and upload it (for reference!)
3. Then make the case around it any way you like. If you are 3D printing remember that prints can shrink so you need to **account for tolerances especially holes**
4. you can add a plate and any type of mounting you want
5. For the plate if you are 3D printing with PLA, having it at 1.5mm thick is usually not strong enough. Set it to **3mm** but leave the area around the stabilizers to be 1.5mm

<h3>That's pretty much a good summary of how to build your own keyboard! Thanks for reading it and I hope you learned something new. This is my first big project and definitely my first keyboard build so I don't expect everything to be correct. So if you are building this based off of mine, it's not guaranteed to work!!</h3>

## BOM
Everything under quality is the amount they give for the price I payed for. Some come with more than I needed.

| Item | Purpose | Price | Quantity | Source |
|--------|--------|--------|--------|--------|
| Screw-in Stabilizers | stab for space bar etc | $1.78 | has 1 6.25u and two 2u | [Aliexpress](https://www.aliexpress.com/item/3256807050530252.html?spm=a2g0o.cart.0.0.662f38dalKtZIM&mp=1&pdp_npi=6%40dis%21USD%21USD%205.78%21USD%201.78%21%21USD%201.78%21%21%21%4021033b3317839178475821842e1186%2112000039909995531%21ct%21US%217294405090%21%211%210%21) |
| Tactile switch | switches | $8.56 | x100 | [Aliexpress](https://www.aliexpress.com/item/3256812192263951.html?spm=a2g0o.cart.0.0.662f38dalKtZIM&mp=1&pdp_npi=6%40dis%21USD%21USD%2017.83%21USD%208.56%21%21USD%208.56%21%21%21%4021033b3317839178475821842e1186%2112000058235272628%21ct%21US%217294405090%21%211%210%21) |
| 1N4148 SOD-123 | diodes for each switch | $1.67 | x100 | [Aliexpress](https://www.aliexpress.com/item/3256801606142520.html?spm=a2g0o.cart.0.0.662f38dalKtZIM&mp=1&pdp_npi=6%40dis%21USD%21USD%201.67%21USD%201.67%21%21USD%201.67%21%21%21%4021033b3317839178475821842e1186%2112000017590457340%21ct%21US%217294405090%21%211%210%21) |
| Hot Swap Sockets | hot swap keys | $8.29 | x110 | [Aliexpress](https://www.aliexpress.com/item/3256809001206372.html?spm=a2g0o.cart.0.0.662f38dalKtZIM&mp=1&pdp_npi=6%40dis%21USD%21USD%2017.27%21USD%208.29%21%21USD%208.29%21%21%21%4021033b3317839178475821842e1186%2112000048235529402%21ct%21US%217294405090%21%211%210%21) |
| SMD | Reset button | $1.63 | x50 | [Aliexpress](https://www.aliexpress.com/item/3256805092773328.html?spm=a2g0o.cart.0.0.662f38dalKtZIM&mp=1&pdp_npi=6%40dis%21USD%21USD%201.63%21USD%201.63%21%21USD%201.63%21%21%21%4021033b3317839178475821842e1186%2112000032466018227%21ct%21US%217294405090%21%211%210%21) |
| Type C Female | PCB for power | $2.24 | x3 | [Aliexpress](https://www.aliexpress.com/item/3256804989275660.html?spm=a2g0o.cart.0.0.662f38dalKtZIM&mp=1&pdp_npi=6%40dis%21USD%21USD%202.24%21USD%202.24%21%21USD%202.24%21%21%21%402103117b17839184094411318e10ac%2112000031972190842%21ct%21US%217294405090%21%211%210%21) |
| Keycaps | for the Keys | $4.67 | x104 | [Aliexpress](https://www.aliexpress.com/item/3256808108935624.html?spm=a2g0o.cart.0.0.662f38dalKtZIM&mp=1&pdp_npi=6%40dis%21USD%21USD%204.67%21USD%204.67%21%21USD%204.67%21%21%21%402103117b17839184094411318e10ac%2112000044523183095%21ct%21US%217294405090%21%211%210%21) |

