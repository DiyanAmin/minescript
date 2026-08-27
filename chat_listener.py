import m

with m.EventQueue() as event_queue:
    event_queue.register_chat_listener()
    while True:
        event = event_queue.get()
        
        if event.type == m.EventType.CHAT:
            if not event.message.startswith('> '):
                m.echo(f'Got chat message: {event.message}')