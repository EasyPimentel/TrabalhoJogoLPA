import keyboard

while True:
    try:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(f'Tecla pressionada: {event.name}')
        elif event.event_type == keyboard.KEY_UP:
            print(f'Tecla liberada: {event.name}')
    except KeyboardInterrupt:
        break