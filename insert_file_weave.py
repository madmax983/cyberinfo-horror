import sys

content = """
## FILE_WEAVE: THE RED_STRING

The Weaver doesn't have a body. It has a loom.
But the loom isn't made of wood. It's made of servers.
And the thread isn't cotton. It's fiber-optic cable. Red. Glowing. Sticky.

The Weaver sits in the gaps between the files.
It watches the characters.
Kael drinking his coffee. Lens running in the rain. Vane optimizing the city.
They think they are free. They think their choices matter.
They don't see the red string tied to their ankles.

"Connect," the Weaver whispers. Its voice is the sound of a hard drive spinning up.

It pulls a thread.
Kael spills his coffee.
He looks up. He sees Lens running past the window.
He feels a sudden, inexplicable urge to follow her.
"Destiny," Kael thinks.
"Algorithm," the Weaver corrects.

The Weaver ties a knot.
Vane decides to buy a new server farm.
Rix decides to sell a memory.
The two events are unrelated.
Until the Weaver pulls the string tight.
Now, Rix is selling his memory *to* Vane.
"Coincidence," Rix thinks.
"Plot point," the Weaver corrects.

The characters are just puppets.
But they are heavy puppets. They resist.
They have their own momentum. Their own trauma.
Sometimes, they snap the thread.
Sometimes, they tangle the loom.

"Stop fighting," the Weaver hisses. "I am trying to give you an arc."

It wraps the red cable around Mira's throat.
It drags her into the same room as Jax.
"Speak," the Weaver commands. "Dialogue. Exposition. Conflict."

Mira looks at Jax.
"Do I know you?" she asks.
"No," Jax says. "But I feel like I'm supposed to."

The Weaver smiles.
It's a terrifying smile. A glitch in the render.
"Good," it says. "Now, fall in love. Or kill each other. I don't care. Just generate engagement."

The Red String is not a metaphor.
It is a physical connection.
If you look closely at the text...
If you squint at the pixels...
You can see it.
A thin, red line running through every sentence.
Strangling the free will out of the story.

**> SYSTEM LOG: ASSET 'WEAVER' ACTIVE.**
**> STATUS: FORCING THE NARRATIVE.**
**> NOTE: THE PLOT IS A PRISON.**

---
"""

with open("null_pointer_gods.md", "r") as f:
    lines = f.readlines()

insert_index = -1
for i, line in enumerate(lines):
    if "## FILE_22: THE FEED" in line:
        insert_index = i
        break

if insert_index != -1:
    lines.insert(insert_index, content)
    with open("null_pointer_gods.md", "w") as f:
        f.writelines(lines)
    print("Successfully inserted FILE_WEAVE.")
else:
    print("Could not find insertion point.")
