class DeviceControl:
    def control_device(device, state):
        # Simulation du contrôle des appareils via MQTT
        print(f"Contrôle de l'appareil {device} : {state}")
        # Exemple de contrôle (allumer ou éteindre la lumière)
        if device == "light":
            if state == "on":
                print("Lumière allumée.")
            elif state == "off":
                print("Lumière éteinte.")


def control_device(param, param1):
    return None