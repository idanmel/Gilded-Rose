# Gilded Rose Kata
Taken from [Emily Bache](https://github.com/emilybache/GildedRose-Refactoring-Kata).

## Retrospective

### Thoughts effected me while doing the kata
1. I'm not smart enough for this.
2. It takes me too much time.
3. I'm such a good developer, look at my unit tests.


### Adding Conjured items
Because I had these negative thoughts, I added the functionality for the Conjured items
the moment I saw how to.
This was not optimal, because although the change was easy, it was not simple,
as I had to make the change in two places.

On the other hand, that might be the "correct" way of doing it...
I wrote the test, found an easy way to make it pass, then refactored.

### Most used refactoring techniques:
1. Extract method
2. Move up
3. Rename

Several times while manually refactoring, I had the feeling that there should have been
a way to automatically do it.
I can't remember when I had these feelings, so I'll pay closer attention next time.

### What I like about my solution 
I think the refactoring I came up with is pretty good.
1. No duplication
2. No nesting
3. Clear
4. If I had another item type to add, there would probably be one place to change

### What I don't like about my solution
I feel uneasy about all the mutating state.
Half the functions I wrote return None, which smells weird.
Not sure how to refactor the data to be immutable.

I also think I could have used some class system, where each item type
has it's own function to calculate quality. 
I didn't see a way to do it without breaking the Item class, which was not allowed to change.

### A question for the reader:
What's more readable to you?
```python
item.quality = max(0, item.quality)
```
Or
```python
if item.quality < 0:
    item.quality = 0
```

