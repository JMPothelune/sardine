# Preliminary words

**Before installing, there are some guidelines you must know:**

- Being aware of your installed **Python** versions is of tremendous importance! 
  - You can have multiple versions of **Python** running on the same system.
  - **Always** prefer a version of Python that you installed yourself (*e.g.* [Pyenv](https://github.com/pyenv/pyenv)).
  - **Be careful** with aliases. On Windows, people often have **python** and **py** living side by side. **They are not the same installation of Python**.
- Find the command that will summon your **Python 3.10** or **Python 3.11** installation 
  (can be `python`, `python3`, `python3.10`, `python3.11` or `py` depending on the system you are currently using). 
  Now, stick to it! You don't want to scatter files everywhere on your computer or to do a multi-version install.
- Don't let any error happen un-noticed! If you see an error, then there must be an error! Consider it seriously! Most people assume that seing errors is normal as long as nothing crashes. It may not be that bad but a missing package means a broken **Sardine**!
- As funny as it may sound, I am not the owner of the `sardine` package on Pypi. **Sardine** is named `sardine-system`. Some people sometimes end up installing a totally unrelated tool!

**Concerning Sardine versions:**

- Sardine is experimental software. Always install from GitHub if possible!
- The Pipy version is alwas lagging behind. We update with every major version.