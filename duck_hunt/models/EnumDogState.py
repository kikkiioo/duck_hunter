import dataclasses
import enum


@enum
class EnumDogState:
    Nothing = 'None'
    Sniff = 'Sniff'
    Jump = 'Jump'
    Catch = 'Catch'
    Giggle = 'Giggle'
    Bark = 'Bark'
