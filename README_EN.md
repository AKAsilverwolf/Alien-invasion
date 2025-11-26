# Alien Invasion Game

A complete alien invasion shooting game developed with Python and Pygame.

## 🎮 Game Features

- 🚀 **Smooth Ship Control System** - Four-directional movement with precise controls
- 👾 **Alien Formation AI** - Intelligent formation movement with automatic shooting
- 💥 **Complete Sound System** - Shooting, explosion sound effects for immersive experience
- 🌌 **Beautiful Starfield Background** - Procedurally generated with stunning visual effects
- 💯 **Complete Scoring System** - Real-time score display with level progression
- 🏆 **Leaderboard Function** - Local storage of top 10 players with Chinese input support
- ❤️ **Life System** - Multiple lives for added challenge
- 📈 **Progressive Difficulty System** - Increasing challenge with level progression
- 🎯 **Chinese Font Support** - Perfect Chinese display for localized experience

## 🎮 Game Features

- 🚀 Smooth ship control system
- 👾 Alien formation AI
- 💥 Complete sound system (shooting, explosion, game over)
- 🌌 Beautiful starfield background
- 💯 Complete scoring system
- 🏆 Leaderboard function (local storage of top 10)
- ❤️ Life system
- 📈 Progressive difficulty system
- 🎯 Chinese font support

## 🕹️ Game Controls

| Control | Function |
|---------|---------|
| **Arrow Keys (↑↓←→)** | Control four-directional ship movement |
| **Spacebar** | Fire bullets |
| **L Key** | View leaderboard (available anytime during game) |
| **ESC Key** | Close leaderboard/exit input screen |
| **Q Key** | Quick exit game |
| **Mouse Click** | Click button operations |

## 🚀 Quick Start

### Code Entry
Main program entry file: `alien_invasion.py`

### System Requirements
- **Python Version**: 3.6+ (recommended 3.8+)
- **Operating System**: Windows / macOS / Linux
- **Hardware**: Audio output device support

### Installation and Running

#### 1. Install Dependencies
```bash
# Install using pip
pip install -r requirements.txt

# Or manually install core dependencies
pip install pygame numpy
```

#### 2. Run Game
```bash
# Enter game directory
cd Alien-invasion

# Start game
python alien_invasion.py
```

#### 3. First Run
- Automatically generates game image files
- Creates leaderboard data file
- Detects and loads system fonts

#### 4. Verify Installation
After game launch, you should see:
- Alien Invasion title
- Start Game button
- Sound loading success message

## 🎯 Gameplay

### Basic Rules
1. **Destroy Aliens** - Control the spaceship to shoot all aliens on screen
2. **Progressive Difficulty** - Game speed and difficulty increase with each wave cleared
3. **Life System** - Losing life when aliens reach screen bottom or hit the ship
4. **Game Over** - Game ends when all lives are lost

### Scoring System
- **Base Score**: Base points for each alien destroyed
- **Level Bonus**: Higher levels give more score rewards
- **Combo Kills**: Additional rewards for quick consecutive kills

### Leaderboard System
- **Auto Record**: Automatically records high scores at game end
- **Name Input**: Shows name input interface when achieving high score standards
- **View Anytime**: Press L key anytime during game to view leaderboard
- **Persistent Storage**: Leaderboard data saved locally, preserved after restart

### Game Tips
- 🎯 **Precise Shooting** - Save bullets, improve efficiency
- 🚀 **Flexible Movement** - Use four-directional movement to dodge aliens
- 🏆 **Aim High Score** - Get more points with consecutive kills
- 📈 **Challenge Levels** - Try to reach higher difficulty levels

## 🏆 Leaderboard System

### Features
- **Auto Save**: Automatically saves top 10 high scores at game end
- **Complete Info**: Records player name, score, level, and game time
- **Chinese Support**: Perfect support for Chinese name input and display
- **Local Storage**: Data persistence saved locally, preserved after game restart

### Leaderboard Format
| Rank | Player | Score | Level | Time |
|-------|--------|-------|-------|------|
| 1 | Alice | 2,500 | 3 | 2024-01-01 13:00 |
| 2 | Bob | 1,800 | 2 | 2024-01-01 14:00 |
| 3 | Player | 1,000 | 1 | 2024-01-01 12:00 |

### Data Files
- **File Location**: `leaderboard.json`
- **Data Format**: UTF-8 encoded JSON format
- **Backup Recommendation**: Regularly backup leaderboard file

## 🔧 Project Structure

```
Alien-invasion/
├── alien_invasion.py      # Main game file
├── settings.py             # Game settings
├── ship.py                 # Ship class
├── alien.py                # Alien class
├── bullet.py               # Bullet class
├── game_functions.py       # Game functions
├── game_stats.py           # Game statistics
├── scoreboard.py           # Score display
├── button.py               # Game buttons
├── sound_manager.py        # Sound manager
├── leaderboard.py          # Leaderboard management
├── name_input.py           # Name input interface
├── create_images.py        # Image generation script
├── images/                 # Game images
│   ├── ship.bmp           # Ship image
│   ├── alien.bmp          # Alien image
│   └── background.bmp     # Starfield background
├── sounds/                 # Sound effects directory
├── leaderboard.json        # Leaderboard data file
├── requirements.txt        # Dependencies file
└── README.md              # Documentation
```

## 🛠️ Technical Features

### Sound System
- Procedurally generated sound effects, no external audio files needed
- Supports shooting, explosion, game over sounds
- Adjustable volume
- Graceful degradation (still runs without audio device)

### Graphics System
- Procedurally generated game images
- Starfield background with random stars
- Automatic Chinese font detection and loading

### Data Persistence
- JSON format for leaderboard data storage
- UTF-8 encoding supports Chinese
- Automatic backup and recovery

## 📚 Development Notes

The game uses object-oriented design with the following core classes:

- `Ship`: Player-controlled spaceship
- `Alien`: Enemy aliens with formation movement support
- `Bullet`: Bullet system
- `GameStats`: Game statistics management
- `Scoreboard`: Real-time score display
- `Button`: General button component
- `SoundManager`: Sound effects manager
- `Leaderboard`: Leaderboard data management
- `NameInput`: Chinese input interface

## 🎨 Customization Options

Customize by modifying `settings.py`:
- Screen resolution
- Game difficulty
- Ship speed
- Bullet count limit
- Sound settings
- Scoring rules

## 🐛 Troubleshooting

1. **Chinese Display Issues**: Ensure Chinese fonts are installed on system
2. **Sound Not Playing**: Check if audio device is working properly
3. **Game Lag**: Lower game difficulty settings
4. **Image Loading Issues**: Re-run `create_images.py`

## 🧑‍💻 Development Information

### Project Information
- **Project Type**: Python Course Assignment / Game Development Practice
- **Development Language**: Python 3.8+
- **Game Engine**: Pygame 2.6+
- **Development Tools**: VSCode / PyCharm / Other IDEs

### Core Features
- ✅ Complete OOP design pattern
- ✅ Modular code structure
- ✅ Exception handling and error recovery
- ✅ User-friendly interface design
- ✅ Data persistence solutions

### Version History
- **v1.0** - Basic game functionality
- **v2.0** - Sound system integration
- **v3.0** - Leaderboard and UI optimization
- **v4.0** - Four-directional movement and interface beautification

## 📄 License

This project is for learning and teaching purposes only.

### Usage Notes
- Learning and code research allowed
- Secondary development based on this project allowed
- Please retain original copyright information

### Contact
If you have questions or suggestions, welcome feedback and communication.

---

**🎮 Enjoy the game and wish you high scores!**