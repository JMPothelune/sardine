# MIDI

## Receiving MIDI

**MIDI** Input is supported through the use of a special object, the **MidiListener** object. This object will open a connexion listening to incoming MIDI messages. There are only a few types of messages you should be able to listen to:

- **MIDI** notes through the `NoteTarget` object
- **MIDI** control changes through the `ControlTarget` object

Every MidiListener is expecting a target. You must declare one and await on it using the following syntax:

```python

a = MidiListener(target=ControlTarget(20, 0))
@swim
def pluck(d=0.25):
    S('pluck', midinote=a.get()).out()
    a(pluck, d=0.25)
```

In this example, we are listening on the control change n°20 from the default port on the first channel (`0`). **Sardine** cannot assert the value of a given **MIDI** Control before it receives a first message therefore the initial value will be assumed to be `0`.

You can fine tune your listening object by tweaking the parameters:

```python

# picking a different MIDI Port
a = MidiListener('other_midi_port', target=ControlTarget(40, 4))
```

## Sending MIDI

By default, **Sardine** will connect to a **MIDI** port. There is no such thing as a **Sardine** instance without a link to **MIDI**. Having only one port means that you will be limited to 16 channels. While this may already be a lot for some, other users will want to do something with their collection of 123 synthesizers. You can manually open up new MIDI ports by tweaking your **Sardine** session from the **Python** side:

```python
# Add a new MidiHandler focusing on a specific port
your_midi_port: str = "exact_name_of_midi_port"
your_midi = MidiHandler(port_name=your_midi_port)

# Add the MIDI port to the session fishbowl
bowl.add_handler(your_midi)
```

Done! You now have a new MIDI port. The tricky part is now to add new objects to play with! Here is how to do so:
```python
# If Ziffers is imported, grab a reference to its parser!

if ziffers_imported:
    midi._ziffers_parser = z2

N2 = your_midi.send  # For sending MIDI Notes
PC2 = your_midi.send_program  # For MIDI Program changes
CC2 = your_midi.send_control  # For MIDI Control Change messages
SY2 = your_midi.send_sysex  # For MIDI Sysex messages

if ziffers_imported:
    ZN2 = midi.send_ziffers  # Connecting the new Ziffers parser
```
You now have access to an interface to play **notes**, **control changes**, **program changes** and **sysex** messages. If you want to use the shorthand notation, you will have to do one extra step:

```python
# Boilerplate for using the newly creating MIDI port with the shorthand
# syntax for swimming functions

def sy2(*args, **kwargs):
    return _play_factory(your_midi, your_midi.send_sysex, *args, **kwargs)

def n2(*args, **kwargs):
    return _play_factory(your_midi, your_midi.send, *args, **kwargs)

def zn2(*args, **kwargs):
    return _play_factory(your_midi, your_midi.send_ziffers, *args, **kwargs)

def cc2(*args, **kwargs):
    return _play_factory(your_midi, your_midi.send_control, *args, **kwargs)

def pc2(*args, **kwargs):
    return _play_factory(your_midi, your_midi.send_program, *args, **kwargs)
```

The `_play_factory()` method is not a function you are supposed to use directly. This function is mapping a **sender** (`d()`, `n()`) to a function that can be understood by a **player** (`Pa`, `Pb`).

This is everything you need to open new **MIDI** ports and replicate the normal behavior of the **Sardine** **MIDI** port. If you want to go even further, feel free to deep dive into the `midi` object itself. It might contain some sweet methods that you want to use!



