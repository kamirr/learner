# learner
## about
Simple program to learn definitions / foreign vocabulary.

## usage
- `learn` – display random word and definition
- `learn 'word = meaning'` – add new definition<b>*</b>
- `learn quiz` – shows random definition and asks for word
- `learn test` – tests knowledge of all definitions (like quiz) in random order

It's recommended to save `learn.py` as `/usr/bin/learn` and add `learn` command at very and of `~/.bashrc` file. Script requires `.word-list` file to be placed under `~/` directory to work properly. If you want to keep up–to–date with words from repo you can create symlink `ln -s /path/to/repo/.word-list .word-list`.<br/>
<b>*`'word = meaning'` format (including spaces) is required to get `quiz` and `test` working</b>
