truth_dare_bot/
│
├── main.py
├── config.py
├── handlers/
│   ├── __init__.py
│   ├── start.py
│   ├── help.py
│   ├── alive.py
│   ├── game/
│   │   ├── __init__.py
│   │   ├── solo.py
│   │   ├── multiplayer.py
│   ├── questions/
│   │   ├── __init__.py
│   │   ├── truth.py
│   │   ├── dare.py
│   │   ├── add_question.py
│   │   ├── list_questions.py
│   │   ├── remove_question.py
│   │   ├── penalty.py
│   │   ├── add_penalty.py
│   ├── feedback.py
│   ├── broadcast.py
│   ├── stats.py
│   ├── list_groups.py
│   ├── kplayer.py
│   ├── inline_mode.py
│   ├── change_mode.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── game.py
│   ├── question.py
├── database/
│   ├── __init__.py
│   ├── db_manager.py
│   ├── migrations/
│       ├── __init__.py
│       ├── migration_script.sql
├── utils/
│   ├── __init__.py
│   ├── decorators.py
│   ├── keyboards.py
│   ├── messages.py
│   ├── helpers.py
├── logs/
│   └── bot.log
└── requirements.txt
