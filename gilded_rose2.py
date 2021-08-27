# -*- coding: utf-8 -*-

QUALITY_CHANGE_RATE = 1


def keep_quality_between_limits(quality, minimum=0, maximum=50):
    if quality > maximum:
        result = maximum
    elif quality < minimum:
        result = minimum
    else:
        result = quality

    return result


def get_quality_change_normal(item):
    result = QUALITY_CHANGE_RATE
    if item.sell_in < 0:
        result = QUALITY_CHANGE_RATE * 2

    return result


def get_quality_change_backstage_passes(item):
    if item.sell_in < 0:
        return -1 * item.quality

    if 11 <= item.sell_in:
        result = QUALITY_CHANGE_RATE
    elif 6 <= item.sell_in <= 10:
        result = QUALITY_CHANGE_RATE * 2
    else:
        result = QUALITY_CHANGE_RATE * 3

    return result


def is_sulfuras(item):
    return item.name.startswith("Sulfuras")


def is_conjured(item):
    return item.name.startswith("Conjured")


def is_aged_brie(item):
    return item.name == "Aged Brie"


def is_backstage_passes(item):
    return item.name.startswith("Backstage passes")


def do_update_quality(item):
    item.sell_in = item.sell_in - 1
    if is_sulfuras(item):
        item.quality = 80
        item.sell_in = item.sell_in + 1
    elif is_aged_brie(item):
        item.quality += get_quality_change_normal(item)
    elif is_backstage_passes(item):
        item.quality += get_quality_change_backstage_passes(item)
    elif is_conjured(item):
        item.quality -= get_quality_change_normal(item) * 2
    else:
        item.quality -= get_quality_change_normal(item)

    if not is_sulfuras(item):
        item.quality = keep_quality_between_limits(item.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        [do_update_quality(item) for item in self.items]


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


