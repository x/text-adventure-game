# Text Adventure Game Bootstrap

[Demo](https://x.github.io/text-adventure-game/)

## How to Use This Repo
This repo is set up to bootstrap your basic Python text adventure game to function as a web page that's shareable with friends.

## Getting Started

### 0. Create a Github Account
1. If you don't have one already, [create your own github account](https://github.com/signup).

### 1. Fork This Repository
1. Click the "Fork" button at the top right of this page
2. This creates your own copy of the repository under your GitHub account

### 2. Enable GitHub Pages
1. Go to your forked repository
2. Click on "Settings" (in the repository navigation)
3. Scroll down to the "Pages" section in the left sidebar
4. Under "Source", select "Deploy from a branch"
5. Under "Branch", select "main" and "/ (root)"
6. Click "Save"
7. Wait a few minutes for GitHub to build your site
8. Your game will be available at: `https://[your-username].github.io/text-adventure-game/`

### 3. Create Your Own Game
1. Click on `game.py` in your repository
2. Click the pencil icon to edit the file
3. Replace the sample game with your own Python code
4. Commit your changes (scroll down, add a commit message, and click "Commit Changes")

## Writing Your Game
Your game should be written in standard Python. The web terminal supports:
- `print()` statements for output
- `input()` for getting player input
- Functions (`def`) and variables
- Conditional statements (`if`/`elif`/`else`)
- Loops (`while`/`for`/`break`)

## Limitations
- Your game must be in a single `game.py` file
- No external Python libraries (only Python built-ins)
- The game runs entirely in the browser using Pyodide

## Sharing Your Game
Once your game is working, share the link with friends! They can play directly in their browser without installing Python.

## Troubleshooting
- If your game doesn't load, check for Python syntax errors
- Make sure your `game.py` file is in the root of your repository
- Allow a few minutes for GitHub Pages to update after making changes
- Check the browser console (F12) for error messages

## Credits
This project uses:
- [Pyodide](https://pyodide.org/) - Python running in the browser
- [xterm.js](https://xtermjs.org/) - Terminal emulator for the web
