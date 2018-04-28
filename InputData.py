import numpy as np

POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 20     # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate
DELTA_T = 1/52        # years (length of time step, how frequently you look at the patient)


# transition matrix for warfarin
    # Well     Death Other   TIA          Post-TIA   Mild Stroke  Post-Mild    M/S Stroke   Post-M toS Stroke  Death Stroke
TRANS_MATRIX_WARFARIN = [
    [0.947684,   0.040316,   0.001092,    0.0,       0.0051,        0.0,       0.004824,        0.0,         0.000984],  # Well
    [0.0,        1.0,        0.0,         0.0,       0.0,           0.0,       0.0,             0.0,         0.0],       # Death other
    [0.0,        0.0,        0.0,         1.0,       0.0,           0.0,       0.0,             0.0,         0.0],       # TIA
    [0.0,        0.040316,   0.015743,    0.786684,  0.073525,      0.0,       0.069546,        0.0,         0.014186],  # Post-TIA
    [0.0,        0.0,        0.0,         0.0,       0.0,           1.0,       0.0,             0.0,         0.0],       # Mild Stroke
    [0.0,        0.040316,   0.016835,    0.0,       0.078625,      0.774684,  0.07437,         0.0,         0.01517],   # Post-Mild Stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,           0.0,       0.0,             1.0,         0.0],       # M to S Stroke
    [0.0,        0.040316,   0.01183,     0.0,       0.05525,       0.0,       0.05226,         0.829684,    0.01066],   # Post-M to S Stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,           0.0,       0.0,             0.0,         1.0]        # Dead Stroke
    ]

# transition matrix
    # Well     Death Other   TIA          Post-TIA   Mild Stroke  Post-Mild    M/S Stroke   Post-M toS Stroke  Death Stroke
TRANS_MATRIX_DABIGATRAN_110MG = [
    [0.9501988,  0.0364012,  0.0012194,   0.0,       0.005695,     0.0,        0.0053868,      0.0,          0.0010988],  # Well
    [0.0,        1.0,        0.0,         0.0,       0.0,          0.0,        0.0,            0.0,          0.0],        # Death other
    [0.0,        0.0,        0.0,         1.0,       0.0,          0.0,        0.0,            0.0,          0.0],        # TIA
    [0.0,        0.0364012,  0.015743,    0.7905988, 0.073525,     0.0,        0.069546,       0.0,          0.014186],   # Post-TIA
    [0.0,        0.0,        0.0,         0.0,       0.0,          1.0,        0.0,            0.0,          0.0],        # Mild Stroke
    [0.0,        0.0364012,  0.016835,    0.0,       0.078625,     0.7785988,  0.07437,        0.0,          0.01517],    # Post-Mild Stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,          0.0,        0.0,            1.0,          0.0],        # M to S Stroke
    [0.0,        0.0364012,  0.01183,     0.0,       0.05525,      0.0,        0.05226,        0.8335988,    0.01066],    # Post-M to S Stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,          0.0,        0.0,            0.0,          1.0]         # Dead Stroke
    ]

# transition matrix
    # Well     Death Other   TIA          Post-TIA   Mild Stroke  Post-Mild    M/S Stroke   Post-M toS Stroke  Death Stroke
TRANS_MATRIX_DABIGATRAN_150MG = [
    [0.9551544,  0.0356456,  0.0008372,   0.0,       0.00391,      0.0,        0.0036984,     0.0,           0.0007544],  # Well
    [0.0,        1.0,        0.0,         0.0,       0.0,          0.0,        0.0,           0.0,           0.0],        # Death other
    [0.0,        0.0,        0.0,         1.0,       0.0,          0.0,        0.0,           0.0,           0.0],        # TIA
    [0.0,        0.0356456,  0.015743,    0.7913544, 0.073525,     0.0,        0.069546,      0.0,           0.014186],   # Post-TIA
    [0.0,        0.0,        0.0,         0.0,       0.0,          1.0,        0.0,           0.0,           0.0],        # Mild Stroke
    [0.0,        0.0356456,  0.016835,    0.0,       0.078625,     0.7793544,  0.07437,       0.0,           0.01517],    # Post-Mild Stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,          0.0,        0.0,           1.0,           0.0],        # M to S Stroke
    [0.0,        0.0356456,  0.01183,     0.0,       0.05525,      0.0,        0.05226,       0.8343544,     0.01066],    # Post-M to S Stroke
    [0.0,        0.0,        0.0,         0.0,       0.0,          0.0,        0.0,           0.0,           1.0]         # Dead Stroke
    ]


#  relative risk in increasing mortality
RR = 1.3

HEALTH_UTILITY = [
    0.99,  # well
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
