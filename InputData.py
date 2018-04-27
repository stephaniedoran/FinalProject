import numpy as np

Hello this is Chloe! 

POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 2     # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate
DELTA_T = 1      # years (length of time step, how frequently you look at the patient)


# transition matrix for warfarin
    # well     death other   TIA       post TIA   mild stroke  post mild  mod to severe  post mod sev  death stroke
TRANS_MATRIX_WARFARIN = [
    [0.947684,   0.040316,   0.001092,    0.0,       0.0051,    0.0,       0.004824,     0.0,         0.000984],  # Well
    [0.0,        1.0,        0.0,         0.0,       0.0,       0.0,       0.0,          0.0,         0.0],       # Death other
    [0.0,        0.0,        0.0,         1.0,       0.0,       0.0,       0.0,          0.0,         0.0],       # TIA
    [0.0,        0.040316,   0.015743,    0.786684,  0.073525,  0.0,       0.069546,     0.0,         0.014186],  # Post-TIA
    [0.0,        0.0,        0.0,         0.0,       0.0,       1.0,       0.0,          0.0,         0.0],       # mild stroke
    [0.0,        0.040316,   0.016835,    0.0,       0.078625,  0.774684,  0.07437,      0.0,         0.01517],   # post mild stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,       0.0,       0.0,          1.0,         0.0],       # moderate to severe
    [0.0,        0.040316,   0.01183,     0.0,       0.0525,    0.0,       0.05226,      0.829684,    0.01066],   # post moderate to severe
    [0.0,        0.0,        0.0,         0.0,       0.0,       0.0,       0.0,          0.0,         1.0]        # dead stroke
    ]

# transition matrix
    # well     death other   TIA        post TIA   mild stroke post mild  mod to severe  post mod sev  death stroke
TRANS_MATRIX_DABIGATRAN_110MG = [
    [0.947684,   0.040316,   0.001092,    0.0,       0.0051,     0.0,       0.004824,     0.0,        0.000984],  # Well
    [0.0,        1.0,        0.0,         0.0,       0.0,        0.0,       0.0,          0.0,        0.0],       # Death other
    [0.0,        0.0,        0.0,         1.0,       0.0,        0.0,       0.0,          0.0,        0.0],       # TIA
    [0.0,        0.040316,   0.015743,    0.786684,  0.073525,   0.0,       0.069546,     0.0,        0.014186],  # Post-TIA
    [0.0,        0.0,        0.0,         0.0,       0.0,        1.0,       0.0,          0.0,        0.0],       # mild stroke
    [0.0,        0.040316,   0.016835,    0.0,       0.078625,   0.774684,  0.07437,      0.0,        0.01517],   # post mild stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,        0.0,       0.0,          1.0,        0.0],       # moderate to severe
    [0.0,        0.040316,   0.01183,     0.0,       0.0525,     0.0,       0.05226,      0.829684,   0.01066],   # post moderate to severe
    [0.0,        0.0,        0.0,         0.0,       0.0,        0.0,       0.0,          0.0,        1.0]        # dead stroke
    ]

# transition matrix
    # well     death other   TIA        post TIA   mild stroke post mild  mod to severe  post mod sev  death stroke
TRANS_MATRIX_DABIGATRAN_150MG = [
    [0.947684,   0.040316,   0.001092,    0.0,       0.0051,    0.0,     0.004824,     0.0,     0.000984],   # Well
    [0.0,        1.0,        0.0,         0.0,       0.0,       0.0,     0.0,          0.0,     0.0],   # Death other
    [0.0,        0.0,        0.0,         1.0,       0.0,       0.0,     0.0,          0.0,     0.0],   # TIA
    [0.0,        0.040316,   0.015743,    0.786684,  0.073525,  0.0,    0.069546,      0.0,    0.014186],   # Post-TIA
    [0.0,        0.0,        0.0,         0.0,       0.0,       1.0,     0.0,          0.0,     0.0],   # mild stroke
    [0.0,        0.040316,   0.016835,    0.0,       0.078625,   0.774684,   0.07437,    0.0,     0.01517], # post mild stroke
    [0.0,        0.0,        0.0,         0.0,     0.0,       0.0,     0.0,          1.0,     0.0],    # moderate to severe
    [0.0,        0.040316,   0.01183,     0.0,     0.0525,     0.0,     0.05226,      0.829684,    0.01066], # post moderate to severe
    [0.0,        0.0,        0.0,         0.0,     0.0,       0.0,     0.0,          0.0,     1.0] # dead stroke
    ]


#  relative risk in increasing mortality
RR = 1.3

HEALTH_UTILITY_WARFARIN = [
    0.987,  # well
    0.0,  # Death other
    0.8,  # TIA
    0.8,  # post TIA
    0.75,  # mild stroke
    0.75,  # post mild stroke
    0.39,  # moderate to severe stroke
    0.39,  # post moderate to severe stroke
    0  # dead stroke
]

HEALTH_UTILITY_DABIGATRAN_110MG = [
    0.994,  # well
    0.0,  # Death other
    0.8,  # TIA
    0.8,  # post TIA
    0.75,  # mild stroke
    0.75,  # post mild stroke
    0.39,  # moderate to severe stroke
    0.39,  # post moderate to severe stroke
    0  # dead stroke
]

HEALTH_UTILITY_DABIGATRAN_150MG = [
    0.994,  # well
    0.0,  # Death other
    0.8,  # TIA
    0.8,  # post TIA
    0.75,  # mild stroke
    0.75,  # post mild stroke
    0.39,  # moderate to severe stroke
    0.39,  # post moderate to severe stroke
    0  # dead stroke
]

HEALTH_COST = [
    0,      # well
    0,      # dead other
    5780,   # TIA
    0,      # post TIA
    8769,   # mild stroke
    28200,  # post mild stroke
    13020,  # moderate to severe stroke
    61440,  # post moderate to severe stroke
    0       # dead stroke
]

WARFARIN_ANNUAL_COST = 390.55
DABIGATRAN_110MG_ANNUAL_COST = 3420.00
DABIGATRAN_150MG_ANNUAL_COST = 4745.00
