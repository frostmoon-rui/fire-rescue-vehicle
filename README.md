# Fire Rescue Vehicle

Recovered camera subsystem, infrared remote reference and CAD drawings from a fire-rescue vehicle project. The available firmware targets an AI Thinker ESP32-CAM and records camera frames to a microSD card.

This is a source archive of the recovered components, **not a verified complete autonomous-driving or automatic fire-extinguishing implementation**. No STM32 chassis controller, obstacle-avoidance controller, navigation stack or pump-control firmware was found in the supplied project directory. Hardware integration remains to be verified.

## Repository layout

```text
firmware/camera_recorder/    Arduino sketch, camera HTTP server and camera pin definitions
hardware/cad/               Recovered DXF drawings with neutralized author metadata
docs/infrared-remote.md      Historical remote-control codes and intended functions
docs/recovery-notes.md       Scope, limitations and excluded materials
tests/test_archive.py        Offline archive, configuration and source checks
```

## Camera setup

1. Install Arduino IDE and a compatible ESP32 Arduino board package from its official distribution.
2. Open `firmware/camera_recorder/camera_recorder.ino`. Keep its companion `.h` and `.cpp` files in the same sketch directory.
3. Copy `network_config.example.h` to `network_config.h` and configure your own local Wi-Fi network. Never commit that file.
4. Select the matching AI Thinker ESP32-CAM board, enable its PSRAM configuration, and verify the pin map against your actual module and microSD wiring.
5. Compile and test with the camera and microSD card before connecting the subsystem to a vehicle. Serial output uses 115200 baud.

The source uses legacy ESP32 camera and face-detection headers, including `fd_forward.h` and `fr_forward.h`. It is **not confirmed to compile against current ESP32 Arduino releases**; upgrading the board package may require a port. No dependency version is claimed as tested, and no firmware or vehicle hardware has been executed during repository preparation.

The recovered defaults request VGA capture, a 100 ms capture interval and 18,000 frames per recording. These are configuration targets, not measured performance guarantees.

## Important operational limits

- The current `setup()` initializes recording tasks inside the successful Wi-Fi connection branch. An old note claimed offline recording, but that claim does not match this recovered implementation. Do not rely on recording without a network connection until this is corrected and tested.
- Camera HTTP endpoints are inherited from the original example and are not a hardened authenticated service. Use a trusted local network only; do not expose the camera directly to the public internet.
- Verify power supply, motor isolation and emergency-stop behavior independently. This archive is not safety-certified equipment and must not be relied on for emergency response.
- The infrared table documents intended button assignments only. It does not prove that a chassis, gimbal or pump controller implements them.

## Offline checks

```sh
python -m unittest discover -s tests -q
```

These checks validate repository contents, embedded web-page compression, configuration placeholders and CAD text structure. They do not replace an Arduino compile or a hardware test.

## Attribution

The camera HTTP server retains its Espressif copyright and Apache-2.0 notices. The AVI recording source retains the original version and author identifiers present in the recovered code. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [LICENSE](LICENSE). Repository cleanup does not imply authorship of upstream components.
