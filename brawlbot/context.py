from dataclasses import dataclass
from typing import List, Dict


@dataclass
class BrawlBotContext:
    searchChannels: List[str]
    miscChannels: List[str]
    modChannels: List[str]
    matchChannels: List[str]
    matchChannel: str

    brawlChara: Dict[str, str]
    characterlist: List[str]

    completestagelist: List[str]
    stageTNs: Dict[str, str]
    emotes2stage: Dict[str, str]
    stage2emotes: Dict[str, str]
    stages: List[str]
    starters: List[str]
    counterpicks: List[str]


def create_context_from_config(config):
    searchChannels = config['channels']['search']
    miscChannels = config['channels']['misc']
    modChannels = config['channels']['mod']
    matchChannels = config['channels']['match']

    brawlChara = {}
    characterlist = []

    completestagelist = []
    stageTNs = {}
    emotes2stage = {}
    stage2emotes = {}

    stages = []
    starters = []
    counterpicks = []

    for entry in config['characters']:
        for s in entry['strings']:
            brawlChara[s] = entry['emote']
        characterlist.append(entry['emote'])

    stages_data = config['stages']
    for value in stages_data:
        completestagelist.append(value['emote'])
        stageTNs[value['emote']] = value['thumbnail']
        emotes2stage[value['emote']] = value['name']
        stage2emotes[value['emote']] = value['emote']
        if value['is_starter']:
            stages.append(value['emote'])
            starters.append(value['emote'])
        else:
            counterpicks.append(value['emote'])

    return BrawlBotContext(
        searchChannels=searchChannels,
        miscChannels=miscChannels,
        modChannels=modChannels,
        matchChannels=matchChannels,
        matchChannel=matchChannels[0],

        brawlChara=brawlChara,
        characterlist=characterlist,

        completestagelist=completestagelist,
        stageTNs=stageTNs,
        emotes2stage=emotes2stage,
        stage2emotes=stage2emotes,
        stages=stages,
        starters=starters,
        counterpicks=counterpicks,
    )
