# -*- coding: utf-8 -*-
import unittest

from python.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_regular_item_quality_and_sell_in_should_decrease_by_one(self):
        items = [Item(name="foo", sell_in=1, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_regular_item_quality_degrades_twice_as_fast_after_sell_in_passed(self):
        items = [Item(name="foo", sell_in=-2, quality=4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item(name="foo", sell_in=-2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_in_quality(self):
        items = [Item(name="Aged Brie", sell_in=4, quality=5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_quality_is_never_above_50(self):
        items = [Item(name="Aged Brie", sell_in=4, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_sell_in_and_quality_stays_the_same(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_increases_in_value(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=20, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_increases_in_value_by_2_with_10_days_or_less(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_increases_in_value_by_3_with_5_days_or_less(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_quality_drops_to_0_after_concert(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_items_degrade_in_quality_twice_as_fast(self):
        items = [Item(name="Conjured Mana Cake", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_conjured_items_degrade_in_quality_twice_as_fast_when_expired(self):
        items = [Item(name="Conjured Mana Cake", sell_in=-2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(6, items[0].quality)


if __name__ == '__main__':
    unittest.main()
