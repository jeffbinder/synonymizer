# The Synonymizer

This is the code for my [2015 entry](https://github.com/dariusk/NaNoGenMo-2015/issues/175) for [National Novel Generating Month](https://github.com/dariusk/NaNoGenMo-2015).

The idea is to take a novel by a writer known for having a masterful command of vocabulary - specifically, Henry James's _Portrait of a Lady_ - and replace every word with a synonym.

    His gait had a shambling, wandering quality; he was not very firm on
    his legs. As I have said, whenever he passed the old man in the chair he
    rested his eyes upon him; and at this moment, with their faces brought
    into relation, you would easily have seen they were father and son.
    The father caught his son's eye at last and gave him a mild, responsive
    smile.

    "I'm getting on very well," he said.

Turns into this:

    His pace had a scuffling, wandering lineament; he was not very business firm on
    his legs. As I have enunciated, whenever he passed the old man in the chair he
    rested his middles upon him; and at this consequence, with their sides fetched
    into relation, you would easily have realise they were church father and son.
    The father caught his son's eye at last and gave him a mild, reactive
    smile.

    "I'm having on very advantageously," he enjoined.

The script uses [NLTK](http://www.nltk.org) and the Natural-Language Processing module from [NodeBox](https://www.nodebox.net).  You will need to install NLTK and put the "en" directory from NodeBox into the same directory as the script to get it to run.

The text is from [Project Gutenberg](http://www.gutenberg.org/ebooks/2833).
