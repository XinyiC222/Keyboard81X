# Keyboard81X

A custom 75% PCB keyboard with a rotary encoder and 81 keys.

<img width="1052" height="583" alt="Screenshot 2026-08-02 at 5 42 08 PM" src="https://github.com/user-attachments/assets/114b21b6-b3f3-47a6-88ee-0ea8cd1a1162" />

<img width="2026" height="884" alt="image" src="https://github.com/user-attachments/assets/f838d7d8-0ae6-4f7d-bdb9-6d82a02f44a6" />

<img width="2028" height="904" alt="image" src="https://github.com/user-attachments/assets/6aa2b587-a778-4822-b1e9-55775201ddf5" />

<img width="1103" height="464" alt="image" src="https://github.com/user-attachments/assets/243d167c-e3c4-4e88-9f09-5a83e62621d8" />




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
Everything under quantity is the amount they give for the price I payed for or if I own it then its the amount I'm using. Some come with more than I needed.


| Item | Purpose | Price | Quantity | Source |
| ------------- | ------------- | ------------- | ------------- |
| Raspberry Pi Pico | Mirco-controller | $1.99 | 1 | [Aliexpress](https://www.aliexpress.com/item/3256807207612469.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&sourceType=570&pdp_npi=6%40dis%21USD%21USD%208.66%21USD%202.39%21%21USD%201.98%21%21%21%402101d3fe17861144495612456e0f9a%2112000040565295947%21ct%21US%217294405090%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D) |
| 1N5817 DO-41 | USB_C VBUS | $1.79 | x50 | [Aliexpress](https://www.aliexpress.com/item/3256809192784213.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&pdp_npi=6%40dis%21USD%21USD%203.83%21USD%201.92%21%21USD%201.92%21%21%21%402103119c17861142221435145e2191%2112000048926087942%21ct%21US%217294405090%21%211%210%21) |
| Keycaps | for the Keys | $4.73 | x126 | [Aliexpress](https://www.aliexpress.com/item/3256808108935624.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&pdp_npi=6%40dis%21USD%21USD%204.73%21USD%204.73%21%21USD%204.73%21%21%21%402103119c17861142221435145e2191%2112000044523183095%21ct%21US%217294405090%21%211%210%21) |
| Plate Mounted Stabilizers | stab for space bar etc | $2.99 | has one 6.25u and two 2u | [Aliexpress](https://www.aliexpress.com/item/3256808467378574.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&sourceType=570&pdp_npi=6%40dis%21USD%21USD%203.32%21USD%202.99%21%21USD%202.47%21%21%21%402101d3fe17861144495612456e0f9a%2112000046108045634%21ct%21US%217294405090%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D) |
| SMD turtle switches | Reset button | $2.19 | x50 | [Aliexpress](https://www.aliexpress.com/item/3256805092773328.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&sourceType=570&pdp_npi=6%40dis%21USD%21USD%202.25%21USD%202.19%21%21USD%201.81%21%21%21%402101d3fe17861144495612456e0f9a%2112000032466018228%21ct%21US%217294405090%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D) |
| Hot Swap Sockets | hot swap keys | $6.20 | x110 | [Aliexpress](https://www.aliexpress.com/item/3256809001206372.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&pdp_npi=6%40dis%21USD%21USD%2017.45%21USD%206.20%21%21USD%206.20%21%21%21%402101d3fe17861144435192279e0f9a%2112000048235529402%21ct%21US%217294405090%21%211%210%21) |
| Silent Axis switch | switches | $7.66 | x100 | [Aliexpress](https://www.aliexpress.com/item/3256812192263951.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&pdp_npi=6%40dis%21USD%21USD%2018.05%21USD%207.66%21%21USD%207.66%21%21%21%402103119c17861142221435145e2191%2112000058235272628%21ct%21US%217294405090%21%211%210%21) |
| Type C Female | PCB for power | $2.24 | x3 | [Aliexpress](https://www.aliexpress.com/item/3256804989275660.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&pdp_npi=6%40dis%21USD%21USD%202.27%21USD%202.26%21%21USD%202.26%21%21%21%402101d3fe17861144455232342e0f9a%2112000031972190842%21ct%21US%217294405090%21%211%210%21) |
| Solder | soldering | $2.14 | x1 | [Aliexpress](https://www.aliexpress.com/item/3256812349220377.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&pdp_npi=6%40dis%21USD%21USD%204.45%21USD%202.14%21%21USD%202.14%21%21%21%402103119c17861142221435145e2191%2112000058646043574%21ct%21US%217294405090%21%211%210%21) |
| 5.1k resistors | for ground near usb-c | $2.48 | x300 | [Aliexpress](https://www.aliexpress.com/item/3256811592848349.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&pdp_npi=6%40dis%21USD%21USD%203.01%21USD%202.42%21%21USD%202.42%21%21%21%402103119c17861142221435145e2191%2112000056534710480%21ct%21US%217294405090%21%211%210%21) |
| IN4148 DO-31 | matrix | $1.92 | x100 | [Aliexpress](https://www.aliexpress.com/item/3256809322506944.html?spm=a2g0o.cart.0.0.6ac438dadamcUQ&mp=1&sourceType=570&pdp_npi=6%40dis%21USD%21USD%203.81%21USD%201.79%21%21USD%201.22%21%21%21%402101d9ef17861148559937041e10b8%2112000049319061688%21ct%21US%217294405090%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22sourceType%22%3A%22570%22%2C%22cartSource%22%3A%22main%22%7D%7D) |
| Heat Inserts | To mount plate | $0.00 | 2 | Already Owned |
| M2.5 x 15mm bolts | Mount plate | $0.00 | 2 | Already Owned |
| Rotary Encoder | Volume knob | $0.00 | 1 | Already Owned |
| PCB | Connects everything | $39.36 | 5 | JLCPCB |
| 3D Prints | case for all the parts | $0.00 | | Printing Legion |
| Sub-Total+Tax |  | $37.48 | Aliexpress |
| Total |  | $76.84 | All Combined |


