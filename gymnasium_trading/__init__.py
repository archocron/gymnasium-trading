from gymnasium.envs.registration import register
register(
    id="GymnasiumTrading-v0",
    entry_point="gymnasium_trading.gym_trading:GymnasiumTradingEnv",
    max_episode_steps=300,
)
