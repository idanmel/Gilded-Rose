# -*- coding: utf-8 -*-

QUALITY_CHANGE_RATE = 1


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            update_sell_in(item)
            apply_quality_logic(item)


def enforce_minimum_quality(item):
    item.quality = max(0, item.quality)


def enforce_maximum_quality(item):
    item.quality = min(50, item.quality)


def apply_quality_logic(item):
    if is_sulfuras(item):
        item.quality = 80
        return

    if is_backstage_passes(item):
        update_backstage_passes_quality(item)
        return

    degradation_rate = get_degradation_rate(item)

    if is_aged_brie(item):
        item.quality += degradation_rate
    else:
        item.quality -= degradation_rate

    enforce_minimum_quality(item)

    enforce_maximum_quality(item)


def get_degradation_rate(item):
    degradation = QUALITY_CHANGE_RATE
    if item.sell_in <= 0:
        degradation = QUALITY_CHANGE_RATE * 2

    if is_conjured(item):
        degradation = degradation * 2

    return degradation


def update_backstage_passes_quality(item):
    if item.sell_in >= 11:
        item.quality += QUALITY_CHANGE_RATE
    elif 6 <= item.sell_in <= 10:
        item.quality += QUALITY_CHANGE_RATE * 2
    elif 0 < item.sell_in <= 5:
        item.quality += QUALITY_CHANGE_RATE * 3
    else:
        item.quality = 0


def update_sell_in(item):
    if is_sulfuras(item):
        return

    item.sell_in = item.sell_in - 1


def is_sulfuras(item):
    return item.name.startswith("Sulfuras")


def is_conjured(item):
    return item.name.startswith("Conjured")


def is_aged_brie(item):
    return item.name == "Aged Brie"


def is_backstage_passes(item):
    return item.name.startswith("Backstage passes")


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
