# Infrared remote reference

The following NEC-style values were recovered from a local reference table. They are historical button assignments, not a complete controller implementation. The decimal values are the raw values listed in the source notes; byte order and repeat-code handling must be checked with the actual IR library and receiver.

## White remote

| Intended function | Decimal value | Hex value | Button marking |
| --- | ---: | --- | --- |
| Repeat frame | 4294967295 | FFFFFFFF | Repeat |
| Power on | 16753245 | FFA25D | Red power button |
| Power off | 16769565 | FFE21D | MENU |
| Forward | 16712445 | FF02FD | + |
| Reverse | 16750695 | FF9867 | - |
| Turn left | 16769055 | FFE01F | Previous |
| Turn right | 16748655 | FF906F | Next |
| Forward left | 16720605 | FF22DD | TEST |
| Reverse left | 16738455 | FF6897 | 0 |
| Forward right | 16761405 | FFC23D | Play/pause |
| Reverse right | 16756815 | FFB04F | C |
| Gimbal up | 16718055 | FF18E7 | 2 |
| Gimbal down | 16730805 | FF4AB5 | 8 |
| Gimbal left | 16716015 | FF10EF | 4 |
| Gimbal right | 16734885 | FF5AA5 | 6 |
| Upper left | 16724175 | FF30CF | 1 |
| Lower left | 16728765 | FF42BD | 7 |
| Upper right | 16743045 | FF7A85 | 3 |
| Lower right | 16732845 | FF52AD | 9 |
| Water pump | 16754775 | FFA857 | Play |
| Lights | 16726215 | FF38C7 | 5 |

## Black remote with red and green buttons

| Button | Decimal value | Hex value |
| --- | ---: | --- |
| CH- | 16753245 | FFA25D |
| CH | 16736925 | FF629D |
| CH+ | 16769565 | FFE21D |
| Previous | 16720605 | FF22DD |
| Next | 16712445 | FF02FD |
| Play/pause | 16761405 | FFC23D |
| - | 16769055 | FFE01F |
| + | 16754775 | FFA857 |
| EQ | 16748655 | FF906F |
| 0 | 16738455 | FF6897 |
| 100+ | 16750695 | FF9867 |
| 200+ | 16756815 | FFB04F |
| 1 | 16724175 | FF30CF |
| 2 | 16718055 | FF18E7 |
| 3 | 16743045 | FF7A85 |
| 4 | 16716015 | FF10EF |
| 5 | 16726215 | FF38C7 |
| 6 | 16734885 | FF5AA5 |
| 7 | 16728765 | FF42BD |
| 8 | 16730805 | FF4AB5 |
| 9 | 16732845 | FF52AD |
