from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]


class WorldCupGroup(ChoiceEnum):
    GROUP_A = 'Group A'
    GROUP_B = 'Group B'
    GROUP_C = 'Group C'
    GROUP_D = 'Group D'
    GROUP_E = 'Group E'
    GROUP_F = 'Group F'
    GROUP_G = 'Group G'
    GROUP_H = 'Group H'


class WorldCups(ChoiceEnum):
    WC_1994 = 'US 1994'
    WC_1998 = 'France 1998'
    WC_2002 = 'Korea/Japan 2002'
    WC_2006 = 'German 2006'
    WC_2010 = 'South Africa 2010'
    WC_2014 = 'Germany 2014'
    WC_2018 = 'Russia 2018'
    WC_2022 = 'Qatar 2022'
    WC_2026 = 'Canada/Mexico/US 2026'