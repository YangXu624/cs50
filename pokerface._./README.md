PROJECT TITLE: POKERFACE._.

Video Demo:  <https://youtu.be/H-Y5S3iuac8>

Description:
This Python-based poker game allows players to experience a classic Texas Hold'em environment, complete with both human and bot-controlled opponents. The game is designed to be easy to set up and play, making it accessible for players of all skill levels. It follows the standard Texas Hold'em rules, where each player is dealt two hole cards and shares five community cards, aiming to create the best possible five-card hand.

The game structure includes multiple betting rounds, where players can choose to check, call, raise, or fold. As the rounds progress, community cards are revealed, adding to the complexity and strategy required to win. After all rounds are completed, the players' hands are evaluated to determine the strongest combination. The game automatically handles the evaluation and comparison of hands, declaring a winner or splitting the pot in case of ties.

Key components of the game include the "Player" and "Bot" classes, which represent human and bot participants respectively. This helps us to keep track of various attributes of the participants, such as their names, balance, hands, and whether they have folded. For simplicity, our bot operates primarily on randomness (but beating it in a game is still as difficult nevertheless!). We have also introduced another class, "Cards", to seamlessly deal out and evaluate the cards.

The game also features functions that manage the deck, deal cards, and process player actions during betting rounds. At the core of the hand evaluation, the game includes functions to identify poker hand rankings such as pairs, straights, flushes, and full houses. The winning hand is determined by comparing the strength of the players' hands, ensuring that the game is fair and follows the traditional rules of poker.

To play, simply run the script and follow the on-screen prompts to set up your game, including the number of players and bots. The game is designed to be run in a Python 3.x environment and is straightforward to execute with minimal setup.

Future plans for this project include enhancing the bot's betting strategy (possibly using AI or ML), adding a graphical user interface (GUI) for a more interactive experience, and potentially introducing network multiplayer support for remote gameplay.
