> [!NOTE]
> This repo was created for for teaching purposes only.

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

## Sharing Your Game
Once your game is working, share the link with friends! They can play directly in their browser without installing Python.

## Limitations

- Your game must be contained in a single `game.py` file.
- No external Python libraries are allowed, only those supported by Pyodide [^1].
- Because standard Python `input` is not fully supported in Pyodide [^2], the built-in `input` function is replaced with an asynchronous version [^3]. All code is preprocessed so that calls to `input` become `await input`, all functions are defined with `async def`, and all function calls are prefixed with `await` [^4].
- This approach is **very** error-prone and will break if you use lambdas, define functions inside other functions, or reassign functions to new variable names (such as when using callbacks).

[^1]: https://pyodide.org/en/stable/usage/wasm-constraints.html
[^2]: https://www.youtube.com/watch?v=-SggWFS15Do
[^3]: https://github.com/x/text-adventure-game/blob/43945a822d7c4c9231a854d490a4f287ead5cb21/index.html#L76-L107
[^4]: https://github.com/x/text-adventure-game/blob/43945a822d7c4c9231a854d490a4f287ead5cb21/index.html#L212-L253

## Troubleshooting
- If your game doesn't load, check for Python syntax errors
- Make sure your `game.py` file is in the root of your repository
- Allow a few minutes for GitHub Pages to update after making changes
- Check the browser console [^1] for the preprocessed code

[^1]: https://developer.chrome.com/docs/devtools/open
