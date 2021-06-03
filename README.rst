====================
 Dungeon Encounters
====================

A tool to give D&D 5e players and DMs better insight into the difficulty
and deadliness of encounters, beyond just challenge rating.

Beliefs
=======

* DMs have enough to worry about beyond building encounters. They should
  concentrate on building an exciting story rather than on whether this fight
  will accidentally destroy their campaign or bore their players to tears.

* DMs are too often in the dark when it comes to the real challenge of their encounters.

* People are genuinely curious about the real deadliness of their encounters

Philosophies
============

- Aim to be detailed and specific:

  - More than just challenge rating but the actual creatures

  - More than just character levels but the actual characters.

  - Not just random but clever. Not just for the battle, but the war

- The challenge rating system is good for getting a ballpark view into a
  fight but DMs often want to know more:

  - Will this fight reasonably challenge my players?

  - Will this fight be too hard for my players?

  - What are the odds the players will win? What are the odds that someone
    goes down or dies?

  - How can I make this fight better?

- We shouldn't be afraid to dive deep. We should aim to support even difficult things like:

  - Location on a grid

  - More left-field capabilities (eventually) like Lair Actions, Opportunity Attacks, Non-attack actions

  - Side-effects of actions (e.g. Thunderwave)

  - Monsters and players should not simply always take a greedy approach.

  - AI techniques and algorithms (Minimax, statefulness, etc.)

- It should be possible to incorporate this code in many other places and applications

  - Other projects

  - Web Applications

Current Tack
============

* Start with a subset of abilities:

  * Simple Attack actions then Multi-attack actions

  * Simple Spell actions

* A structure should be built that allows entities to:

  * Know their available actions

  * Know the state of the encounter

* Entities can then:

  * Choose an available action or series of available actions

  * Impart those actions into the encounter

* Support:

  * Different algorithms (monsters aim to gang up on the weakest player a-la-Fire Emblem)

  * Locations

  * Bonus Actions, Lair Actions, Legendary Actions

Open Questions
==============

* How to best leverage existing works in dungeon-sheets?

  * Seems to be the best way to get Characters into an encounter

  * Need a clever structure to support monsters who may have complex
    actions and abilities:

    1. Could extend dungeon-sheets `Monster` or `Entity` class to support these
       more complex actions (Bonus Actions, Lair Actions)

    2. Could write an `Actor` for Monsters that combines with the existing `Monster` class
       as a mixin or extends the `Monster` class with a list of actions that really work for dungeon-encounters.


Documentation
=============

TODO: Put this on RTD

Installation
============

TODO: Get this stable then put it on PyPI

.. code:: bash

    $ pip install dungeonencounters

Usage
=====

TODO: Write me
