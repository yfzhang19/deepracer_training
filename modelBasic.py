def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    #steering penalty
    #change number based on action space setting
    ABS_STEERING_THRESHOLD=15
    
    #penalize reward if steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward*=0.8
    
    #penalize reward for slowing car
    SPEED_THRESHOLD = 0.15
    if params['speed']<SPEED_THRESHOLD:
        reward *= 0.5
    #change top speed to 2.4
    #train longer
    #chaneg speed

    #how long to train
    #rec At least 2 hours of training
    #what if you change your reward function
    #when it stops increases, it converges
    #what do you rec i do?
    #Yufei, you can clone the model to continue training 1 or 2
    # more hours and increase the max speed a bit, maybe 2m/s.
    # yiu can only see the evaluabtion when you are training

    #trained 1 hour
    return float(reward)