import os

from gym.envs.registration import register
from d4rl.locomotion import ant
from d4rl.locomotion import maze_env
from d4rl.locomotion import mujoco_goal_env

"""
register(
    id='antmaze-umaze-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.U_MAZE_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_u-maze_noisy_multistart_False_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)
"""

register(
    id='antmaze-lowgear-mediummaze-v1',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.MED_MAZE_TEST,
        'reward_type':'dense',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_u-maze_noisy_multistart_False_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'xml_path':os.path.join(
        os.path.dirname(mujoco_goal_env.__file__),
        'assets',
        'low_gear_ratio_ant.xml'), 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-lowgear-mediummaze-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.MED_MAZE,
        'reward_type':'dense',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_u-maze_noisy_multistart_False_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'xml_path':os.path.join(
        os.path.dirname(mujoco_goal_env.__file__),
        'assets',
        'low_gear_ratio_ant.xml'), 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)



register(
    id='antmaze-lowgear-umaze-v1',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.U_MAZE_TEST,
        'reward_type':'dense',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_u-maze_noisy_multistart_False_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'xml_path':os.path.join(
        os.path.dirname(mujoco_goal_env.__file__),
        'assets',
        'low_gear_ratio_ant.xml'), 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-lowgear-umaze-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.U_MAZE_TEST,
        'reward_type':'dense',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_u-maze_noisy_multistart_False_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'xml_path':os.path.join(
        os.path.dirname(mujoco_goal_env.__file__),
        'assets',
        'low_gear_ratio_ant.xml'), 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-umaze-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.U_MAZE_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_u-maze_noisy_multistart_False_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-umaze-diverse-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.U_MAZE_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_u-maze_noisy_multistart_True_multigoal_True_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-medium-play-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.BIG_MAZE_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_big-maze_noisy_multistart_True_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-medium-diverse-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.BIG_MAZE_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_big-maze_noisy_multistart_True_multigoal_True_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-large-diverse-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.HARDEST_MAZE_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_hardest-maze_noisy_multistart_True_multigoal_True_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-large-play-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.HARDEST_MAZE_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_hardest-maze_noisy_multistart_True_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-eval-umaze-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.U_MAZE_EVAL_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_umaze_eval_noisy_multistart_True_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-eval-umaze-diverse-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=700,
    kwargs={
        'maze_map': maze_env.U_MAZE_EVAL_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_umaze_eval_noisy_multistart_True_multigoal_True_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-eval-medium-play-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.BIG_MAZE_EVAL_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_medium_eval_noisy_multistart_True_multigoal_True_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-eval-medium-diverse-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.BIG_MAZE_EVAL_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_medium_eval_noisy_multistart_True_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-eval-large-diverse-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.HARDEST_MAZE_EVAL_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_large_eval_noisy_multistart_True_multigoal_False_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)

register(
    id='antmaze-eval-large-play-v0',
    entry_point='d4rl.locomotion.ant:make_ant_maze_env',
    max_episode_steps=1000,
    kwargs={
        'maze_map': maze_env.HARDEST_MAZE_EVAL_TEST,
        'reward_type':'sparse',
        'dataset_url':'http://rail.eecs.berkeley.edu/datasets/offline_rl/ant_maze_new/Ant_maze_large_eval_noisy_multistart_True_multigoal_True_sparse.hdf5',
        'non_zero_reset':False, 
        'eval':True,
        'maze_size_scaling': 4.0,
        'ref_min_score': 0.0,
        'ref_max_score': 1.0,
    }
)
