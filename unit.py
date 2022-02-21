# A Unit is a piece of behaviour provided to an Entity.
# A Unit is used to provide Entities with functionality.
# Exemples: Units can provide appearance (MeshRenderer), physics (TrackBody), rendering (Camera).

from abc import ABC, abstractmethod


class Unit:
    pass


class UpdatableUnit(Unit):
    @abstractmethod
    def update(self):
        pass


UpdatableUnits = []
