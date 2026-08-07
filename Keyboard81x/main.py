import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.mouse_keys import MouseKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MouseKeys())


keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15
)

keyboard.row_pins = (
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP18,
    board.GP17,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

media_keys = MediaKeys()
ecoder_handler = EncoderHandler()

keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(MouseKeys())

encoder_handler.pins = (
    (board.GP27, board.GP26, None, False), #ENCA ENCB SW is_inverted
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
]

Base = 0
FN = 1

_ = KC.TRNS

# ┌───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┐
# │Esc│ │Bri│Bru│ F3│Fnd│ │Wak│Slp│Prv│Ply│ │Nxt│Mut│Vol│Vol│ │ROT│
# └───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┘
# ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┬───┐
# │ ~ │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │ - │ = │Backsp │Fnd│
# ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┼───┤
# │ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │ [ │ ] │  \  │Und│
# ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┼───┤
# │ Caps │ A │ S │ D │ F │ G │ H │ J │ K │ L │ ; │ ' │ Enter  │Pst│
# ├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────┬───┼───┤
# │ Shift  │ Z │ X │ C │ V │ B │ N │ M │ , │ . │ / │Shift │ ↑ │Cpy│
# ├────┬───┴┬──┴─┬─┴───┴───┴───┴───┴───┴──┬┴───┴┬──┴──┬───┼───┼───┤
# │Ctrl│Alt │Cmd │         Space          │RGu  │Alt  │ ← │ ↓ │ → │
# └────┴────┴────┴────────────────────────┴─────┴─────┴───┴───┴───┘

keyboard.keymap = [
    [
    #row 0
    KC.ESC, KC.BRID, KC.BRIU, KC.F3, KC.FIND,
    KC.WAKE, KC.SLEP, KC.MPRV, KC.MPLY, KC.MNXT,
    KC.MUTE, KC.VOLD, KC.VOLU,

    #row 1
    KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4,
    KC.N5, KC.N6, KC.N7, KC.N8, KC.N9,
    KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.DEL,

    #row 2
    KC.TAB, KC.Q, KC.W, KC.E, KC.R,
    KC.T, KC.Y, KC.U, KC.I, KC.O,
    KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.MS_WH_UP,

    #row 3
    KC.CAPS, KC.A, KC.S, KC.D, KC.F,
    KC.G, KC.H, KC.J, KC.K, KC.L,
    KC.SCLN, KC.QUOT, KC.ENT, KC.MS_WH_DOWN,

    #row 4
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V,
    KC.B, KC.N, KC.M, KC.COMM, KC.DOT,
    KC.SLSH, KC.RSFT, KC.UP, KC.END,

    #row
    KC.LCTL, KC.LALT, KC.LGUI, KC.SPC, KC.RGUI, KC.RALT, KC.LEFT, KC.DOWN, KC.RGHT,

    ],
]

if __name__ == '__main__':
    keyboard.go()
