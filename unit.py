from abc import ABC, abstractmethod


class Unit:
    pass


class UpdatableUnit(Unit):
    @abstractmethod
    def update(self):
        pass


UpdatableUnits = []
